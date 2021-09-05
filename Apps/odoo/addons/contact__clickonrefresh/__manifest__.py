# -*- coding: utf-8 -*-
{
    'name': "Contact Clickonrefresh",

    'summary': """
        This app is in development, keep an eye for new features coming soon
    """,

    'description': """
        This app is in development, keep an eye for new features coming soon
    """,

    'author': "Clickonrefresh",
    'website': "https://clickonrefresh-dashboard.netlify.app",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],


    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

