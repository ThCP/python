'''
Created on 13/mag/2015

@author: Riccardo
'''
    
from flask import Flask
from flask.templating import render_template

app = Flask("Application")

@app.route('/')
def index():
    return render_template('indexStation.html')

@app.route('/post', methods=['POST'])
def post ():
    pass
 
if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, debug = True)
