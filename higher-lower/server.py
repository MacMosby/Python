from random import randint
from flask import Flask

num = randint(0, 9)
print(num)

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess == num:
        return "You're right!"
    elif guess < num:
        return "Too low, try again!"
    else:
        return "Too high, try again!"


if __name__ == "__main__":
    app.run(debug=True)
