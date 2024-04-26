# -*- coding: utf-8 -*-
{
    'name': 'Pusat Training Indonesia',
    'summary': 'Ini adalah applikasi untuk Pusat Training Indonesia',
    'version': '1.001',
    'category': 'custom',
    'author': 'jeki',
    'maintainer': 'jeki',
    'website':  'odooindonesia.com',
    'license': 'AGPL-3',
    'data': [
        'views/siswa/profile.xml',
        'views/siswa/profile_edit.xml',
        'views/siswa/profile_edit_corporat.xml',
        'views/siswa/login.xml',
        'views/siswa/logout.xml',
        'views/siswa/password_reset.xml',
        'views/siswa/password_otp.xml',
        'views/siswa/password_new.xml',
        'views/siswa/registrasi_personal.xml',
        'views/siswa/registrasi_corporat.xml',
        'views/siswa/registrasi_done.xml',
        'views/siswa/training.xml',
        'views/siswa/training_detail.xml',
        'views/siswa/corporat_member_list.xml',
        'views/siswa/corporat_member_add.xml',
        'views/siswa/corporat_pic.xml',
        'views/siswa/kelas.xml',
        'views/siswa/training_daftar_corporat.xml',
        'views/siswa/training_daftar_personal.xml',
    ],
    'application': True,
    'depends': [
        'web'
    ]
}