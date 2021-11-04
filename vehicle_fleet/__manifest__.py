{

    'name': 'Vehicle fleet',

    'version': '1.0.0',

    'category': 'Vehicle fleet',

    'summary': 'Vehicle fleet',

    'author': 'Leonel Valentinetti',

    'depends': [
        'base',
    ],

    'data': [
        'data/ir_sequence.xml',
        'data/logistic_stage.xml',
        'security/logistic_security.xml',
        'security/ir.model.access.csv',
        'views/logistic_view.xml',
        'views/logistic_stage_view.xml',
        'wizard/wizard_create_logistic_view.xml',
        'views/stock_picking_view.xml',
        'views/carrier_partner_view.xml',
        'views/stock_picking_view.xml',
        'views/menu.xml',
    ],

    'demo': [
        'data/demo.xml',
    ],

    'installable': True,

    'auto_install': False,

    'application': True,

    'description': 'Gestion de logistica personalizada',

}

