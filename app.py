from flask import Flask, render_template, request
from edamam_api import random_recipe, recipe_search, search_by_calorie, search_by_cuisine, search_by_time

app = Flask(__name__)


@app.get('/')
def homepage_random_ingredient():
    rand_recipe = random_recipe()
    rand_ingredient = rand_recipe[-1]
    return render_template('homepage.html', rand_ingredient=rand_ingredient, rand_recipe=rand_recipe)


@app.get("/recipes")
def display_recipes():
    ingredient = request.args.get('ingredient')
    recipe_list = recipe_search(ingredient)
    return render_template('search_results.html', ingredient=ingredient, recipe_list=recipe_list)


@app.get("/recipes-by-calories/<calories>")
def display_by_calories(calories):
    recipe_list = search_by_calorie(calories)
    calorie_count = calories
    return render_template('search_recipes_calories.html', recipe_list=recipe_list, calorie_count=calorie_count)


@app.get("/recipes-by-time/<time>")
def display_by_time(time):
    recipe_list = search_by_time(time)
    time_count = time
    return render_template('search_recipes_time.html', recipe_list=recipe_list, time_count=time_count)


@app.get("/recipes-by-cuisine/<cuisineType>")
def display_by_cuisine(cuisineType):
    recipe_list = search_by_cuisine(cuisineType)
    cuisine = cuisineType
    return render_template('search_recipes_cuisine.html', recipe_list=recipe_list, cuisine=cuisine)


app.run(debug=True)
