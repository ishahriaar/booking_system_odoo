
# from odoo import http


# class BookingErp(http.Controller):
#     @http.route('/booking_erp/booking_erp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_erp/booking_erp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_erp.listing', {
#             'root': '/booking_erp/booking_erp',
#             'objects': http.request.env['booking_erp.booking_erp'].search([]),
#         })

#     @http.route('/booking_erp/booking_erp/objects/<model("booking_erp.booking_erp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_erp.object', {
#             'object': obj
#         })
