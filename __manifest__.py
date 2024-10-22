{
    'name': 'Sales Analytic Extension',
    'version': '17.0',
    'category': 'Accounting/Analytic',
    'summary': 'Manage seasons and customer types with analytic account integration in sales and stock moves',
    'description': """
        This module provides functionality to manage season and customer types with
        analytic accounts, integrates them into sales order lines and stock valuation.
    """,
    'author': 'Christapher Thomas',
    'depends': ['sale_management', 'account', 'stock', 'base', 'contacts', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/season_master_view.xml',
        'views/customer_type_master_view.xml',
        'views/product_template_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml',
    ],

    'installable': True,
    'application': False,
}
