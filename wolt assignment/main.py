from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api():
    return jsonify(delivery_fee=960)


if __name__ == "__main__":
    app.run()
