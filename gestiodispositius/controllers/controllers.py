# -*- coding: utf-8 -*-
# from odoo import http


# class Gestiodispositius(http.Controller):
#     @http.route('/gestiodispositius/gestiodispositius', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestiodispositius/gestiodispositius/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestiodispositius.listing', {
#             'root': '/gestiodispositius/gestiodispositius',
#             'objects': http.request.env['gestiodispositius.gestiodispositius'].search([]),
#         })

#     @http.route('/gestiodispositius/gestiodispositius/objects/<model("gestiodispositius.gestiodispositius"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestiodispositius.object', {
#             'object': obj
#         })
