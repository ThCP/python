'''
Created on 15/mag/2015
@author: Riccardo

This module simulates HTTP requests to the server, printing the outcome on stdout.

'''
import requests
from flask.json import jsonify
from flask.app import Flask

app = Flask('test')

d = { 
        'k1' : 'this is the value',
        'k2' : 'value2'
        }
print d

data = d

if __name__ == '__main__':
    
#    rest.send('POST', "http://localhost:80/post", data)
  #  r = requests.post ('http://localhost:8088', data)
 #   print "################################################"
  #  print r.text
    r2  = requests.post ('http://localhost:8088/post', data)
    print r2.text
    