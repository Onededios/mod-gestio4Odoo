from odoo import models, fields

class Dispositius(models.Model):
    _name = 'gestiodispositius.dispositius'
    _description = 'Tabla de Dispositius'

    nom_aula = fields.Many2one('gestiodispositius.aules', string='Nom Aula')
    id = fields.Integer(string='ID')
    tipus_dispositiu = fields.Char(string='Tipus de Dispositiu')
    estat = fields.Selection([('averiado', 'Averiado'), ('disponible', 'Disponible'), ('reparando', 'Reparando'), ('roto', 'Roto')], string='Estat') 
