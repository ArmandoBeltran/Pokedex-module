# ~*~ coding: utf-8 ~*~

from odoo import fields, models

class PokedexPokemonMove(models.Model): 
    _name = 'pokedex.pokemon.move'
    _inherit = ['image.mixin']

    name = fields.Char()
    description = fields.Char()
    power = fields.Char()
    type_id = fields.Many2one('pokedex.pokemon.type')