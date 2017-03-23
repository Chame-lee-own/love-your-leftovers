
import os
import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask("MyApp")

my_key = 'a36d8f597d70a074e4866e5c25ff8a6c'

# payload = { 'key': 'a36d8f597d70a074e4866e5c25ff8a6c', 'q':
# 'first ingredient, second ingredient', 'sort': 'r'}

# endpoint1 = 'http://food2fork.com/api/get'
# payload2 = { 'key': 'a36d8f597d70a074e4866e5c25ff8a6c', 'rId': ''}

@app.route("/welcome")
def welcome():
    return render_template("leftover.html")


@app.route("/search", methods=['POST'])
def index():
    endpoint = 'http://food2fork.com/api/search'
    # Since the "payload" depends on what the user types in on your form, it is
    # easier to put it inside this function here so that you can build it up
    # using data from the form
    payload = {'key': my_key,
        'q': request.form['first_ingredient'] + "," + request.form['second_ingredient'],
        'sort': 'r'}
    raw_results = requests.get(endpoint, params = payload)

    # The following line converts the raw JSON raw_results into a nice Python dictionary to work with
    results = raw_results.json()

    # Useful for seeing the results, but can be deleted once you have everything working!
    print results

    return render_template('results.html', results=results)

if 'PORT' in os.environ:
    app.run(host='0.0.0.0',port=int(os.environ['PORT']))
else:
    app.run(debug=True)
