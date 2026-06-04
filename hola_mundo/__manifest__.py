# -*- coding: utf-8 -*-
{
    'name': "Hola Mundo",
    'summary': "Mi primer módulo de prueba en Odoo .sh",
    'version': '19.0.1.0.0',
    'author': "Anderson Gonzalez",
    'category': 'Pruebas',
    'depends': ['base'],
    'data': [
         'views/views.xml',
         'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': True,
}