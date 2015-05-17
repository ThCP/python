'''
Created on 15/mag/2015
@author: Riccardo

This module simulates HTTP requests to the server, printing the outcome on stdout.

'''
import requests
from flask.json import jsonify
from flask.app import Flask
from rest import send

address_server = 'http://10.15.3.155:5000'
address_station = ''

page = '/post'

d = { 
        'k1' : 'this is the value',
        'k2' : 'value2'
    }
print d

data = d

def send__GET_request (address_server, page):
    r = requests.get(address_server + page)
    #send ('GET', address_server + page)
    
    return r
    
def send_POST_request (address_server, page, data):
    r = requests.post(address_server + page, data)
    res = send ('POST', address_server + page, data);
    
    return r
    
if __name__ == '__main__':
    
    r = send__GET_request(address_server, page)
    
    print r.text
    
    