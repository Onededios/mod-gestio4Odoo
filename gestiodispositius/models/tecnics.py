from odoo import models, fields

class Tecnics(models.Model):
    _name = 'gestiodispositius.tecnics'
    _description = 'Tabla de Pecnics'

    nom = fields.Char(string='Nom')
    dni = fields.Char(string='DNI')
    dispositiu_id = fields.Many2one('gestiodispositius.dispositius', string='ID del Dispositiu')
