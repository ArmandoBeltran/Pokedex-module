# ~*~ coding: utf-8 ~*~

from odoo import fields, models

class PokedexPokemon(models.Model): 
    _name = 'pokedex.pokemon'
    _inherit = ['image.mixin']

    name = fields.Char()
    preevolution_id = fields.Many2one('pokedex.pokemon')
    evolution_ids = fields.One2many('pokedex.pokemon', 'preevolution_id')
    description = fields.Char()
    sequence = fields.Integer()
    height = fields.Float()
    weight = fields.Float()
    type_ids = fields.Many2many('pokedex.pokemon.type')
    move_ids = fields.Many2many('pokedex.pokemon.move')
    color = fields.Integer(string = 'Color Index', default = 0)

