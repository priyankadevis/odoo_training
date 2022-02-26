# -*- coding: utf-8 -*-
{
    'name': "Sakthi Institute",
    'summary': """
        Sakthi Institute summary of the module's purpose, used as
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
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/student_fee.xml',
    ],
    'license': 'LGPL-3',
    'application': True,
}
