from odoo import api, fields, models

class SeasonMaster(models.Model):
    _name = 'season.master'
    _description = 'Season Master'

    name = fields.Char(string='Season Name', required=True)
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account', readonly=True)

    @api.model
    def create(self, vals):
        season_record = super(SeasonMaster, self).create(vals)
        analytic_plan = self.env['account.analytic.plan'].search([('name', '=', 'Season')], limit=1)
        if not analytic_plan:
            analytic_plan = self.env['account.analytic.plan'].create({
                'name': 'Season',
            })
        if analytic_plan:
            analytic_account = self.env['account.analytic.account'].create({
                'name': season_record.name,
                'plan_id': analytic_plan.id,
            })
            season_record.analytic_account_id = analytic_account.id
        else:
            analytic_account = self.env['account.analytic.account'].create({
                'name': season_record.name,
                'plan_id': analytic_plan.id,
            })
            season_record.analytic_account_id = analytic_account.id

        return season_record
