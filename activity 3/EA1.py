from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def hello():
    return """
    <html><body><h1>Hello</h1><form action ="/greet">What is your Name? <input type='text' name='user'><br>
    What is your best characteristic? <input type='text' name='character'><br>
    <input type='submit' value='continue'></form></body></html>"""

@app.route('/greet')
def greet():
    username = request.args.get('user', 'World')
    character = request.args['character']

    if username == '':

        msg = 'I dont know who you are!, please tell me about your self ":>"'
    else:
        msg = 'my name is also ' + username + ' and I also ' + character + '.'

    return """
    <html> <body>
   <h2>hello, {0}!</h2>
   <p>{1}</p>
   </body>
   </html>""".format(username, msg)


app.run(host=("localhost"), debug=True)