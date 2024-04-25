from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Product(models.Model):
    _name = 'otoko.product'
    _description = 'This is Product model of otoko module'

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    price = fields.Integer()
    state = fields.Selection(string='Status', 
                             selection=[
                                 ('A', 'Active'),
                                 ('I', 'Inactive'),
                             ],
                             default='A')
    
    @api.constrains('code')
    def _check_your_field(self):
        for record in self:
            if record.code and len(record.code) < 5:
                raise ValidationError("Code must be at least 5 characters long!")
            
            cari = self.env['otoko.product'].search([('code','=', record.code), ('id', '!=', record.id)])
            if cari:
                raise ValidationError("Code is duplicate {} informasi tambahan {} non str: {}".format(record.code, 'ini info tambahan', 789))
