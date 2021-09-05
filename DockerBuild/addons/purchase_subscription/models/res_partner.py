# Copyright Sudokeys (www.sudokeys.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    po_subscription_count = fields.Integer(
        string="Purchase Subscriptions", compute="_compute_po_subscription_count"
    )

    def _compute_po_subscription_count(self):
        """ Compute the  number of subscription(s) """
        for partner in self:
            partner.po_subscription_count = self.env[
                "purchase.subscription"
            ].search_count([("partner_id", "=", partner.id)])

    def purchase_subscription_action_res_partner(self):
        """ Action on click on the stat button in partner form """
        for partner in self:
            return {
                "type": "ir.actions.act_window",
                "res_model": "purchase.subscription",
                "views": [[False, "tree"], [False, "form"]],
                "domain": [["partner_id", "=", partner.id]],
                "context": {"create": False},
                "name": "Purchase Subscriptions",
            }
