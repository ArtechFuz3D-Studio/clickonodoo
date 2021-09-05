# Copyright Sudokeys (www.sudokeys.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class PurchaseSubscriptionLine(models.Model):
    _name = "purchase.subscription.line"
    _description = "Purchase Subscription Line"

    product_id = fields.Many2one(
        "product.product",
        string="Product",
        domain="[('recurring_invoice_po','=',True)]",
        required=True,
    )
    p_subscription_id = fields.Many2one("purchase.subscription", string="Subscription")
    analytic_account_id = fields.Many2one(
        "account.analytic.account", string="Analytic account"
    )
    name = fields.Text(string="Description", required=True)
    quantity = fields.Float(
        compute="_compute_quantity",
        inverse="_inverse_quantity",
        string="Quantity",
        store=True,
        help="Max between actual and buy quantities; this quantity will be invoiced",
    )
    actual_quantity = fields.Float(help="Quantity actually used", default=0.0)
    buy_quantity = fields.Float(help="Quantity buy", required=True, default=1)
    uom_id = fields.Many2one("uom.uom", string="Unit of Measure", required=True)
    discount = fields.Float(string="Discount (%)", digits="Discount", default=0.0)
    price_unit = fields.Float(string="Unit Price", required=True)
    price_subtotal = fields.Monetary(
        compute="_compute_amount",
        string="Sub Total",
        store=True,
        currency_field="currency_id",
    )
    price_total = fields.Monetary(
        compute="_compute_amount",
        string="Total",
        store=True,
        currency_field="currency_id",
    )
    price_tax = fields.Float(compute="_compute_amount", string="Tax", store=True)
    taxes_id = fields.Many2many(
        "account.tax",
        string="Taxes",
        domain=["|", ("active", "=", False), ("active", "=", True)],
    )
    currency_id = fields.Many2one(
        related="p_subscription_id.currency_id",
        store=True,
        string="Currency",
        readonly=True,
    )
    company_id = fields.Many2one(
        "res.company",
        related="p_subscription_id.company_id",
        string="Company",
        store=True,
        readonly=True,
    )

    @api.depends("buy_quantity", "actual_quantity")
    def _compute_quantity(self):
        """ Compute the quantity of item in the line """
        for line in self:
            line.quantity = max(line.buy_quantity, line.actual_quantity)

    def _inverse_quantity(self):
        """ Set the actual quantity of the line """
        for line in self:
            line.actual_quantity = line.quantity

    @api.depends("price_unit", "quantity", "discount", "taxes_id")
    def _compute_amount(self):
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.taxes_id.compute_all(
                price,
                line.p_subscription_id.currency_id,
                line.quantity,
                product=line.product_id,
                partner=line.p_subscription_id.partner_id,
            )
            line.update(
                {
                    "price_tax": sum(
                        t.get("amount", 0.0) for t in taxes.get("taxes", [])
                    ),
                    "price_total": taxes["total_included"],
                    "price_subtotal": taxes["total_excluded"],
                }
            )

    def _compute_tax_id(self):
        for line in self:
            fpos = line.p_subscription_id.partner_id.property_account_position_id
            taxes = line.product_id.supplier_taxes_id.filtered(
                lambda r: not line.company_id or r.company_id == line.company_id
            )
            line.taxes_id = (
                fpos.map_tax(taxes, line.product_id, line.p_subscription_id.partner_id)
                if fpos
                else taxes
            )

    @api.onchange("product_id")
    def onchange_product_id(self):
        """ Used when the product is modified, change the caracteristics of the product """
        contract = self.p_subscription_id
        company_id = contract.company_id.id
        context = dict(self.env.context, company_id=company_id)
        if not self.product_id:
            self.price_unit = 0.0
        else:
            partner = contract.partner_id.with_context(context)
            if partner.lang:
                context.update({"lang": partner.lang})

            product = self.product_id.with_context(context).with_company(company_id)
            self.price_unit = product.standard_price
            self.uom_id = product.uom_po_id.id

            name = product.display_name
            if product.description_purchase:
                name += "\n" + product.description_purchase
            self.name = name
            self._compute_tax_id()
