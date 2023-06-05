from odoo import http
from odoo.http import request
from odoo.osv import expression
from odoo.addons.website_sale.controllers.main import WebsiteSale


class ProductBrand(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        result = super(ProductBrand, self).shop(page=page, category=category, search=search, min_price=min_price,
                                                max_price=max_price, ppg=ppg, **post)

        brands = request.env['product.brand.ept']
        allbrands = brands.search([])
        result.qcontext['brands'] = allbrands
        return result
