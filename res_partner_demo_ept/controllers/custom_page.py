from odoo import http
from odoo.http import request

class CustomPage(http.Controller):

    @http.route(['/custom_page'], type='http', auth="public", website=True)
    def custom_page(self):
        # return 'Hello this the custom template'
        # values = {'subjects': ['Operating System', 'DBMS', 'Data Structure', 'OOPs']}
        # return request.render('res_partner_demo_ept.cssubjects', values)
        res = request.render('res_partner_demo_ept.custompage')
        return res
        # return request.render("website_sale.custompage")

    @http.route(['/product_data'], type='json', auth="public", website=True)
    def get_product_data(self):
        product = request.env['product.template'].search([('website_published','=',True)],limit=1)
        print('Products are :',product)
        values={'product':product}
        return request.render('res_partner_demo_ept.product_data', values)
