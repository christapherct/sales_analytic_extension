from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account')

    @api.model
    def create(self, vals):
        sale_order_line = super(SaleOrderLine, self).create(vals)
        customer_type_account = sale_order_line.order_id.partner_id.customer_type_id.analytic_account_id
        product_season_account = sale_order_line.product_id.season_id.analytic_account_id

        if customer_type_account or product_season_account:
            sale_order_line.analytic_account_id = customer_type_account or product_season_account

        return sale_order_line
