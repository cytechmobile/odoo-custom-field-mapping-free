from odoo import fields, models


class CompanyLegacyModel(models.Model):
    _name = 'company.legacy'
    _description = "Company Legacy"

    name = fields.Char(string='Name', required=True)
