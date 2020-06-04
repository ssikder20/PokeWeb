from app import app
from flask import render_template, request, jsonify
from app.generation import *

gen_pokemon = gen_read()
generations = get_gen(gen_pokemon)

@app.route('/', methods=['GET', 'POST'])
def index():
    pokemons = ["Please choose a generation, then a pokemon"]

    if request.method == 'POST':
        generation = request.form.get('generation')
        pokemon = request.form.get('pokemon')
        return f"<h1>Generation: {generation}, Pokemon: {pokemon}</h1>"

    return render_template('home.html', generations=generations, pokemons=pokemons)

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