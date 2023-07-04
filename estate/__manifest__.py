{
    'name': 'Estate',
    'version': '1.0',
    'summary': 'Empty module for managing real estate properties',
    'description': 'This module provides basic functionality for managing real estate properties.',
    'category': 'Uncategorized',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        ],
}
