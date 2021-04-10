# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import Warning


class EmployeeTransfer(models.Model):
    _name = 'employee.transfer'
    _description = 'Employee Transfer'
    _order = "id desc"

    def _default_employee(self):
        emp_ids = self.env['hr.employee'].search([('user_id', '=', self.env.uid)])
        return emp_ids and emp_ids[0] or False

    name = fields.Char(string='Name', help='Give a name to the Transfer', copy=False, default="/", readonly=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True,
                                  help='Select the employee you are going to transfer')
    date = fields.Date(string='Date', default=fields.Date.today(), help="Date")
    branch = fields.Many2one('transfer.company', string='Transfer Branch', help="Branch", copy=False, required=True)

    state = fields.Selection(
        [('draft', 'New'), ('cancel', 'Cancelled'), ('transfer', 'Transferred'), ('done', 'Done')],
        string='Status', readonly=True, copy=False, default='draft',
        help=" * The 'Draft' status is used when a transfer is created and unconfirmed Transfer.\n"
             " * The 'Transferred' status is used when the user confirm the transfer. It stays in the open status till the other branch/company receive the employee.\n"
             " * The 'Done' status is set automatically when the employee is Joined/Received.\n"
             " * The 'Cancelled' status is used when user cancel Transfer."
    )
    sequence_number = fields.Integer(string='Sequence Number', help='A unique sequence number for the Transfer',
                                     default=1, copy=False)
    company_id = fields.Many2one('res.company', string='Company',
                                 related='employee_id.company_id', help="Company")
    note = fields.Text(string='Internal Notes', help="Specify notes for the transfer if any")
    transferred = fields.Boolean(string='Transferred', copy=False, default=False, compute='_get_transferred', help="Transferred")
    responsible = fields.Many2one('hr.employee', string='Responsible', default=_default_employee, readonly=True, help="Responsible person for the transfer")

    def _get_transferred(self):
        if self:
            if self.branch.company_id == self.env.user.company_id.id:
                self.transferred = True
            else:
                self.transferred = False

    def transfer(self):
        obj_emp = self.env['hr.employee'].browse(self.employee_id.id)
        emp = {}
        if not self.branch:
            raise Warning(_(
                'You should select the transfer branch/company.'))
        if self.branch.company_id == self.company_id.id:
            raise Warning(_(
                'You cant transfer to same company.'))
        for this in self:
            emp = {
                'name': self.employee_id.name,
                'company_id': self.branch.company_id

            }
        new_emp = self.env['hr.employee'].sudo().create(emp)
        if obj_emp.address_home_id:
            obj_emp.address_home_id.active = False
        for obj_contract in self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id)]):
            if obj_contract.date_end:
                continue
            if not obj_contract.date_end:
                obj_contract.write({'date_end': date.today().strftime(DEFAULT_SERVER_DATE_FORMAT)})
                self.wage = obj_contract.wage
        self.state = 'transfer'
        self.employee_id = new_emp
        obj_emp.write({'active': False})

    
    def receive_employee(self):
        for this in self:
            if this._context is None:
                context = {}
            partner = {}
            for i in this:
                partner = {
                    'name': i.employee_id.name,
                    'company_id': i.branch.company_id,
                }
            partner_created = self.env['res.partner'].create(partner)
            self.env['hr.employee'].browse(this.employee_id.id).write({'address_home_id': partner_created.id})
            return {
                'name': _('Contract'),
                'view_mode': 'form',
                'res_model': 'hr.contract',
                'type': 'ir.actions.act_window',
                'target': 'current',
                'context': {'default_employee_id': this.employee_id.id,
                            'default_date_start': this.date,
                            'default_emp_transfer': this.id,
                            },
            }


    def cancel_transfer(self):
        obj_emp = self.env['hr.employee'].browse(self.employee_id.id)
        emp = {
            'name': self.employee_id.name,
            'company_id': self.company_id.id,
        }
        obj_emp.write(emp)
        for obj_contract in self.env['hr.contract'].search([('employee_id', '=', self.employee_id.id)]):
            obj_contract.unlink()
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        vals['name'] = "Transfer Of " + self.env['hr.employee'].browse(vals['employee_id']).name
        res = super(EmployeeTransfer, self).create(vals)
        return res
