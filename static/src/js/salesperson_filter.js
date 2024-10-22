odoo.define('sales_analytic_extension.salesperson_filter', function (require) {
    "use strict";

    var ListView = require('web.ListView');
    var rpc = require('web.rpc');
    var core = require('web.core');

    ListView.include({
        start: function () {
            var self = this;
            this._super.apply(this, arguments);
            if (this.model === 'crm.lead') {
                self._populateSalespersonDropdown();
            }
        },
        _populateSalespersonDropdown: function () {
            var self = this;
            rpc.query({
                model: 'res.users',
                method: 'search_read',
                args: [[], ['id', 'name']],
            }).then(function (salespersons) {
                var dropdown = $('#salesperson_dropdown');
                dropdown.empty();
                dropdown.append('<option value="">All Salespersons</option>');
                _.each(salespersons, function (salesperson) {
                    dropdown.append('<option value="' + salesperson.id + '">' + salesperson.name + '</option>');
                });
                dropdown.on('change', function () {
                    self._filterOpportunitiesBySalesperson($(this).val());
                });
            });
        },
        _filterOpportunitiesBySalesperson: function (salesperson_id) {
            var domain = salesperson_id ? [['user_id', '=', parseInt(salesperson_id)]] : [];
            this.reload({ domain: domain });
        },
    });
});
