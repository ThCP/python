'''
Created on 21/mag/2015

@author: Luca Mezzatesta

STATION
'''

import rest
import json
from sensors_debug import fetch_data
import time
from time import sleep

# GLOBAL VARIABLES
lat = None
lon = None
station_id = None
server_addr = 'http://10.15.3.164:5000'
station_addr = 'http://10.15.3.164:8000'

'''
Send own data to the server
'''
def init(lat,lon,station_id,server_addr):
    message = { 'station_id': station_id, 'lat': lat, 'lon':lon }
    res = rest.send( 'POST', server_addr + '/newstation', json.dumps(message, separators=(',',':')), {'Content-Type': 'application/json'} )
    state = res['state']
    if( state == False ):
        sleep_time = res['sleep']
    else:
        sleep_time = False
    
    f = open("log.txt", "a")
    f.write(time.strftime("%c") + " - " + res['msg'] + "\n")
    f.close()

    return {'state':state,'sleep':sleep_time}

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

    state = False;

    # init() the station, sendind info to the server
    res = init(lat,lon,station_id,server_addr)
    state = res['state']

    if( state == False ):
        sleep_time = res['sleep']
    else:
        sleep_time = 0

    while( not state ):
        # TODO: Think a smart thing to do before sending another init request
        sleep(sleep_time)
        state = init(lat,lon,station_id,server_addr)
    
    while(True):        # too much power consuption with this instruction
                        # Solution: using a semaphore
        
        while( state ):
            # getting data from the sensors
            data = fetch_data()

            # sending data to the server
            res = rest.send('POST', server_addr + '/stations/'+station_id, json.dumps(data, separators=(',',':')), {'Content-Type': 'application/json'})

            state = res['state']
            if( state == False ):
                 sleep_time = res['sleep']
            else:
                sleep_time = 0
                
            # writing on log.txt
            f = open("log.txt", "a")
            f.write(time.strftime("%c") + " - " + res['msg'] + "\n")
            f.close()
                
            old_data = data.copy()

        # TODO: Think a smart thing to do before sending another request
        sleep(sleep_time)

        res = rest.send('GET', server_addr + '/stations/' + station_id + '/restart' )
        state = res['state']
        if( state == False ):
            sleep_time = res['sleep']
        else:
            sleep_time = 0

        # writing on log.txt
        f = open("log.txt", "a")
        f.write(time.strftime("%c") + " - " + res['msg'] + "\n")
        f.close()
        
