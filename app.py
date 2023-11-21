from flask import Flask, render_template, request

app = Flask(__name__)


@app.get("/")
def recipe_search():


app.run(debug=True)