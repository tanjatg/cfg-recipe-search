import requests
import random


def recipe_search(ingredient):
    APP_ID = "1615c37c"
    APP_KEY = "55c93edaaee28bc3ad1ffea9ca66f8b4"
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, APP_ID, APP_KEY)
    )
    data = result.json()
    return data['hits']


def search_by_time(time):
    APP_ID = "1615c37c"
    APP_KEY = "55c93edaaee28bc3ad1ffea9ca66f8b4"
    result = requests.get('https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&time={}&random=true'.format(APP_ID, APP_KEY, time))
    data = result.json()
    return data['hits']


def search_by_cuisine(cuisineType):
    APP_ID = "1615c37c"
    APP_KEY = "55c93edaaee28bc3ad1ffea9ca66f8b4"
    result = requests.get('https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&cuisineType={}&random=true'.format(APP_ID, APP_KEY, cuisineType))
    data = result.json()
    print(data)
    return data['hits']


def search_by_calorie(calories):
    APP_ID = "1615c37c"
    APP_KEY = "55c93edaaee28bc3ad1ffea9ca66f8b4"
    result = requests.get('https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&calories={}&random=true'.format(APP_ID, APP_KEY, calories))
    data = result.json()
    print('https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&calories={}&random=true'.format(APP_ID, APP_KEY, calories))
    return data["hits"]


def random_ingredient():
    ingredients = [
        "almond", "anchovy", "apple", "apricot", "artichoke", "asparagus", "avocado", "aubergine",
        "bacon", "beans", "banana", "bamboo", "barley", "basil", "beef", "beer", "beet", "berry", "bream", "bok choi", "brie", "bulgur", "butternut", "buttermilk", "broccoli", "bell pepper",
        "cabbage", "cake", "camembert", "capers", "carrot", "cashew", "cauliflower", "catfish", "cavolo nero", "celery", "cheese", "cherry", "chestnut", "chicken", "chickpea", "chocolate", "chorizo", "coconut", "coffee", "coriander", "corn", "crab", "couscous", "courgette", "cress", "cucumber", "currant", "cumin",
        "daikon", "dandelion", "date", "dill", "duck",
        "eel", "egg", "elderflower",
        "fennel", "fig", "feta", "flour", "fish", "fruit",
        "gammon", "garlic", "ginger", "gnocchi", "grape", "goose",
        "haddock", "halloumi", "hare", "ham", "hazelnut", "honey", "horseradish",
        "jam", "kale", "ketchup", "kiwi", "kohlrabi", "kipper",
        "lamb", "lardons", "leek", "lemon", "lime", "lettuce", "lentil",
        "mackerel", "mango", "meat", "mayonnaise", "melon", "milk", "mint", "mince", "miso", "mushroom", "mustard", "mutton",
        "noodles", "nuts", "nutmeg", "nettle",
        "oats", "octopus", "olive", "okra", "onion", "orange", "oregano", "oyster",
        "pak choi", "pancetta", "paneer", "papaya", "pasta", "parmesan", "paprika", "passion fruit", "passata", "parsnip", "parsley", "pastry", "peach", "peas", "peanut", "pear", "pecan", "pheasant", "pineapple", "pistachio", "plaice", "plantain", "pomegranate", "plum", "pork", "potato", "prawn", "pumpkin",
        "quail", "quinoa", "rabbit", "radish", "raisins", "rice", "rhubarb", "risotto", "rosemary", "rocket", "ricotta",
        "sage", "salad", "salmon", "sardine", "sausage", "scallop", "sea bass", "seafood", "seaweed", "sesame", "shallot", "soup", "spaghetti", "squid", "spring onion", "spinach", "steak", "swede", "sweet potato",
        "tea", "teriyaki", "tofu", "tilapia", "tomato", "turnip", "turmeric", "truffle", "tortellini", "trout", "turkey",
        "vanilla", "veal", "venison", "walnut", "wine", "yam", "yoghurt"
    ]
    random_ingredient = random.choice(ingredients)
    return random_ingredient


def random_recipe():
    rand_ingredient = random_ingredient()
    ingredient = rand_ingredient
    list = [ingredient]
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']['label']
        url = result['recipe']['url']
        image = result['recipe']['image']
        list.append({'recipe': recipe, 'url': url, 'image': image})
    return list


# def testrun():
#     results = search_by_calorie('100')
#     for result in results:
#         recipe = result['recipe']
#         print(recipe)
#         print(recipe['label'])
#         print(recipe['uri'])
#         print(recipe['image'])
#
#
# testrun()
