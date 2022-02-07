from odoo import models, fields


class TravelCustomer(models.Model):
    _name = "travel.customer"
    _description = "Passengers"


name = fields.Char(string="Name")
gender = fields.Selection([('male', "Male"),
                           ('female', "Female"),
                           ('other', "Transgender")], required=True)
destination = fields.Char()
phone = fields.Char("Phone")
start_date = fields.Date()
end_date = fields.Date()
