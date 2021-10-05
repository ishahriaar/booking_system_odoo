

from odoo import models, fields, api


class HotelList(models.Model):
    _name = 'hotels.list'
    _description = 'Nearby Hotels'

    name = fields.Char(string="Hotel Name")
    location = fields.Selection([
        ('dhaka', 'Dhaka'),
        ('ctg', 'Chattogram')
    ], string='Location')

    status = fields.Selection([
        ('available', 'Available'),
        ('unavailable', 'Unavailable')
    ], string='Status')

    total_room = fields.Integer(string='Available Room')
    bookingID = fields.One2many('book.hotel', 'room_user', string='Booking Info')

    def action_url(self):
        return {
            'res_model': 'book.hotel',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': self.env.ref('booking_erp.booking_view_form').id,
            'target': 'new'
        }



