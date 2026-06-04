# -*- coding: utf-8 -*-
from odoo import models, fields, api, Command

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

    @api.model_create_multi
    def create(self, vals_list):
        # 1. Llamamos al método original (super) para que guarde el contacto en la base de datos
        records = super(ResPartner, self).create(vals_list)

        # 2. Lógica para crear la factura de forma automática
        for record in records:
            # Opcional: Puedes poner una condición, por ejemplo, que solo facture a personas jurídicas
            # o dejarlo directo para todos los contactos que se creen.
            self.env['account.move'].create({
                'partner_id': record.id,          # El cliente de la factura es el contacto recién creado
                'move_type': 'out_invoice',       # Factura de cliente
                'state': 'draft',                 # Se crea en estado borrador
                'invoice_line_ids': [
                    Command.create({
                        "name": f"Cargo inicial de apertura - {record.name}",
                        "quantity": 1,
                        "price_unit": 50.00,       # Un monto de ejemplo fijo
                    }),
                    Command.create({
                        "name": "Service Fee",
                        "quantity": 1,
                        "price_unit": 100.00,      # Tu tarifa de servicio fija
                    }),
                ],
            })
        return records