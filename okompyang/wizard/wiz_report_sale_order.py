from odoo import api, fields, models, _, tools
import logging
_logger = logging.getLogger(__name__)



# model_okompyang_wizard_kategori_baru

class WizReportSaleOrder(models.TransientModel):
    _name = "okompyang.wizard.report.sale.order"
    _description = "Ini adalah wizard untuk filter Sale Order yang akan di print"

    date_start = fields.Date(string='')
    date_end = fields.Date(string='')

    


    def do_pilih_sale_order(self):

        print("date_start: ", self.date_start)
        print("date_end: ", self.date_end)

        return True

    def do_print(self):

        date_start = self.date_start
        date_end = self.date_end

        #so_ids = data_sale_order_yang_akan_diprint 
        so_ids = self.env['sale.order'].search([('date_order', '>=', date_start), ('date_order','<=',date_end)])


        #my user id = id user yang sedang login sekarang
        #cari sale.order yang partner_id = user_id atau user_id = user_id
        # user_id = self.env.user.id
        # all_sale_order = self.env['sale.order'].search(['|',('partner_id', '=', user_id), ('user_id','=',user_id)])


        return True


    def do_update_data(self):
        date_start = self.date_start
        date_end = self.date_end
        
        siswa_id = self._context.get('siswa_id')

        """
            browser = adalah function search by id
        """
        # siswa = self.env['okompyang.siswa'].search([('id','=', siswa_id)])
        siswa = self.env['okompyang.siswa'].browse(siswa_id)

        siswa.with_context(date_start=date_start, date_end=date_end).proses_update_data()

