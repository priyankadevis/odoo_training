import datetime
from datetime import timedelta

from odoo import models, fields, api


class StudentFee(models.Model):
    _name = "student.fee"
    _description = "Type Student Records"

    student_id = fields.Many2one('sakthi.student', string="Name")
    fee_invoice_no = fields.Char(default='New')
    fee = fields.Monetary("Fee (INR)", default=500, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True,
                                  default=lambda self: self._default_currency_id())

    date = fields.Date()

    def _default_currency_id(self):
        return self.env.user.company_id.currency_id

    @api.model
    def create(self, values):
        print(values)
        values['fee_invoice_no'] = self.env['ir.sequence'].next_by_code('student.fee') or ('New')
        return super(StudentFee, self).create(values)
