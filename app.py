from flask import Flask, render_template, request, session
from edamam_api import random_recipe

app = Flask(__name__)

# app.secret_key = secrets.token_hex()
# print(app.secret_key)


@app.route('/', methods=['POST'])
def homepage_form_post():
    ingredient = request.form['ingredient']
    return render_template('homepage.html', ingredient=ingredient)

@app.get('/')
def homepage_random_ingredient():
    rand_recipe = random_recipe()
    rand_ingredient = rand_recipe[0]
    return render_template('homepage.html', rand_ingredient=rand_ingredient, rand_recipe=rand_recipe)

# @app.get("/<name>")
# def display_recipes():
#

app.run(debug=True)