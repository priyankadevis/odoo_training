import datetime
from datetime import timedelta

from odoo import models, fields, api


class SakthiStudent(models.Model):
    _name = "sakthi.student"
    _description = "Type Student Records"
    _order = "register_no"
    _rec_name = "register_no"

    _sql_constraints = [
        ('unique_register_no', 'unique (register_no)', 'Register no. is unique!')
    ]

    sequence = fields.Integer("Sequence", default=10)
    register_no = fields.Char(readonly=True)
    name = fields.Char(string="Name")
    gender = fields.Selection([('male', "Male"),
                               ('female', "Female"),
                               ('other', "Transgender")], required=True)
    dob = fields.Date("DOB")
    age = fields.Integer(compute="_compute_age")
    fee_ids = fields.One2many("student.fee", "student_id", "Fee (INR)")
    sslc_mark = fields.Float("SSLC Mark")
    type_course = fields.Selection([('junior', 'Junior'),
                                    ('senior', 'Senior'),
                                    ('short hand', 'Short Hand')])
    admi = fields.Date("Date of Admission")
    aadhar = fields.Integer("Aadhaar", required=True)
    phn_no = fields.Char("Phone Number")
    address = fields.Char()
    doj = fields.Date("Date of Joining")
    dol = fields.Date("Date of Leaving", compute="_compute_dol")

    @api.depends('doj')
    def _compute_dol(self):
        for record in self:
            if record.doj:
                after_six_month = record.doj + timedelta(days=180)
                record.dol = after_six_month
            else:
                record.dol = None

    @api.depends('dob')
    def _compute_age(self):
        for record in self:
            record.ensure_one()
            if record.dob:
                age_calc = (datetime.datetime.today().date() - record.dob).days / 365
                print(age_calc)
                record.age = round(age_calc)
            else:
                record.age = 0

    # def name_get(self):
    #     res = []
    #     for record in self:
    #         if record.student_name and record.type_course:
    #             res.append((record['id'], "%s@%s" % (record.student_name, record.type_course)))
    #         elif record.student_name:
    #             res.append((record['id'], "%s" % (record.student_name)))
    #         else:
    #             res.append((record['id'], _("No Named Student")))
    #     return res

    def _default_currency_id(self):
        return self.env.user.company_id.currency_id

    @api.model
    def create(self, values):
        print(values)
        values['register_no'] = self.env['ir.sequence'].next_by_code('sakthi.student') or ('New')
        return super(SakthiStudent, self).create(values)
