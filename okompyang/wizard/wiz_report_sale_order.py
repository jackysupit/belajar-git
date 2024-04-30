from odoo import api, fields, models, _, tools
from odoo.exceptions import UserError, ValidationError

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



    def do_print(self):
        date_start = self.date_start
        date_end = self.date_end

        fields = ['name','partner_id','amount_total','state',]
        """
            di odoo, kita bisa mengambil data dari model dengan cara: 

            data_sale_order = self.env['sale.order'].search_read(...) # ini akan return array field yang kita pilih 
            
            data_sale_order = self.env['sale.order'].search(...) # ini akan return list of object record
            
            data_sale_order = self.env['sale.order'].search_count(...) # ini akan return integer hasil count(records)
            
            data_sale_order = self.env['sale.order'].browse([ids]) # mirip dengan search(), bedanya, akan error jika id tidak ditemukan. jadi harus pasti yakin id exists dulu 
        """
        data_sale_order = self.env['sale.order'].search_read(fields=fields, domain=[('date_order', '>=', date_start), ('date_order','<=',date_end)])
        if not data_sale_order:
            raise UserError(_('Tidak ada data sale pada range tanggal tersebut'))

        param_data = {
            'title': 'Print Sale Order Periode',
            'periode': '{} - {}'.format(date_start, date_end),
            'data_sale_order': data_sale_order,
        }

        # ini mengambil action yang kita buat di file report_sale_order.xml
        action = self.env.ref("okompyang.action_report_sale_order").report_action([], data=param_data)
        
        
        #discard_logo_check=True parameter ini untuk menghilangkan space ksong di atas yang biasanya digunakan untuk kop surat
        action = self.env.ref("okompyang.action_report_sale_order").with_context(discard_logo_check=True).report_action([], data=param_data)

        return action