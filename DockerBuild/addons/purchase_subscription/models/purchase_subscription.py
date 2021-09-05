# Copyright Sudokeys (www.sudokeys.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools import format_date

_logger = logging.getLogger(__name__)


class PurchaseSubscription(models.Model):
    _name = "purchase.subscription"
    _description = "Purchase Subscription"
    _inherit = "mail.thread"

    @api.model
    def get_user_company(self):
        """ Get the company of the user """
        return self.env.user.company_id.id

    state = fields.Selection(
        [
            ("draft", "New"),
            ("open", "In Progress"),
            ("pending", "To Renew"),
            ("close", "Closed"),
            ("cancel", "Cancelled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="draft",
        tracking=True,
    )
    date_start = fields.Date(
        string="Start Date",
        default=fields.Date.today,
        tracking=True,
    )
    date = fields.Date(
        string="End Date",
        help="If set in advance, the subscription will be set to pending 1 month "
        "before the date and will be closed on the date set in this field.",
        tracking=True,
    )
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    recurring_invoice_line_ids = fields.One2many(
        "purchase.subscription.line",
        "p_subscription_id",
        string="Invoice Lines",
        copy=True,
    )
    recurring_rule_type = fields.Selection(
        [
            ("daily", "Day(s)"),
            ("weekly", "Week(s)"),
            ("monthly", "Month(s)"),
            ("yearly", "Year(s)"),
        ],
        string="Recurrency",
        help="Invoice automatically repeat at specified interval",
        required=True,
        default="monthly",
    )
    recurring_interval = fields.Integer(
        string="Repeat Every",
        help="Repeat every (Days/Week/Month/Year)",
        required=True,
        default=1,
    )
    recurring_next_date = fields.Date(
        string="Date of Next Invoice",
        default=fields.Date.today,
        tracking=True,
        help="The next invoice will be created on this date then the period will be extended.",
    )
    recurring_total = fields.Float(
        compute="_compute_recurring_total",
        string="Recurring Price",
        store=True,
        tracking=True,
    )
    description = fields.Text()
    user_id = fields.Many2one("res.users", string="Sales Rep")
    invoice_ids = fields.One2many("account.move", "subscription_id")
    invoice_count = fields.Integer(compute="_compute_invoice_count")
    partner_id = fields.Many2one(
        "res.partner", string="Provider", domain="[('supplier_rank', '>', 0)]"
    )
    code = fields.Char(
        string="Reference",
        index=True,
        default=lambda self: self.env["ir.sequence"].next_by_code(
            "purchase.subscription"
        )
        or "New",
        copy=False,
    )
    user_id = fields.Many2one("res.users", string="Purchases Rep")
    company_id = fields.Many2one(
        "res.company", string="Company", required="True", default=get_user_company
    )
    name = fields.Char(
        string="Contract", required=True, compute="_compute_get_name", store=True
    )
    payment_term_id = fields.Many2one(
        comodel_name="account.payment.term", string="Payment term"
    )
    attachment = fields.Binary(
        string="Attachment",
        attachment=True,
    )
    filename = fields.Char("File Name")

    @api.depends("code", "partner_id")
    def _get_name(self):
        """ Get the name of the subscription : reference - provider """
        for sub in self:
            sub.name = (
                "%s - %s" % (sub.code, sub.partner_id.name)
                if sub.code
                else sub.partner_id.name
            )

    def _track_subtype(self, init_values):
        """ return the subtype state when found in init_values """
        self.ensure_one()
        if "state" in init_values:
            return self.env.ref("purchase_subscription.subtype_state_change_purchase")
        return super(PurchaseSubscription, self)._track_subtype(init_values)

    @api.onchange("partner_id")
    def get_info_partner(self):
        """ Get all the information about the partner """
        for purchase in self:
            currency = False
            payment_term = False
            if purchase.company_id:
                currency = purchase.company_id.currency_id
            if purchase.partner_id:
                if (
                    "property_purchase_currency_id" in purchase.partner_id._fields
                    and purchase.partner_id.property_purchase_currency_id
                ):
                    currency = purchase.partner_id.property_purchase_currency_id
                elif purchase.partner_id.property_product_pricelist:
                    currency = (
                        purchase.partner_id.property_product_pricelist.currency_id
                    )
                if purchase.partner_id.property_supplier_payment_term_id:
                    payment_term = purchase.partner_id.property_supplier_payment_term_id
            purchase.currency_id = currency
            purchase.payment_term_id = payment_term

    def _compute_invoice_count(self):
        """ Compute the number of invoices """
        for sub in self:
            sub.invoice_count = len(sub.invoice_ids)

    @api.depends("recurring_invoice_line_ids")
    def _compute_recurring_total(self):
        """ Compute the reccuring price of the subscription """
        for sub in self:
            sub.recurring_total = sum(
                line.price_subtotal for line in sub.recurring_invoice_line_ids
            )

    @api.model
    def create(self, vals):
        """ Set the reference of the subscription before creation """
        vals["code"] = (
            vals.get("code")
            or self.env.context.get("default_code")
            or self.env["ir.sequence"].next_by_code("purchase.subscription")
            or "New"
        )
        if vals.get("name", "New") == "New":
            vals["name"] = vals["code"]
        return super(PurchaseSubscription, self).create(vals)

    def name_get(self):
        """ Get the name of the subscription : reference - provider """
        res = []
        for sub in self:
            name = (
                "%s - %s" % (sub.code, sub.partner_id.name)
                if sub.code
                else sub.partner_id.name
            )
            res.append((sub.id, "%s" % name))
        return res

    def action_subscription_invoice(self):
        """ Show the invoices views """
        return {
            "type": "ir.actions.act_window",
            "res_model": "account.move",
            "views": [
                [self.env.ref("account.view_in_invoice_tree").id, "tree"],
                [self.env.ref("account.view_move_form").id, "form"],
            ],
            "domain": [["id", "in", self.invoice_ids.ids]],
            "context": {"create": False},
            "name": _("Invoices"),
        }

    @api.model
    def cron_purchase_subscription(self):
        """ Compute the end of the subscription """
        today = fields.Date.today()
        next_month = fields.Date.to_string(
            fields.Date.from_string(today) + relativedelta(months=1)
        )

        # set to pending if date is in less than a month
        domain_pending = [("date", "<", next_month), ("state", "=", "open")]
        subscriptions_pending = self.search(domain_pending)
        subscriptions_pending.write({"state": "pending"})

        # set to close if date is passed
        domain_close = [("date", "<", today), ("state", "in", ["pending", "open"])]
        subscriptions_close = self.search(domain_close)
        subscriptions_close.write({"state": "close"})

        return dict(pending=subscriptions_pending.ids, closed=subscriptions_close.ids)

    @api.model
    def _cron_recurring_create_invoice(self):
        """ If subscribed, create an invoice """
        return self._recurring_create_invoice(automatic=True)

    def set_open(self):
        """ Set the subscription status to 'open' """
        return self.write({"state": "open"})

    def set_pending(self):
        """ Set the subscription status to 'pending' """
        return self.write({"state": "pending"})

    def set_cancel(self):
        """ Set the subscription status to 'cancel' """
        return self.write({"state": "cancel"})

    def set_close(self):
        """ Set the subscription status to 'close' """
        return self.write(
            {"state": "close", "date": fields.Date.from_string(fields.Date.today())}
        )

    def _prepare_invoice_data(self):
        """ Prepare the data of the invoice """
        self.ensure_one()

        if not self.partner_id:
            raise UserError(
                _("You must first select a Customer for Subscription %s!") % self.name
            )

        # Get the fiscal position of the company
        fpos_id = (
            self.env["account.fiscal.position"]
            .with_context()
            .get_fiscal_position(self.partner_id.id)
            .with_company(self.company_id.id)
        )
        # Get the purchase journal of the company
        journal = self.env["account.journal"].search(
            [("type", "=", "purchase"), ("company_id", "=", self.company_id.id)],
            limit=1,
        )
        if not journal:
            raise UserError(
                _('Please define a purchase journal for the company "%s".')
                % (self.company_id.name or "",)
            )

        next_date = fields.Date.from_string(self.recurring_next_date)
        periods = {
            "daily": "days",
            "weekly": "weeks",
            "monthly": "months",
            "yearly": "years",
        }
        new_date = next_date + relativedelta(
            **{periods[self.recurring_rule_type]: self.recurring_interval}
        )

        return {
            "move_type": "in_invoice",
            "partner_id": self.partner_id.id,
            "journal_id": journal.id,
            "invoice_date": self.recurring_next_date,
            "invoice_origin": self.code,
            "fiscal_position_id": fpos_id,
            "currency_id": self.currency_id and self.currency_id.id or False,
            "invoice_payment_term_id": self.payment_term_id
            and self.payment_term_id.id
            or self.partner_id.property_supplier_payment_term_id.id,
            "company_id": self.company_id.id,
            "narration": _("This invoice covers the following period: %s - %s")
            % (format_date(self.env, next_date), format_date(self.env, new_date)),
        }

    def _prepare_invoice_line(self, line, fiscal_position):
        """ Prepare the invoice line """
        account_id = line.product_id.property_account_expense_id
        if not account_id:
            account_id = line.product_id.categ_id.property_account_expense_categ_id
        account_id = fiscal_position.map_account(account_id).id

        tax = line.taxes_id or line.product_id.supplier_taxes_id.filtered(
            lambda r: not line.company_id or r.company_id == line.company_id
        )
        tax = fiscal_position.map_tax(tax, line.product_id, self.partner_id)

        return {
            "name": line.name,
            "account_id": account_id,
            "price_unit": line.price_unit or 0.0,
            "discount": line.discount,
            "quantity": line.quantity,
            "product_id": line.product_id.id,
            "tax_ids": [(6, 0, tax.ids)],
        }

    def _prepare_invoice_lines(self, fiscal_position):
        """ Prepare the invoice lines """
        self.ensure_one()
        fiscal_position = self.env["account.fiscal.position"].browse(fiscal_position.id)
        return [
            (0, 0, self._prepare_invoice_line(line, fiscal_position))
            for line in self.recurring_invoice_line_ids
        ]

    def _prepare_invoice(self):
        """ Prepare the invoice """
        invoice = self._prepare_invoice_data()
        invoice["invoice_line_ids"] = self._prepare_invoice_lines(
            invoice["fiscal_position_id"]
        )
        return invoice

    def recurring_invoice(self):
        """ Reccuring the invoice """
        self._recurring_create_invoice()
        return self.action_subscription_invoice()

    @api.returns("account.move")
    def _recurring_create_invoice(self, automatic=False):
        AMobj = self.env["account.move"]
        invoices = []
        current_date = fields.Date.today()
        periods = {
            "daily": "days",
            "weekly": "weeks",
            "monthly": "months",
            "yearly": "years",
        }
        domain = (
            [("id", "in", self.ids)]
            if self.ids
            else [("recurring_next_date", "<=", current_date), ("state", "=", "open")]
        )
        sub_data = self.search_read(fields=["id", "company_id"], domain=domain)
        for company_id in {data["company_id"][0] for data in sub_data}:
            sub_ids = [
                s["id"]
                for s in [s for s in sub_data if s["company_id"][0] == company_id]
            ]
            subs = (
                self.with_context(company_id=company_id)
                .browse(sub_ids)
                .with_company(company_id)
            )
            for sub in subs:
                try:
                    new_invoice = AMobj.create(sub._prepare_invoice())
                    invoices.append(new_invoice)
                    sub.invoice_ids = [(4, invoices[-1].id, _)]
                    invoices[-1]._recompute_tax_lines()
                    invoices[-1]._compute_amount()
                    next_date = fields.Date.from_string(
                        sub.recurring_next_date or current_date
                    )
                    rule, interval = sub.recurring_rule_type, sub.recurring_interval
                    new_date = next_date + relativedelta(**{periods[rule]: interval})
                    sub.write({"recurring_next_date": new_date})
                    if automatic:
                        self.env.cr.commit()
                    msg_body = _(
                        "Invoice created <a href=# data-oe-model=account.move "
                        "data-oe-id=%d>See invoice</a>."
                    ) % (new_invoice.id)
                    sub.message_post(body=msg_body)
                except Exception:
                    if automatic:
                        self.env.cr.rollback()
                        _logger.exception(
                            "Fail to create recurring invoice for subscription %s",
                            sub.code,
                        )
                    else:
                        raise
        return invoices

    def increment_period(self):
        """ Get the date of the next occurrence """
        for account in self:
            current_date = (
                account.recurring_next_date
                or self.default_get(["recurring_next_date"])["recurring_next_date"]
            )
            periods = {
                "daily": "days",
                "weekly": "weeks",
                "monthly": "months",
                "yearly": "years",
            }
            new_date = fields.Date.from_string(current_date) + relativedelta(
                **{periods[account.recurring_rule_type]: account.recurring_interval}
            )
            account.write({"recurring_next_date": new_date})

    @api.model
    def name_search(self, name, args=None, operator="ilike", limit=100):
        """ Search the name of a partner in the subscription list """
        args = args or []
        domain = ["|", ("code", operator, name), ("name", operator, name)]
        partners = self.env["res.partner"].search(
            [("name", operator, name)], limit=limit
        )
        if partners:
            domain = ["|"] + domain + [("partner_id", "in", partners.ids)]
        rec = self.search(domain + args, limit=limit)
        return rec.name_get()
