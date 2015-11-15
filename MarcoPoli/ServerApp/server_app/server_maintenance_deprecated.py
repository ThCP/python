'''
Created on 20/mag/2015
@author: Riccardo Cappuzzo


'''
from flask import request
from flask.helpers import make_response
import json
import rest
import time 

'''
Start a particular station. The address is fetched from the database or it is inserted manually.
'''
def start_station_by_IP(IP_address):
    message = {
               'state' : True,
               'msg' : 'Starting loop'
               }
    rest.send( 'POST', IP_address + '/start', json.dumps(message, separators=(',',':')), {'Content-Type': 'application/json'} )
    
    
    # PROBLEMA: SE ASPETTO LA RESPONSE DALLA STAZIONE QUESTA FUNZIONE NON TERMINA FINCHE' LA STAZIONE NON SI FERMA
    
    '''
    f = open("log.txt", "a")
    f.write(time.strftime("%c") + " - " + res['msg'] + "\n")
    f.close()
    '''
if __name__ == '__main__':
    start_station_by_IP('http://10.15.3.164:8000') 