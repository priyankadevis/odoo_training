# # -*- coding: utf-8 -*-
#
from odoo import fields, models, _


class FarmerRegistration(models.Model):
    _name = 'farmer.registration'
    _description = 'Farmer Registration'
    # _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']



    name = fields.Char()
    mobile = fields.Char()
    address = fields.Text()
    nature_cultivation = fields.Selection([('natural farming', "Natural farming"),
                                           ('organic farming', "Organic farming"),
                                           ('chemical farming', "Chemical farming")])


    def create(self, values):
        print(values)
        values['name'] = self.env['ir.sequence'].next_by_code('farmer.registration') or ('New')
        return super(FarmerRegistration, self).create(values)


    def write(self, values):
        print(values)
        return super(FarmerRegistration, self).write(values)
