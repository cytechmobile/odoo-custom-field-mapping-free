# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Custom Fields Mapping',
    'version': '1.0.3',
    'sequence': 1,
    'author': 'Cytech',
    'maintainer': 'Cytech',
    'category': 'Extra Tools',
    'website': 'https://www.cytechmobile.com/',
    'summary': 'Custom Fields Mapping is an Odoo module that will allow you to map custom fields from CRM-Leads to the Contacts module.',
    'description': "Custom Fields Mapping is an Odoo module that will allow you to map custom fields from CRM-Leads to the Contacts module.",
    'depends': ['crm', 'base', 'web', 'contacts', 'partner_autocomplete'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/my_custom_property.xml',
        'views/crm_lead_extent_views.xml',
        'views/partner_extended_view.xml',
        'views/lead_owner_id_views.xml',
        'views/lead_status_views.xml',
        'views/found_on_us_views.xml',
        'views/interested_in_views.xml',
        'views/salutation_views.xml',
        'views/currency_views.xml',
        'views/company_legacy_views.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
        ],
    },
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'license': 'GPL-3',
}
