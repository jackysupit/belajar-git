# -*- coding: utf-8 -*-
{
    'name': 'Warung Odah Kompyang',
    'summary': 'Ini adalah applikasi untuk Warung Odah Kompyang',
    'version': '1.001',
    'category': 'custom',
    'author': 'jeki',
    'maintainer': 'jeki',
    'website':  'natha.com',
    'license': 'AGPL-3',
    'data': [
        'data/kategori.xml',
        'security/ir.model.access.csv',
        'views/produk.xml',
        'views/pesan.xml',
    ],
    'application': True,
    'depends': [
        'sale'
    ]
}