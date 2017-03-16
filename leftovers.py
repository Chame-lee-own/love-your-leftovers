import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask("MyApp")

@app.route("/welcome")
def welcome():
    return render_template("leftover.html")

@app.route("/<name>")
def hello_someone(name):
    return render_template("leftover.html", name=name.title())



@app.route("/bye/<name>")
def bye_someone(name):
    return render_template("leftover.html", bye=True, name=name.title())

@app.route("/goodbye/<name>/<time>")
def bye_custom(name, time):
    return render_template("leftover.html", bye=True, name=name.title())


@app.route("/signup", methods=['POST'])
def sign_up():
    form_data = request.form
    print form_data['first ingredient']
    print form_data['second ingredient']
    return "That's submitted!"



app.run(debug=True)
