# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AgricultureCrop(models.Model):
    _name = 'agriculture.crop'
    _description = 'Agriculture Crop'

    crop_name = fields.Char(required=True)
    period_to_produce = fields.Char()
    starting_period = fields.Date()
    ending_period = fields.Date()
    crop_season = fields.Selection([('summer', "Summer"),
                                    ('rainy', "Rainy"),
                                    ('other', "Other")], required=True)
    crop_stock_location = fields.Char()
    disease = fields.Char()
    disease_cure = fields.Char()
    description = fields.Char()
    material_ids = fields.One2many('crop.material', 'agriculture_crop_id')





    def name_get(self):
     res = []
     for record in self:
        if record.crop_name:
            res.append((record['id'], "%s" % (record.crop_name)))
        else:
            res.append((record['id'], _("No Named Crop")))
     return res


    class CropMaterial(models.Model):
         _name = 'crop.material'
         _description = 'Crop Material'

         name=fields.Char(string="Product")
         qty=fields.Integer(string="Quantity")
         uom=fields.Char(string="Unit Of Measures")
         agriculture_crop_id = fields.Many2one('agriculture.crop', string="crop")

