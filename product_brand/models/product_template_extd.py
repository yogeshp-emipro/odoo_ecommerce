from odoo import fields, models


class ProductTemplateExtd(models.Model):
    _inherit = 'product.template'

    product_brand_ept_id = fields.Many2one(comodel_name='product.brand.ept', string='Product Brand',
                                           help='id of the product brand ')

    def _search_get_detail(self, website, order, options):
        res = super(ProductTemplateExtd, self)._search_get_detail(website=website, order=order, options=options)

        attrib_values = options.get('attrib_values')
        if attrib_values:
            ids = []
            for value in attrib_values:
                if value[0] == 0:
                    ids.append(value[1])
            res['base_domain'].append([('product_brand_ept_id.id', 'in', ids)])
        return res
