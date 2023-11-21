import requests

url = "https://edamam-recipe-search.p.rapidapi.com/api/recipes/v2"

querystring = {"type":"public","co2EmissionsClass":"A+","field[0]":"uri","beta":"true","random":"true","cuisineType[0]":"American","imageSize[0]":"LARGE","mealType[0]":"Breakfast","health[0]":"alcohol-cocktail","diet[0]":"balanced","dishType[0]":"Biscuits and cookies"}

headers = {
	"Accept-Language": "en",
	"X-RapidAPI-Key": "4ecf27ffd7mshb9e852ab1af37fbp1d65cbjsn70459f614af5",
	"X-RapidAPI-Host": "edamam-recipe-search.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())