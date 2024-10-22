from odoo import api, fields, models


class CustomerTypeMaster(models.Model):
    _name = 'customer.type.master'
    _description = 'Customer Type Master'

    name = fields.Char(string='Customer Type', required=True)
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account', readonly=True)

    @api.model
    def create(self, vals):
        # Create the customer.type.master record
        customer_type_record = super(CustomerTypeMaster, self).create(vals)

        # Create the Analytic Account under the 'Customer Type' Analytic Plan
        analytic_plan = self.env['account.analytic.plan'].search([('name', '=', 'Customer Type')], limit=1)
        if not analytic_plan:
            analytic_plan = self.env['account.analytic.plan'].create({
                'name': 'Customer Type',
            })
        if analytic_plan:
            analytic_account = self.env['account.analytic.account'].create({
                'name': customer_type_record.name,
                'plan_id': analytic_plan.id,
            })
            customer_type_record.analytic_account_id = analytic_account.id
        else:
            analytic_account = self.env['account.analytic.account'].create({
                'name': customer_type_record.name,
                'plan_id': analytic_plan.id,
            })
            customer_type_record.analytic_account_id = analytic_account.id

        return customer_type_record
