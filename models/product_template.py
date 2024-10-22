from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    season_id = fields.Many2one('season.master', string='Season')
