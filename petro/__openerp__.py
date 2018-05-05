# -*- coding: utf-8 -*-
{
    'name': "Petro",

    'summary': "Inventario Productos",

    'description': """
        Módulo diseñado para el manejo de inventario de productos
    """,


    'author': "SaintRec",
    'website': "http://www.saintrec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Databases',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/petro.xml',
        'data/web_planner_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # only loaded in demonstration mode
    # 'demo': [
    #   'demo/demo.xml',
    # ],
}
