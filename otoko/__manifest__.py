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
    'data': [
        'security/ir.model.access.csv',
        'views/product.xml',
    ],
    'application': True,
    'depends': [
        'sale'
    ]
}