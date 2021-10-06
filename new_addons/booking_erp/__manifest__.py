# -*- coding: utf-8 -*-
{
    'name': "iBooking",

    'summary': "",

    'description': "",
    'sequence': 1,

    'author': "BJIT Ltd.",
    'website': "https://bjitgroup.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',


    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/hotel_book_access.xml',
        'security/ir.model.access.csv',


        'views/menu.xml',
        'views/hotels_view.xml',
        'views/booking_view.xml',
        'views/hotel_api_views.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
