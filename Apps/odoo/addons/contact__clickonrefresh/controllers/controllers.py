# -*- coding: utf-8 -*-
from odoo import http


class ContactClickonrefresh(http.Controller):
    @http.route('/contact__clickonrefresh/contact__clickonrefresh/', auth='public')
    def index(self, **kw):
        return "clickonrefresh@gmail.com"
              
    # @http.route('/contact__clickonrefresh/contact__clickonrefresh/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('contact__clickonrefresh.listing', {
    #         'root': '/contact__clickonrefresh/contact__clickonrefresh',
    #         'objects': http.request.env['contact__clickonrefresh.contact__clickonrefresh'].search([]),
    #     })

    # @http.route('/contact__clickonrefresh/contact__clickonrefresh/objects/<model("contact__clickonrefresh.contact__clickonrefresh"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('contact__clickonrefresh.object', {
    #         'object': obj
    #     })
