# -*- coding: utf-8 -*-
from odoo import models, fields

class HolaMundoTarea(models.Model):
    _name = 'hola.mundo.tarea'
    _description = 'Tareas de Hola Mundo'

    name = fields.Char(string='Título de la Tarea', required=True)
    description = fields.Text(string='Descripción')
    is_done = fields.Boolean(string='¿Completada?', default=False)


# Prueba para heredar  de Contactos y agregar un nuevo campo Status
class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_test_partner = fields.Boolean(
        string='¿Es de prueba?', 
        default=False,
        help='Indica si este contacto es usado para pruebas internas.'
    )