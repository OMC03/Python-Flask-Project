import subprocess
import os
from flask import Flask, request, redirect, url_for
from flask import render_template
from datetime import datetime
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/", methods=["GET", "POST"])
def userdata():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            return redirect(url_for('userdata', name=name))
    name = request.args.get("name", None)
    return render_template(
        "userdata.html",
        name=name,
        date=datetime.now()
    )

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

def run_turtle_script():
    import Lottery_Simulator_Turtle
    Lottery_Simulator_Turtle.main()

@app.route("/lottery/")
def lottery_page():
    return render_template("LotterySim.html")

@app.route("/run-lotto/", methods=["POST"])
def lotterySim():
    try:
        # Start the Turtle script in a separate process
        subprocess.Popen(["python", "Lottery_Simulator_Turtle.py"], cwd=os.path.dirname(os.path.abspath(__file__)))
        return "Lotto game has been started. Check the Turtle graphics window."
    except Exception as e:
        return f"An error occurred: {e}", 500

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")