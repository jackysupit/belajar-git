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

    def do_kategori_baru(self):
        action =  {
            'name': 'Tulis Nama Kategori Yang Diinginkan',
            'type': 'ir.actions.act_window',
            'res_model': 'okompyang.wizard.kategori.baru',  # Ganti dengan nama model yang Anda inginkan
            'view_mode': 'form',  # Mode tampilan untuk window baru
            'target': 'new',  # Buka window baru di tab baru
        }

        return action

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

    def do_pilih_makanan(self):
        ctx = self.env.context
        ids = ctx.get('active_ids', [])
        siswa_id = ctx.get('siswa_id')

        if siswa_id:
            siswa = self.env['okompyang.siswa'].browse(siswa_id)
            
            siswa.with_context(produk_ids=ids).do_pilih_makanan()

        return True
