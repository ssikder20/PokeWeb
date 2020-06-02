from flask import render_template
from app import app

generations = [
    "Generation 1",
    "Generation 2",
    "Generation 3",
    "Generation 4",
    "Generation 5",
    "Generation 6",
    "Generation 7"
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', generations=generations)