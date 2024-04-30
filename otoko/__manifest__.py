# -*- coding: utf-8 -*-
{
    'name': 'Toko Kelontong',
    'summary': 'Ini adalah applikasi untuk Toko Kelontong',
    'version': '1.001',
    'category': 'custom',
    'author': 'Goesde Rai',
    'maintainer': 'Goesde Rai',
    'website':  'natha.com',
    'license': 'AGPL-3',
    'icon': '/otoko/static/description/icon.png',
    'data': [
        'security/ir.model.access.csv',
        'data/otoko_sequences.xml',
        'views/product.xml',
        'views/sale.xml',
        # 'views/my_sale.xml',
    ],
    'application': True,
    'depends': [
        'sale',
        'okompyang'
    ]
}