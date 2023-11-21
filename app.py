from flask import Flask, render_template, request
import edamam_api

app = Flask(__name__)


@app.get("/")
def recipe_search():


app.run(debug=True)