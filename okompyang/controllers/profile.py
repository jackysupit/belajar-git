# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import content_disposition, request
from odoo.tools import html_escape
from odoo.http import content_disposition, Controller, request, route


class MyController(Controller):
    @route('/andi', auth='public')
    def andi(self):
        return 'HALO INI andi'


class PartnerController(Controller):

    @route([['/kom'],['/kom2'],'/kom3'], type='http', auth="user", website=True)
    def partner_name(self):
        return "Halo Jek"
        # partner = request.env.user.partner_id  # Get the partner associated with the current user
        # return http.request.render('otraining.partner_name_template', {'partner': partner})


# class TBXLSXReport(http.Controller):
#     @http.route('/sale_dynamic_xlsx_reports', type='http', auth='user',
#                 methods=['POST'], csrf=False)
#     def get_report_xlsx(self, model, options, output_format, report_data,
#                         report_name, dfr_data):
#         """Generate a dynamic sale report in Excel format and send it as a
#         response to a HTTP POST request."""