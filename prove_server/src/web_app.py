'''
Created on 13/mag/2015

@author: Riccardo
'''
from flask import Flask
from flask.templating import render_template

app = Flask("Application")

'''website part'''
@app.route('/')
def index():
    return render_template('indexServer.html')
'''end website part'''

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)
