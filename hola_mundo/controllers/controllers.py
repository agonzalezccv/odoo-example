# from odoo import http


# class HolaMundo(http.Controller):
#     @http.route('/hola_mundo/hola_mundo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hola_mundo/hola_mundo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hola_mundo.listing', {
#             'root': '/hola_mundo/hola_mundo',
#             'objects': http.request.env['hola_mundo.hola_mundo'].search([]),
#         })

#     @http.route('/hola_mundo/hola_mundo/objects/<model("hola_mundo.hola_mundo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hola_mundo.object', {
#             'object': obj
#         })

