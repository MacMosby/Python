from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper




@app.route("/")
def hello_world():
    return "<h1>Hello, big World!</h1>"


@app.route("/bye")
@make_bold
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
