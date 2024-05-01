# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import content_disposition, request
from odoo.tools import html_escape
from odoo.http import content_disposition, Controller, request, route

class PartnerController(Controller):

    @route(['/peserta/profile'], type='http', auth="user", website=True)
    def do_profile(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_profile', {'partner': partner})

    @route(['/peserta/profile/edit'], type='http', auth="user", website=True)
    def do_profile_edit(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_profile_edit', {'partner': partner})

    @route(['/peserta/profile/edit/corporat'], type='http', auth="user", website=True)
    def do_profile_edit_corporat(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_profile_edit_corporat', {'partner': partner})
