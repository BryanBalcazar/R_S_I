# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloIsp(http.Controller):
#     @http.route('/modulo_isp/modulo_isp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_isp/modulo_isp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_isp.listing', {
#             'root': '/modulo_isp/modulo_isp',
#             'objects': http.request.env['modulo_isp.modulo_isp'].search([]),
#         })

#     @http.route('/modulo_isp/modulo_isp/objects/<model("modulo_isp.modulo_isp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_isp.object', {
#             'object': obj
#         })

