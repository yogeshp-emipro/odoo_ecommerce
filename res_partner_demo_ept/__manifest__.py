{
    'name': "Partner Demo EPT",
    'version': "1.4",
    'author': "Yogesh Pandey",
    'description': "This module is for demonstration and learning purpose only...",
    'summary': "Localization Information",
    'website': 'https://www.emiprotechnologies.com',
    'depends': ['sales_team', 'website_sale', 'website'],
    'data': ['security/ir.model.access.csv',
             'views/res_partner_demo_ept_views.xml',
             'views/templates.xml'],
    'assets': {
        'web.assets_frontend': ['res_partner_demo_ept/static/src/js/custom_get_product_data.js']
    },
    'demo': ['data/partner_demo_ept4.xml']
}
