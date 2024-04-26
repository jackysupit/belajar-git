from odoo import api, fields, models, _, tools
from datetime import datetime

class Kategori(models.Model):
    _name = "okompyang.kategori"
    _description = "Ini adalah model kategori produk kompyang"

    name = fields.Char(required=True, copy=False, readonly=True, default=lambda self: _('New'))
    # name = fields.Char(default=lambda self: self.env['ir.sequence'].next_by_code('okompyang.kategori.seq'))

    keterangan = fields.Char()

    @api.model
    def create(self, vals):
        ymd = datetime.today().strftime('%Y%m%d')  # Mendapatkan tanggal hari ini dalam format YYYYMMDD
        
        if not vals.get('name') or vals.get('name') == _('New'):
            kode = self.env['ir.sequence'].next_by_code('okompyang.kategori.seq')
            nama_baru = "{}-{}".format(kode, ymd)
            vals['name'] = nama_baru
        else:
            print("ini else")

        """
            mengembalikan hasil create 
        """
        return super(Kategori, self).create(vals)