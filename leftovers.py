
from flask import Flask
from flask import render_template
from flask import request


app = Flask("MyApp")



@app.route("/welcome")
def welcome():
    return render_template("leftover.html")



import requests

endpoint = 'http://food2fork.com/api/search'
payload = { 'key': 'a36d8f597d70a074e4866e5c25ff8a6c', 'q':
'first ingredient, second ingredient', 'sort': 'r'}

endpoint1 = 'http://food2fork.com/api/get'
payload2 = { 'key': 'a36d8f597d70a074e4866e5c25ff8a6c', 'rId': ''}

response = requests.get(endpoint, params = payload)




@app.route("/search", methods=['POST'])
def index():
    results = requests.get(endpoint, params = payload)
    return render_template('results.html', results=results)





app.run(debug=True)
