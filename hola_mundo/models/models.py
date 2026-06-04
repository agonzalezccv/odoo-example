from odoo import models, fields

class HolaMundoTarea(models.Model):
    _name = 'hola.mundo.tarea'
    _description = 'Tareas de Hola Mundo'

    name = fields.Char(string='Título de la Tarea', required=True)
    description = fields.Text(string='Descripción')
    is_done = fields.Boolean(string='¿Completada?', default=False)