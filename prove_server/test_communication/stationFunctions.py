'''
Created on 16/mag/2015
@author: Riccardo

This method contains all the functions which must be executed by the station.

'''

import json
from rest import send

data = {
        'running' : 'false',
        'id' : '0001',
        'ip' : 'ip',
        'lat' : '00000',
        'long' : '00000'
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
    send(method = 'POST', url = '10.15.2.89:8000', data = j_data)

if __name__ == '__main__':
    pass