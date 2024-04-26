from odoo import api, fields, models, _, tools
from datetime import datetime

#inherit Model = ini data akan di commit ke database 
#inherit TranscientModel = ini data hanya akan disimpan sementara, nanti akan dihapus oleh odoo

class Pesan(models.TransientModel):
    _name = 'okompyang.pesan'
    _description = 'ini untuk message box'

    name = fields.Char(readonly=True)


    def popup(self, pesan, title = 'Pesan'):
        ctx = {
            'default_name': pesan
        }

        return {
            'name': title,
            'type': 'ir.actions.act_window',
            'res_model': 'okompyang.pesan',  # Ganti dengan nama model yang Anda inginkan
            'view_mode': 'form',  # Mode tampilan untuk window baru
            'target': 'new',  # Buka window baru di tab baru
            'context': ctx,
        }        