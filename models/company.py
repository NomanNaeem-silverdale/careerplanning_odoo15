from odoo import models, fields


class CompanyToSettle(models.Model):
    _name = 'company.settle'
    _description = 'Company want to Settle'
    _rec_name = 'type'


    type = fields.Char(string='Company Type')

