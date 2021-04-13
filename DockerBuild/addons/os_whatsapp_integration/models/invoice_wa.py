from odoo import _, models


class WhatsappInvoice(models.Model):
    _inherit = 'account.move'

    def invoice_whatsapp(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Whatsapp Message'),
                'res_model': 'whatsapp.message.wizard',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_template_id': self.env.ref('os_whatsapp_integration.invoice_whatsapp_template').id},
                }
