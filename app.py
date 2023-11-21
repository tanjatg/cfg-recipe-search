from flask import Flask, render_template, request
from edamam_api import recipe_request

app = Flask(__name__)
@app.get("/")
def homepage_search():
    search_request = recipe_request()
    return render_template("homepage.html", search_request=search_request)

@app.get("/<name>")
def display_recipes():


app.run(debug=True)