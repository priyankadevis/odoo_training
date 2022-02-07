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
        'security/ir.model.access.csv',
        'views/student.xml',

    ],
    'license': 'LGPL-3',
    'application': True,
}
