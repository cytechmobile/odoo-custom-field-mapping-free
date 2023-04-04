from odoo import fields, models


class FoundOnUsModel(models.Model):
    _name = 'found.on.us'
    _description = "Found Us From"

    name = fields.Char(string='Name', required=True)
