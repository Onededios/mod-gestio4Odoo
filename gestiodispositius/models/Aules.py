from odoo import models, fields

class Aules(models.Model):
    _name = 'gestiodispositius.aules'
    _description = 'Tabla de Aules'

    nom = fields.Char(string='Nom')
    numero = fields.Integer(string='Número')
    pis = fields.Integer(string='Pis')
    ordinadors_disponibles = fields.Boolean(string='Ordinadors Disponibles')
