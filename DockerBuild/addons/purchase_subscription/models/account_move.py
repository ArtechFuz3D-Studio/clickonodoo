# Copyright Sudokeys (www.sudokeys.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    subscription_id = fields.Many2one(
        comodel_name="purchase.subscription", string="Purchase subscription"
    )
