from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)


class CRMLeadExtendModel(models.Model):
    _name = "crm.lead"
    _inherit = 'crm.lead'

    x_cytech_custom_field_mapping_crm_lead_firstname = fields.Char(string='Firstname')
    x_cytech_custom_field_mapping_crm_lead_lastname = fields.Char(string='Lastname')
    x_cytech_custom_field_mapping_crm_lead_industry = fields.Char(string='Industry (Legacy)')
    x_cytech_custom_field_mapping_crm_lead_created_time = fields.Datetime(string='Created Time')
    x_cytech_custom_field_mapping_crm_lead_skype_id = fields.Char(string='Skype ID')
    x_cytech_custom_field_mapping_crm_lead_email_opt_out = fields.Boolean(string='Email opt-out')
    x_cytech_custom_field_mapping_crm_lead_vat_no = fields.Char(string='VAT No')
    x_cytech_custom_field_mapping_crm_lead_secondary_email = fields.Char(string='Secondary Email')
    x_cytech_custom_field_mapping_crm_lead_job_description = fields.Char(string='Job Description')
    x_cytech_custom_field_mapping_crm_lead_tax_office = fields.Char(string='Tax Office')
    x_cytech_custom_field_mapping_crm_lead_competitor = fields.Char(string='Competitor')
    x_cytech_custom_field_mapping_crm_lead_lead_owner_id = fields.Many2one('lead.owner.id', 'Lead Owner ID (Legacy)')
    x_cytech_custom_field_mapping_crm_lead_lead_status = fields.Many2one('lead.status', 'Lead Status (Legacy)')
    x_cytech_custom_field_mapping_crm_lead_found_on_us = fields.Many2one('found.on.us', 'Found On Us')
    x_cytech_custom_field_mapping_crm_lead_interested_in = fields.Many2one('interested.in', 'Interested In')
    x_cytech_custom_field_mapping_crm_lead_salutation = fields.Many2one('salutation', 'Salutation')
    x_cytech_custom_field_mapping_crm_lead_currency = fields.Many2one('currency', 'Currency (Legacy)')
    x_cytech_custom_field_mapping_crm_lead_company_legacy = fields.Many2one('company.legacy', 'Company (Legacy)')

    def _prepare_customer_values(self, partner_name, is_company=False, parent_id=False):
        _logger.info("CRMLeadExtendModel - _prepare_customer_values - start")

        res = super()._prepare_customer_values(partner_name, is_company, parent_id)
        custom_properties = self.env['my.custom.property'].search([])
        for custom_property in custom_properties:
            temp_transfer_value = self[custom_property.field_name]
            if type(temp_transfer_value).__name__ == 'str' or type(temp_transfer_value).__name__ == 'int' or type(
                    temp_transfer_value).__name__ == 'bool' or type(temp_transfer_value).__name__ == 'datetime' or type(
                temp_transfer_value).__name__ == 'date':
                res[custom_property.field_name] = self[custom_property.field_name]
            else:
                res[custom_property.field_name] = self[custom_property.field_name].id
        _logger.info("CRMLeadExtendModel - _prepare_customer_values - end")
        return res
