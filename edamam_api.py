import requests

# querystring = {"type" :"public","co2EmissionsClass":"A+","field[0]":"uri","beta":"true","random":"true","cuisineType[0]":"American","imageSize[0]":"LARGE","mealType[0]":"Breakfast","health[0]":"alcohol-cocktail","diet[0]":"balanced","dishType[0]":"Biscuits and cookies"}
#
# APP_ID = "1615c37c"
# APP_KEY = "55c93edaaee28bc3ad1ffea9ca66f8b4"
#
# INGREDIENT = input("What do you want to search for? ")
#
# REQUEST = requests.get(f"https://api.edamam.com/search?q={INGREDIENT}&app_id={APP_ID}&app_key={APP_KEY}")
#
# recipe_test = REQUEST.json()
#
# print(recipe_test)
def recipe_search(ingredient):
    APP_ID = "1615c37c"
    APP_KEY = "55c93edaaee28bc3ad1ffea9ca66f8b4"
    result = requests.get(
    'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, APP_ID,
    APP_KEY)
    )
    data = result.json()
    return data['hits']
def run():
    ingredient = input('What do you want to search for? ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print(recipe['image'])
        print()

run()