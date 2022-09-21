from flask import Flask, request
from datetime import datetime, timedelta

date = datetime.now()
datetmrw = timedelta(days=1)
app = Flask(__name__)

@app.route('/')
def hello():

    return """<html><body><h1>Hello world ,Flask! </h1>the Date today is {0}.<br> the Date yesterday is {1} and <br>the Date tommorow is {2}</body></html>""".format(date, date-datetmrw, date+datetmrw)

#lunch the Flask dev server
app.run(host=("localhost"), debug=True)


