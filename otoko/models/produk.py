from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Produk(models.Model):
    _inherit = 'okompyang.produk'

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    qty = fields.Integer()

    @api.depends('qty', 'harga')
    def compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga

    subtotal = fields.Integer(compute="compute_subtotal")


    state = fields.Selection(string='Status', 
                             selection=[
                                 ('A', 'Active'),
                                 ('I', 'Inactive'),
                             ],
                             default='A')
    color = fields.Selection(string='Warna', 
                             selection=[
                                 ('red', 'Merah'),
                                 ('yellow', 'Kuning'),
                                 ('green', 'Hijau'),
                             ],
                             default='green')
    
    @api.constrains('code')
    def _check_your_field(self):
        for record in self:
            if record.code and len(record.code) < 5:
                raise ValidationError("Code must be at least 5 characters long!")
            
            cari = self.env['otoko.product'].search([('code','=', record.code), ('id', '!=', record.id)])
            if cari:
                raise ValidationError("Code {} is duplicate!".format(record.code))
