from odoo import api, fields, models, _, tools
import logging
_logger = logging.getLogger(__name__)



# model_okompyang_wizard_kategori_baru

class WizPilihMakanan(models.TransientModel):
    _name = "okompyang.wizard.pilih.makanan"
    _description = "Ini adalah wizard untuk memilih makanan favorit milik siswa"

    # produk_ids = fields.Many2many('okompyang.produk', string='Makanan Favorit', default = lambda self: return self.env['okompyang.produk'].search([]))

    def default_produk_ids(self):
        # all_produk = self.env['okompyang.produk'].search([('name', '=', 'Tahu')])
        # all_produk = self.env['okompyang.produk'].search([('name', 'like', 'Tahu')])
        all_produk = self.env['okompyang.produk'].search([])
        
        # all_produk = [
        #     {id:1, name: apel, harga:1000},
        #     {id:2, name: mangga, harga:2000},
        # ]
        # ids = all_produk.ids    [1, 2]
        # all_names = all_produk.mapped('name') # [apel, mangga]


        # p_ids = []
        # p_names = []
        # for (produk in all_produk) {
        #     p_ids.push(produk.id)
        #     p_names.push(produk.name)
        # }

        print("################## ################## ##################")
        print("################## ################## ##################")
        print("################## ################## ##################")
        print("################## ################## ##################")
        print("################## ################## ##################")
        print("################## ################## ##################")
        print("all_produk: ", all_produk)

        _logger.warning('##########################################')
        _logger.warning('##########################################')
        _logger.warning('##########################################')
        _logger.warning('##########################################')
        _logger.warning('##########################################')
        _logger.warning('##########################################')

        default_value = [(6, 0, all_produk.ids)]
        _logger.warning('all_produk default_value', str(default_value))
        return default_value

    produk_ids = fields.Many2many('okompyang.produk', string='Makanan Favorit', default=default_produk_ids)


    def do_sudah_dipilih(self):
        print("produk dipilih: ", self.produk_ids)

        return self.produk_ids