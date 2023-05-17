from odoo import models, fields

class Aules(models.Model):
    _name = 'gestiodispositius.aules'
    _description = 'Tabla de Aules'

    nom = fields.Char(string='Nom')
    numero = fields.Integer(string='Número')
    pis = fields.Integer(string='Pis', selection=[('-1', '-1'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')])
    ordinadors_disponibles = fields.Boolean(string='Ordinadors Disponibles')
