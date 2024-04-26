# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import content_disposition, request
from odoo.tools import html_escape
from odoo.http import content_disposition, Controller, request, route

class SiswaController(Controller):
    @route(['/siswa/registrasi'], type='http', auth="user", website=True)
    def do_registrasi_personal(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_registrasi_personal', {'partner': partner})

    @route(['/siswa/registrasi/corporat'], type='http', auth="user", website=True)
    def do_registrasi_corporat(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_registrasi_corporat', {'partner': partner})


    @route(['/siswa/registrasi/done'], type='http', auth="user", website=True)
    def do_registrasi_done(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_registrasi_done', {'partner': partner})

    @route(['/siswa/edit'], type='http', auth="user", website=True)
    def do_training_edit(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_profile', {'partner': partner})

    @route(['/siswa/login'], type='http', auth="user", website=True)
    def do_siswa_login(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_siswa_login', {'partner': partner})

    @route(['/siswa/logout'], type='http', auth="user", website=True)
    def do_siswa_logout(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_siswa_logout', {'partner': partner})

    @route(['/siswa/password/reset'], type='http', auth="user", website=True)
    def do_siswa_password_reset(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_siswa_password_reset', {'partner': partner})

    @route(['/siswa/password/otp'], type='http', auth="user", website=True)
    def do_siswa_password_otp(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_siswa_password_otp', {'partner': partner})

    @route(['/siswa/password/new'], type='http', auth="user", website=True)
    def do_siswa_password_new(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_siswa_password_new', {'partner': partner})

    @route(['/siswa/training'], type='http', auth="user", website=True)
    def do_training(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_training', {'partner': partner})

    @route(['/siswa/training/detail'], type='http', auth="user", website=True)
    def do_training_detail(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_training_detail', {'partner': partner})

    @route(['/siswa/corporat/member/list'], type='http', auth="user", website=True)
    def do_corporat_member_list(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_corporat_member_list', {'partner': partner})

    @route(['/siswa/corporat/member/add'], type='http', auth="user", website=True)
    def do_corporat_member_add(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_corporat_member_add', {'partner': partner})

    @route(['/siswa/training/daftar/personal'], type='http', auth="user", website=True)
    def do_training_data_personal(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_training_daftar_personal', {'partner': partner})

    @route(['/siswa/training/daftar/corporat'], type='http', auth="user", website=True)
    def do_training_data_corporat(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_training_daftar_corporat', {'partner': partner})

    @route(['/siswa/corporat/pic'], type='http', auth="user", website=True)
    def do_corporat_pic(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_corporat_pic', {'partner': partner})

    @route(['/siswa/kelas'], type='http', auth="user", website=True)
    def do_siswa_kelas(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_siswa_kelas', {'partner': partner})
