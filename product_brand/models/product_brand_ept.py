from odoo import fields, models


class ProductBrandEpt(models.Model):
    _name = 'product.brand.ept'
    _inherit = ['website.published.multi.mixin']
    _description = 'Product Brand Ept'

    # name -> Char
    # website_id -> Many2one("website")
    # logo -> Binary
    # product_ids -> One2many("product.template", "product_brand_ept_id")
    name = fields.Char(string='Name', help='name of the product')
    website_id = fields.Many2one(comodel_name='website', string='Website', help='website id of the product brand')
    logo = fields.Binary(string='Product Logo', help='logo of the product brand')
    product_ids = fields.One2many(comodel_name='product.template', inverse_name='product_brand_ept_id',
                                  string='Products', help='product ids of product brands')
