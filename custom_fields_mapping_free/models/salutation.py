from odoo import fields, models


class SalutationModel(models.Model):
    _name = 'salutation'
    _description = "Salutation"

    name = fields.Char(string='Name', required=True)
