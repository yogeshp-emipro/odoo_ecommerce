from odoo import fields, models


class ProductTemplateExtd(models.Model):
    _inherit = 'product.template'

    product_brand_ept_id=fields.Many2one(comodel_name='product.brand.ept',string='Product Brand',help='id of the product brand ')
