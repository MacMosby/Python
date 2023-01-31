from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.date.today().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<some_name>")
def guess(some_name):
    name = some_name
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog")
def blog():
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
