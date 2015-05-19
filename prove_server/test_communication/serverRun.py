'''
Created on 16/mag/2015
@author: Riccardo

This method contains the function needed to run the server, together with the routes for the website (possibly).
'''

from flask import Flask, request
from flask.templating import render_template
from flask.helpers import make_response
from serverFunctions import encode_data

app = Flask ('test_communication')

@app.route ('/')
def index():
    return render_template('indexServer.html')

@app.route('/newstation', methods = ['POST'])
def newstation():
    #data = request.get_json()
    #data = request.data()
    print request.json
    #data = Request.get_json()
    response = {'questa e\' la ':'risposta'}
    res = make_response(encode_data(response))

    return res
    #return render_template('response.html', data_page = data)
    #d = Request.form['k1']
    #j_data = Request.get_json()
    #d = decode_data(j_data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug = True)