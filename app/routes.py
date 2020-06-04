from app import app
from flask import render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import SelectField
from app.generation import *

gen_pokemon = gen_read()
generations = get_gen(gen_pokemon)

class Form(FlaskForm):
    generation = SelectField('generation', choices=generations)
    pokemon = SelectField('pokemon', choices=[])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Form()

    if request.method == 'POST':
        pokemon = form.pokemon.data
        return f"<h1>Generation: {form.generation.data}, Pokemon: {pokemon}</h1>"

    return render_template('home.html', form=form)

@app.route('/pokemon/<generation>')
def get_pokemon(generation):
    pokemons = gen_pokemon[generation]

    pokemon_arr = []
    for pokemon in pokemons:
        pokeObj = {}
        pokeObj['nat_dex'] = pokemon[0]
        pokeObj['name'] = pokemon[1]
        pokemon_arr.append(pokeObj)
    
    return jsonify({'pokemon' : pokemon_arr})