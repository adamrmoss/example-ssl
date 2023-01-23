"""Server for Example SSL website."""

from flask import Flask, render_template

app = Flask(__name__)

# A secret key is needed to use Flask sessioning features
app.secret_key = 'A SECRET KEY'


@app.route("/")
def homepage():
    return render_template("index.html")


if __name__ == "__main__":
    # When running server.py, connect the database and start the webapp
    app.run(host="127.0.0.1", debug=True, port=5001)
