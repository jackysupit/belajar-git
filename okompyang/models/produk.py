from odoo import api, fields, models, _, tools


class Produk(models.Model):
    _name = "okompyang.produk"
    _description = "Ini adalah model produk kompyang"


    name = fields.Char(required=True)
    harga = fields.Integer(string='')
    
    #one2many 
    siswa_ids = fields.One2many('okompyang.siswa', 'produk_id')


    state = fields.Selection(string='Status', selection=[
        ('merah', 'Merah'),
        ('kuning', 'Kuning'),
        ('hijau', 'Hijau'),
        ], default='hijau')

    def do_tambah(self):
        kategori = self.env['okompyang.kategori'].create({
            'name': 'INI-KODE-BARU',
            'keterangan': 'ini adalah isi field keterangan'
        })

        # jika sudah selesai, munculkan popup 

        pesan = 'Kategori berhasil dibuat, id: {}'.format(kategori.id)
        return self.env['okompyang.pesan'].popup(pesan)

        # ctx = {
        #     'default_name': pesan
        # }

        # return {
        #     'name': 'Pesan',
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'okompyang.pesan',  # Ganti dengan nama model yang Anda inginkan
        #     'view_mode': 'form',  # Mode tampilan untuk window baru
        #     'target': 'new',  # Buka window baru di tab baru
        #     'context': ctx,
        # }