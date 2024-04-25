from odoo import api, fields, models, _, tools


class Produk(models.Model):
    _name = "okompyang.produk"
    _description = "Ini adalah model produk kompyang"


    name = fields.Char(required=True)
    harga = fields.Integer(string='')

    state = fields.Selection(string='Status', selection=[
        ('merah', 'Merah'),
        ('kuning', 'Kuning'),
        ('hijau', 'Hijau'),
        ], default='hijau')