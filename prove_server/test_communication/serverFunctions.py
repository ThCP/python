'''
Created on 16/mag/2015
@author: Riccardo Cappuzzo

This method contains all the functions which must be executed by the server.

'''

from flask import request
import json
from rest import send

data = {
        'k1' : 'value1',
        'k2' : 'value2'
        }

def encode_data(data):
    j_data = json.dumps(data, separators=(',',':'))
    print "j_data = %r " % j_data
    return j_data

def decode_data(j_data):
    d = json.loads(j_data)
    print "d = %r " % d
    return d

def send_request(j_data):
    send(method = 'POST', url = 'http://10.15.2.89/post:8000', data = j_data)

if __name__ == '__main__':
    j_data = encode_data(data)
    d = decode_data(j_data)
    
    while (True):
        go = raw_input("Send? ")
        send_request(j_data)
        