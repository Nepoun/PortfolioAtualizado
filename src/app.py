from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/aboutme.html")
def aboutme():
    return render_template("aboutme.html")

@app.route("/projects.html")
def projects():
    return render_template("projects.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")
    