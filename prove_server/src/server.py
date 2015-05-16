'''
Created on 12/mag/2015

This file is the draft of what will be put in the ServerApp.py (and other) file. 

This file contains in particular the 


@author: Riccardo Cappuzzo
'''
from flask import Flask, jsonify, Request, request
#import management
#from management import read_station_list
#from management import print_station_list
from flask.templating import render_template
from flask.wrappers import Response
from flask.helpers import make_response

app = Flask(__name__)

# WEB APP
@app.route('/', methods = ['GET', 'POST'])
def index ():
    return render_template('indexServer.html')

@app.route('/post', methods =['GET','POST'])
def post():
  # r = request.form['k1']
    
    d = '123'
 #   print r
    return render_template('response.html', data=d)

# REST SERVER
@app.route('/stations/<int:station_id>')
def get_station ():
    #document.write(r)
    pass

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8088, debug = True)
    # read_station_list()
    # print_station_list()
    

