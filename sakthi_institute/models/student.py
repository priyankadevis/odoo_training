# -*- coding: utf-8 -*-

from odoo import models, fields


class SakthiStudent(models.Model):
    _name = "sakthi.student"
    _description = "Student Record"

    register_no = fields.Char()
    name = fields.Char(string="Name")
    gender = fields.Selection([('male', "Male"),
                               ('female', "Female"),
                               ('other', "Transgender")], required=True)
    dob = fields.Date(tracking=True)
    age = fields.Integer(compute="_compute_age")
    fee = fields.Float(default=500)
    sslc_mark = fields.Float()
    type_course = fields.Selection([
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('short hand', 'Short Hand')])
    doj = fields.Datetime("Date of Joining")
    aadhar = fields.Integer("Aadhaar", default=10)
