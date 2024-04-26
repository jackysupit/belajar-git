from odoo import fields, models, api, _, tools

class Sale(models.Model):
    _name = 'otoko.sale'
    _description = 'This is Sale model of otoko module'

    name = fields.Char(string='Sale Number', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    remark = fields.Char(string='Remark')

    @api.model
    def create(self, vals):
        if not (vals.get('name') or vals.get('name') == _('New')):
            vals['name'] = self.env['ir.sequence'].next_by_code('otoko_sale_sequence')
            
        return super(Sale, self).create(vals)