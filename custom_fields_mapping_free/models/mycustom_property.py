from odoo import fields, models
import logging

_logger = logging.getLogger(__name__)


class MyCustomPropertyModel(models.Model):
    _name = 'my.custom.property'
    _description = "My Custom Property"

    field_name = fields.Char(string='Field Name', required=True)
    table_name = fields.Char(string='Table Name')
    field_type = fields.Selection(
        string='Type',
        selection=[('Char', 'Char'), ('Integer', 'Integer')],
        help="Type")

    def action_migrate_custom_fields(self):
        _logger.info("MyCustomPropertyModel - action_migrate_custom_fields - start")
        crm_leads = self.env['crm.lead'].search([])
        for crm_lead in crm_leads:
            custom_properties = self.env['my.custom.property'].search([])
            if crm_lead.partner_id.type == 'contact':
                for custom_property in custom_properties:
                    temp_value = crm_lead[custom_property.field_name]
                    if temp_value:
                        if not crm_lead.partner_id[custom_property.field_name]:
                            crm_lead.partner_id[custom_property.field_name] = temp_value
                            update_vals = {
                                custom_property.field_name: temp_value
                            }
                            crm_lead.partner_id.write(update_vals)
        _logger.info("MyCustomPropertyModel - action_migrate_custom_fields - end")
        return True
