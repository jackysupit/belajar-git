from odoo import api, fields, models, _, tools


class Kategori(models.Model):
    _name = "okompyang.kategori"
    _description = "Ini adalah model kategori produk kompyang"

    name = fields.Char()
    keterangan = fields.Integer()