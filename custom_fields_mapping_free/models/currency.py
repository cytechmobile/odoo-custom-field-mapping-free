from odoo import fields, models


class CurrencyModel(models.Model):
    _name = 'currency'
    _description = "Currency"

    name = fields.Char(string='Name', required=True)
