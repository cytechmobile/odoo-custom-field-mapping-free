from odoo.tests.common import tagged, users
from odoo.addons.crm.tests import common as crm_common
from odoo.addons.mail.tests.common import mail_new_test_user

import logging

_logger = logging.getLogger(__name__)


@tagged('post_install', '-at_install')
class CustomFieldsMappingTestCase(crm_common.TestLeadConvertMassCommon):

    @classmethod
    def setUpClass(cls):
        # add env on cls and many other things
        super(CustomFieldsMappingTestCase, cls).setUpClass()
        _logger.info("CustomFieldsMappingTestCase - setUpClass - after super")

        cls.leads = cls.lead_1 + cls.lead_w_partner + cls.lead_w_email_lost

        cls.company_main = cls.env.user.company_id
        cls.user_manager_cfm = mail_new_test_user(
            cls.env, login='user_manager_cfm',
            name='User Manager CFM', email='cfm_manager@test.example.com',
            company_id=cls.company_main.id,
            notification_type='inbox',
            groups='custom_fields_mapping_free.group_custom_fields_mapping_manager,sales_team.group_sale_manager',
        )

        cls.cfm_team_convert = cls.env['crm.team'].create({
            'name': 'Convert CFM Team',
            'sequence': 10,
            'alias_name': False,
            'use_leads': True,
            'use_opportunities': True,
            'company_id': False,
            'user_id': cls.user_manager_cfm.id,
        })

        _logger.info("CustomFieldsMappingTestCase - setUpClass - after data added")

    @users('user_manager_cfm')
    def test_before_convert_to_opportunity(self):
        """ Test internals mass converted in convert mode, without duplicate management """
        skype_id_text_for_test = "skype-id-added-before"

        (self.lead_w_partner | self.lead_w_email_lost).write({
            'user_id': False
        })

        self.lead_1.write({
            'x_cytech_custom_field_mapping_crm_lead_skype_id': skype_id_text_for_test,
        })

        mass_convert = self.env['crm.lead2opportunity.partner.mass'].with_context({
            'active_model': 'crm.lead',
            'active_ids': self.leads.ids,
            'active_id': self.leads.ids[0]
        }).create({
            'deduplicate': False,
            'user_id': self.user_manager_cfm.id,
            'force_assignment': False,
        })
        # default values
        self.assertEqual(mass_convert.name, 'convert')
        self.assertEqual(mass_convert.action, 'each_exist_or_create')
        # depending on options
        self.assertEqual(mass_convert.partner_id, self.env['res.partner'])
        self.assertEqual(mass_convert.deduplicate, False)
        self.assertEqual(mass_convert.user_id, self.user_manager_cfm)
        self.assertEqual(mass_convert.team_id, self.cfm_team_convert)

        mass_convert.action_mass_convert()
        for lead in self.lead_1 | self.lead_w_partner:
            self.assertEqual(lead.type, 'opportunity')
            if lead == self.lead_w_partner:
                self.assertEqual(lead.user_id, self.env['res.users'])  # user_id is bypassed
                self.assertEqual(lead.partner_id, self.contact_1)
            elif lead == self.lead_1:
                self.assertEqual(lead.user_id, self.user_sales_leads)  # existing value not forced
                new_partner = lead.partner_id
                self.assertEqual(new_partner.name, 'Amy Wong')
                self.assertEqual(new_partner.email, 'amy.wong@test.example.com')
                # This is the point where checking the custom field if its mapped correctly
                self.assertEqual(new_partner.x_cytech_custom_field_mapping_crm_lead_skype_id, skype_id_text_for_test)
