from odoo import fields, models


class LeadOwnerIdModel(models.Model):
    _name = 'lead.owner.id'
    _description = "Lead Owner Id Legacy"

    name = fields.Char(string='Name', required=True)
