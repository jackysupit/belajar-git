from odoo import fields, models, api, _, tools

# HEADER
class Sale(models.Model):
    _name = 'otoko.sale'
    _description = 'This is Sale model of otoko module'

    name = fields.Char(string='Sale Number', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    remark = fields.Char(string='Remark')
    customer_id = fields.Many2one(string='Customer', comodel_name='res.partner', ondelete='restrict')
    date = fields.Datetime(string='Transaction Date', default=fields.Date.today)
    grand_total = fields.Float(string='Grand Total')
    sale_detail_ids = fields.One2many(comodel_name='otoko.sale_detail',inverse_name='sale_id')

    # Override insert
    @api.model
    def create(self, vals):
        if not (vals.get('name') or vals.get('name') == _('New')):
            vals['name'] = self.env['ir.sequence'].next_by_code('otoko_sale_sequence')
            
        return super(Sale, self).create(vals)
    
    # Override update
    def write(self, vals):
        if not self:
            return true
        
        if 'date' not in vals:
            vals['date'] = fields.Date.today()
        
        return super(Sale, self).write(vals)

# DETAIL
class SaleDetail(models.Model):
    _name = "otoko.sale_detail"
    _description = "This is Sale details model of otoko module"

    sale_id = fields.Many2one(comodel_name='otoko.sale', ondelete='restrict')
    product_id = fields.Many2one(comodel_name='otoko.product', ondelete='restrict')
    qty  = fields.Integer(string='QTY')
    item_price  = fields.Integer(string='Item Price', related="product_id.price", store=True) #read only
    sub_total = fields.Integer(string='Total', compute='compute_total', store=True) #read only 
    
    """"
    field compute & related
    - readonly
    - tidak tersimpan di database
    - jika field tidak tersimpan di database, tidak bisa digunakan untuk search & groups
    """
    
    @api.depends('qty', 'item_price')
    def compute_total(self):
        for rec in self:
            rec.sub_total = rec.qty * rec.item_price