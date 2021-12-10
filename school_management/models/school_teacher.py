# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher'

    name = fields.Char()
    department_id = fields.Many2one("college.department", required=True)
    hod_of_dept_id = fields.One2many("college.department", "hod_id")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100