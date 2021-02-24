import random

from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world!"

@app.route('/template')
def template():
    return render_template('home.html')

@app.route('/test')
def test():
    workers_list = ["http://www.is.fi", "http://www.hs.fi", "http://yle.fi"]

    rr = random.randint(0,len(workers_list)-1)
    return redirect (workers_list[rr])

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')