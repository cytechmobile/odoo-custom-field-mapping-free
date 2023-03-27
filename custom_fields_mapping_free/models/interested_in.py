from odoo import fields, models


class InterestedInModel(models.Model):
    _name = 'interested.in'
    _description = "Interested In"

    name = fields.Char(string='Name', required=True)
