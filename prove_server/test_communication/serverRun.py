'''
Created on 16/mag/2015

@author: Riccardo
'''

from flask import Flask, request
from flask.templating import render_template

app = Flask ('test_communication')

@app.route ('/')
def index():
    return render_template('indexServer.html')


if __name__ == '__main__':
    app.run('10.15.3.106', port = 5000)