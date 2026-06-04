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
        # 1. Creamos los contactos con la lógica normal de Odoo
        records = super(ResPartner, self).create(vals_list)

        # 2. Iteramos para crear la factura
        for record in records:
            # Buscamos el diario de ventas de la compañía actual
            sales_journal = self.env['account.journal'].search([
                ('type', '=', 'sale'), 
                ('company_id', '=', record.company_id.id or self.env.company.id)
            ], limit=1)

            # VALIDACIÓN SEGURA: 
            # 1. Que exista un diario de ventas en el sistema.
            # 2. Que el contacto sea de tipo 'contact' (evita bots o direcciones secundarias de envío).
            if sales_journal and record.type == 'contact': 
                self.env['account.move'].create({
                    'partner_id': record.id,
                    'move_type': 'out_invoice',
                    'state': 'draft',
                    'journal_id': sales_journal.id,
                    'invoice_line_ids': [
                        Command.create({
                            "name": f"Cargo inicial de apertura - {record.name}",
                            "quantity": 1,
                            "price_unit": 50.00,
                        }),
                        Command.create({
                            "name": "Service Fee",
                            "quantity": 1,
                            "price_unit": 100.00,
                        }),
                    ],
                })
        return records