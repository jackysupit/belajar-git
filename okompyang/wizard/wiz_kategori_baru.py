from odoo import api, fields, models, _, tools

# model_okompyang_wizard_kategori_baru

class WizKategoriBaru(models.TransientModel):
    _name = "okompyang.wizard.kategori.baru"
    _description = "Ini adalah wizard untuk membuat kategori baru"


    name = fields.Char(required=True)
