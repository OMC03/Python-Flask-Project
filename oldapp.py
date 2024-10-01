import re
from datetime import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)

print ("http://127.0.0.1:5000/hello/VSCode")
print ("http://127.0.0.1:5000/api/data")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")