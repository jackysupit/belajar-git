from odoo import api, fields, models, _, tools


class Peserta(models.Model):
    _name = "okompyang.siswa"
    _description = "Ini adalah model untuk siswa"

    name = fields.Char()
    jurusan = fields.Char()
    tanggal = fields.Date(string='')
    
    #many2one
    produk_id = fields.Many2one(string='Produk', comodel_name='okompyang.produk', ondelete='restrict')
    
    produk_ids = fields.Many2many('okompyang.produk', string='Makanan Favorit')

    notes = fields.Text()
    
    date_start = fields.Date(string='Date Start Yang Terakhir Dipilih User')
    date_end = fields.Date(string='Date End Yang Terakhir Dipilih User')


    def do_pilih_makanan(self):
        produk_ids = self._context.get('produk_ids')

        if not produk_ids:
            action =  {
                'name': 'Pilih Makanan Favorit',
                'type': 'ir.actions.act_window',
                'res_model': 'okompyang.produk',  # Replace with your desired model name
                'view_mode': 'list',  # View mode for the new window
                'target': 'new',  # Open in a new tab
                'view_id': self.env.ref('okompyang.okompyang_produk_tree_wizard').id,  # Replace 'your_module_name' with the actual name of your module
                'context': {
                    'create': False,
                    'export_xlsx': False,
                    'siswa_id': self.id,
                    }, 
            }

            return action

        self.produk_ids = [(6, 0, produk_ids)]

    def do_ambil_tanggal(self):
        # action = self.env.ref('model_okompyang_wizard_report_sale_order_action')[0]

        action =  {
            'name': 'Pilih Tanggal',
            'type': 'ir.actions.act_window',
            'res_model': 'okompyang.wizard.report.sale.order',  # Ganti dengan nama model yang Anda inginkan
            'view_mode': 'form',  # Mode tampilan untuk window baru
            'target': 'new',  # Buka window baru di tab baru
        }

        return action

    def penampung_data(self):

        return True

    """
        proses untuk mengupdate date_start dan date_end milik siswa
        dengan date_start dan date_end yang terakhir dipilih
    """
    def proses_update_data(self):
        date_start = self._context.get('date_start')
        date_end = self._context.get('date_end')

        # Jika user belum memilih tanggal, 
        if not date_start:
            # maka suruh dia pilih tanggal dulu 

            ctx = {
                'siswa_id': self.id,
            }
            action =  {
                'name': 'Pilih Tanggal',
                'type': 'ir.actions.act_window',
                'res_model': 'okompyang.wizard.report.sale.order',  # Ganti dengan nama model yang Anda inginkan
                'view_mode': 'form',  # Mode tampilan untuk window baru
                'target': 'new',  # Buka window baru di tab baru
                'context': ctx,  # Buka window baru di tab baru
            }
            return action

        self.write({
            'date_start': date_start,
            'date_end': date_end,
        })        

        # self.date_start = date_start
        # self.date_end = date_end
        return True

