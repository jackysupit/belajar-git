from odoo import api, fields, models, _, tools


class Siswa(models.Model):
    _name = "okompyang.siswa"
    _description = "Ini adalah model untuk siswa"

    name = fields.Char()
    jurusan = fields.Char()
    tanggal = fields.Date(string='')
    produk_id = fields.Many2one(string='Produk', comodel_name='okompyang.produk', ondelete='restrict')
    