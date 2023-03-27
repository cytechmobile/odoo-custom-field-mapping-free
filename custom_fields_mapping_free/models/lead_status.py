from odoo import fields, models


class LeadStatusModel(models.Model):
    _name = 'lead.status'
    _description = "Lead Status Legacy"

    name = fields.Char(string='Name', required=True)
