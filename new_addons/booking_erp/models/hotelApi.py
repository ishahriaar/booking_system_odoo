import requests
from odoo import models, fields


class HotelApi(models.Model):
    _name = 'hotels.api'
    _description = 'Hotel api'



    url = "https://hotels-com-free.p.rapidapi.com/nice/image-catalog/v2/hotels/106346"

    headers = {
        'x-rapidapi-host': "hotels-com-free.p.rapidapi.com",
        'x-rapidapi-key': "c82515d032mshccc29e53802a2ccp10bf4cjsn4b3eab5c58a5"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

    hotel_name = fields.Char(string="Hotels name", default=response.json()['hotelId'])
    # customer_name = fields.Char(string="Customer Name")
    # customer_address = fields.Char(string="Customer Address")
    # customer_number = fields.Char(string="Customer Number")
    # expected_room = fields.Integer(string="Expected Room")


