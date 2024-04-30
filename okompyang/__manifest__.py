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
        'views/siswa.xml',
        'wizard/wiz_pilih_makanan.xml',
        'wizard/wiz_report_sale_order.xml',

        'report/report_sale_order.xml',
    ],
    'application': True,
    'depends': [
        'sale'
    ],
    'assets': {
        'web.assets_common': [
            ('include', 'web._assets_helpers'),
            'okompyang/static/css/custom.css',
        ],
        'web.assets_backend': [
            'okompyang/static/css/custom.css',
        ]
    }    
}    