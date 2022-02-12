# -*- coding: utf-8 -*-

from odoo import models, fields,


class TypeStudent(models.Model):
    _name = 'type.student'
    _description = 'Institute Students'

    name = fields.char()
    register_no = fields.Char()
    gender = fields.selection([('male', "Male"),
                               ('female', "Female"),
                               ('trangender', "Transgender")]), required = True)

    section = fields.selection([('junior', "Junior"),
                                ('senior', "Senior"),
                                ('short hand', "Shorthand")]), required = True)
    timing = fields.selection()
    dob = fields.Date(tracking=True)
    age = fields.Integer(compute="_compute_age")
    fee = fields.Float(default=10000)
    doj = fields.Datetime("Date of Joining")
    description = fields.Text("About me")
