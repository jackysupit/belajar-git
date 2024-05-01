# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import content_disposition, request
from odoo.tools import html_escape
from odoo.http import content_disposition, Controller, request, route

class PesertaController(Controller):
    @route(['/peserta/registrasi'], type='http', auth="user", website=True)
    def do_registrasi_personal(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_registrasi_personal', {'partner': partner})

    @route(['/peserta/registrasi/corporat'], type='http', auth="user", website=True)
    def do_registrasi_corporat(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_registrasi_corporat', {'partner': partner})


    @route(['/peserta/registrasi/done'], type='http', auth="user", website=True)
    def do_registrasi_done(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_registrasi_done', {'partner': partner})

    @route(['/peserta/edit'], type='http', auth="user", website=True)
    def do_training_edit(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_profile', {'partner': partner})

    @route(['/peserta/login'], type='http', auth="user", website=True)
    def do_peserta_login(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_peserta_login', {'partner': partner})

    @route(['/peserta/logout'], type='http', auth="user", website=True)
    def do_peserta_logout(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_peserta_logout', {'partner': partner})

    @route(['/peserta/password/reset'], type='http', auth="user", website=True)
    def do_peserta_password_reset(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_peserta_password_reset', {'partner': partner})

    @route(['/peserta/password/otp'], type='http', auth="user", website=True)
    def do_peserta_password_otp(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_peserta_password_otp', {'partner': partner})

    @route(['/peserta/password/new'], type='http', auth="user", website=True)
    def do_peserta_password_new(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_peserta_password_new', {'partner': partner})

    @route(['/peserta/training'], type='http', auth="user", website=True)
    def do_training(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_training', {'partner': partner})

    @route(['/peserta/training/detail'], type='http', auth="user", website=True)
    def do_training_detail(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_training_detail', {'partner': partner})

    @route(['/peserta/corporat/member/list'], type='http', auth="user", website=True)
    def do_corporat_member_list(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_corporat_member_list', {'partner': partner})

    @route(['/peserta/corporat/member/add'], type='http', auth="user", website=True)
    def do_corporat_member_add(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_corporat_member_add', {'partner': partner})


    @route(['/peserta/corporat/member/delete'], type='http', auth="user", website=True)
    def do_corporat_member_delete(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_corporat_member_delete', {'partner': partner})

    @route(['/peserta/training/daftar/personal'], type='http', auth="user", website=True)
    def do_training_data_personal(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_training_daftar_personal', {'partner': partner})

    @route(['/peserta/training/daftar/corporat'], type='http', auth="user", website=True)
    def do_training_data_corporat(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_training_daftar_corporat', {'partner': partner})

    @route(['/peserta/corporat/pic'], type='http', auth="user", website=True)
    def do_corporat_pic(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_corporat_pic', {'partner': partner})

    @route(['/peserta/kelas'], type='http', auth="user", website=True)
    def do_peserta_kelas(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_peserta_kelas', {'partner': partner})

    @route(['/peserta/pembayaran/konfirmasi'], type='http', auth="user", website=True)
    def do_peserta_pembayaran_konfirmasi(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_pembayaran_konfirmasi', {'partner': partner})

    @route(['/peserta/pembayaran/done'], type='http', auth="user", website=True)
    def do_peserta_pembayaran_done(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_pembayaran_done', {'partner': partner})


    @route(['/peserta/dashboard'], type='http', auth="user", website=True)
    def do_peserta_dashboard(self):
        partner = request.env.user.partner_id  # Get the partner associated with the current user
        return http.request.render('otraining.page_peserta_dashboard', {'partner': partner})
