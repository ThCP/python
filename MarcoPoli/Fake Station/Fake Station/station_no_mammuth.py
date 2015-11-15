'''
Created on 21/mag/2015

@author: Luca Mezzatesta

STATION
'''

import rest
import json
from sensors_2 import fetch_data
import time
from time import sleep

# GLOBAL VARIABLES
lat = None
lon = None
station_id = None
server_addr = 'http://10.15.3.164:5000'
station_addr = 'http://10.15.3.164:8000'

'''
Main
'''
if __name__ == '__main__':

    # Opening/closing info.txt file
    f = open("info.txt", "r")
    raw_info = f.read()
    f.close()
    
    # Fetching data from raw_info
    info = raw_info.split();
    
    # Basic information about the station
    lat = info[0]
    lon = info[1]
    station_id = info[2]
    server_addr = info[3]

    # getting data from the sensors
    data = fetch_data()
    
    # sending data to the server
    res = rest.send('POST', server_addr + '/stations/'+station_id, json.dumps(data, separators=(',',':')), {'Content-Type': 'application/json'})