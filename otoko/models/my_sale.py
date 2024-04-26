from odoo import fields, models, api
from odoo.exceptions import ValidationError

class MySale(models.Model):
    _inherit = 'sale.order'

    discount = fields.Float()