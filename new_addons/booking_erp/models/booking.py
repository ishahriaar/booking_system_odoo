from odoo import models, fields, api


class HotelBook(models.Model):
    _name = 'book.hotel'
    _description = 'Book a Hotel'

    def _default_user(self):
        return self.env.user.id

    customer_name = fields.Many2one('res.users', string="Customer Name", default=_default_user, required=True,
                                    ondelete='cascade', index=True, readonly=True)
    customer_address = fields.Char(string="Customer Address")
    customer_number = fields.Char(string="Customer Number")
    expected_room = fields.Integer(string="Expected Room")

    room_user = fields.Many2one('hotels.list', string="Hotel Name")

    statusID = fields.Selection([
        ('request', 'Pending'),
        ('approve', 'Approved'),
        ('reject', 'Rejected')
    ], string='Booking Status', default='request', required=True,
                                    index=True, readonly=True)

    def update_new(self):
        for record in self:
            if record.statusID == 'request':
                record.statusID = 'approve'
            elif record.statusID == 'reject':
                record.statusID = 'approve'

    def update_old(self):
        for record in self:
            if record.statusID == 'request':
                record.statusID = 'reject'
            elif record.statusID == 'approve':
                record.statusID = 'reject'





