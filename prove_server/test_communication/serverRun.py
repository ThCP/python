'''
Created on 16/mag/2015
@author: Riccardo

This method contains the function needed to run the server, together with the routes for the website (possibly).
'''

from flask import Flask, request
from flask.templating import render_template

app = Flask ('test_communication')

@app.route ('/')
def index():
    return render_template('indexServer.html')



if __name__ == '__main__':
    app.run('10.15.3.155', port = 5000)