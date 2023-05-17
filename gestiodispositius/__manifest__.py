# -*- coding: utf-8 -*-
{
    'name': "Gestio de Dispositius",

    'summary': """
        Modulo de gestion de dispositivos de un centro.""",

    'description': """
        El mòdul en qüestió es basa en l'organització i l'estat dels diferents dispositius que hi ha a l'institut. Es divideix en diverses taules en què primer està l'aula en què aquestes sales si tenen dispositius es gestionen de la manera següent i en el darrer cas serà els tècnics que gestiona la reparació o canvi del dispositiu. Això ens permet una organització senzilla i còmoda per als tècnics que volen veure l'estat, canviar-ho o fer les reparacions adients.
    """,

    'author': "JAJA",
    'website': "https://github.com/Onededios/mod-gestio4Odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',
    'application': 'true',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/aules.xml',
        'views/dispositius.xml',
        'views/tecnics.xml',
        'views/templates.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
