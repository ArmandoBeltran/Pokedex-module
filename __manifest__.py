# ~*~ coding: utf-8 ~*~

{
    'name': 'Pokédex', 
    'version': '0.1', 
    'category': 'Dev', 
    'summary': 'Curso desarrollo Odoo (Pokédex)', 
    'description': """
Curso desarrollo Odoo (Pokedex)
===============================
RST
    """, 
    'depends': [
        'contacts', 
    ] , 
    'data': [
        'security/ir.model.access.csv',
        'views/pokemon_views.xml',
        'views/pokemon_type_views.xml',
        'views/pokemon_move_views.xml',
        'views/res_partner_views.xml',
        'wizard/pokemon_evolve_view.xml'
    ], 
    'installable': True, 
    'auto_install': False, 
}