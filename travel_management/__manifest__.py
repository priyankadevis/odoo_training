# -*- coding: utf-8 -*-
{
    'name': "Travel Management",
    'summary': """
            Travel Management summary of the module's purpose, used as
            subtitle on modules listing""",
    'description': """
            Long description of module's purpose
        """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'crm',
        'hr',
    ],
    'data': [
         'security/ir.model.access.csv',
         'views/customer.xml',
    ],
    'license': 'LGPL-3',
    'application': True,
}
