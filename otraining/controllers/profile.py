# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import content_disposition, request
from odoo.tools import html_escape
from odoo.http import content_disposition, Controller, request, route

class PartnerController(Controller):

    @route(['/satu'], type='http', auth="user", website=True)
    def do_satu(self):
        # return "Halo Jek"
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_satu', {'partner': partner})
    
    @route(['/dua'], type='http', auth="user", website=True)
    def do_dua(self):
        # return "Halo Jek"
        partners = request.env['res.partner'].search([])
        return http.request.render('otraining.page_dua', {'partners': partners})