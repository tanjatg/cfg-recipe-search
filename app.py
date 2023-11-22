from flask import Flask, render_template, request
from edamam_api import random_recipe, recipe_search

app = Flask(__name__)


@app.get('/')
def homepage_random_ingredient():
    rand_recipe = random_recipe()
    rand_ingredient = rand_recipe[0]
    return render_template('homepage.html', rand_ingredient=rand_ingredient, rand_recipe=rand_recipe)


@app.get("/recipes")
def display_recipes():
    ingredient = request.args.get('ingredient')
    recipe_list = recipe_search(ingredient)
    return render_template('search_results.html', ingredient=ingredient, recipe_list=recipe_list)


app.run(debug=True)
