# insecure_addon/__manifest__.py
{
    'name': "Insecure Addon",
    'version': "1.0",
    'category': "Testing",
    'summary': "A deliberately vulnerable module for scanner testing",
    'description': """
        - Missing ir.model.access.csv  
        - Permissive record rule  
        - Public method with no permission checks  
        - Unsafe SQL interpolation  
        - eval() on unsanitized input  
        - QWeb t-raw vulnerability
    """,
    'author': "Test Suite",
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/insecure_menus.xml',
        'views/insecure_views.xml',
        'views/insecure_templates.xml',
        'security/record_rules.xml',
    ],
    'installable': True,
}
