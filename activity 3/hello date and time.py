from flask import Flask
from datetime import datetime

date = datetime.now()
app = Flask(__name__)

@app.route("/")

def hello():
    return """<html><body><h1>Hello world ,Flask! </h1>the time is{0}.</body></html>""".format(date)


#lunch the Flask dev server
app.run(host=("localhost"), debug=True)


