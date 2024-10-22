from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_type_id = fields.Many2one('customer.type.master', string='Customer Type')
