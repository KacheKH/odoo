# -*- coding: utf-8 -*-
from openerp import http

# class Petro(http.Controller):
#     @http.route('/petro/petro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/petro/petro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('petro.listing', {
#             'root': '/petro/petro',
#             'objects': http.request.env['petro.petro'].search([]),
#         })

#     @http.route('/petro/petro/objects/<model("petro.petro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('petro.object', {
#             'object': obj
#         })