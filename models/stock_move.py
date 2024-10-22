from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account')

    @api.model
    def create(self, vals):
        # Check if the stock move is being created from a sale order line
        if vals.get('sale_line_id'):
            sale_line = self.env['sale.order.line'].browse(vals['sale_line_id'])

            # Get the analytic account from the sale order line
            if sale_line.analytic_account_id:
                vals['analytic_account_id'] = sale_line.analytic_account_id.id
                print(sale_line.analytic_account_id, "haii")

        # Create the stock move with the updated values
        return super(StockMove, self).create(vals)