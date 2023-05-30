odoo.define('res_partner_demo_ept.custom_get_product_data',function(require){
'use strict';
var ajax= require('web.ajax');
var publicWidget = require('web.public.widget');

publicWidget.registry.websiteCustomData = publicWidget.Widget.extend({
    selector: '#wrapwrap',
    events: {
        'click .product_data': '_onClickGetProductData',
    },
    _onClickGetProductData:function(){
        alert('Testing')
        ajax.jsonRpc('/product_data', 'call').then(function(data) {
                        $(".product_div").html(data);
        });
    },})
})
