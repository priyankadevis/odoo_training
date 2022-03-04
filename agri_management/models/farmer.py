# # -*- coding: utf-8 -*-

from odoo import fields, models

class FarmerRegistration(models.Model):
    _name = 'farmer.registration'
    _description = 'Farmer Registration'
    # _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']

    name = fields.Char(required=True)
    crop_area = fields.Integer(required=True,string="Crop Area (in Acre)")
    nature_cultivation = fields.Selection([('natural farming', "Natural Farming"),
                                           ('organic farming', "Organic Farming"),
                                           ('chemical farming', "Chemical Farming")])
    waste_land = fields.Char(string="Barren (in Acre)")
    land_location = fields.Selection([('puducherry', "PUDUCHERRY"),
                                      ('cuddalore', "CUDDALORE"),
                                      ('villupuram', "VILLUPURAM")])
    mobile = fields.Char()
    address = fields.Text()




# def create(self, values):
    #     print(values)
    #     values['name'] = self.env['ir.sequence'].next_by_code('farmer.registration') or ('New')
    #     return super(FarmerRegistration, self).create(values)
    #
    #
    # def write(self, values):
    #     print(values)
    #     return super(FarmerRegistration, self).write(values)
