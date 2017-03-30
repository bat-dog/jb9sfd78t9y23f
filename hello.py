#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<string:page_name>/')
def static_page(page_name):
    return "404"
    #return render_template('404.html')

if __name__ == "__main__":
    app.run()
