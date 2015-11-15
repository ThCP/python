'''
Created on 25/mag/2015

@author: Riccardo Cappuzzo

'''

from flask import Flask, request
from flask.templating import render_template
from flask.helpers import make_response
import json
from server_app.station_db_functions import insert_new_station,\
    refresh_station_data
import time
from server_app import ranking

# GLOBAL VARIABLES
app = Flask ('server_app')

# DEBUG VARIABLES
server_addr = "http://10.15.3.148:5000" # debug, ip addr of the machine which is running the server
text_server = 'init_message'
create_command = True # this command must be changed in order to change the type of response to new_station
get_command = True # same as above
restart_command = True # same as above


# Log entry created when the server starts.
def init ():
    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Server init completed.' + "\n")
    log.close()

# Used to check whether the server is reachable. 
@app.route('/') 
def index():
    return render_template('index.html')

# Page to which the stations send the init request. 
@app.route('/newstation', methods = ['POST'])
def new_station ():
    
    data = request.get_json() # this is the dict created from the json request sent by the station
    station = {}
    station ['station_id'] = data ['station_id']
    station ['lat'] = data ['lat']
    station ['lon'] = data ['lon']
    
    # put the new station in the database
    insert_new_station(station)
    
    # create the response
    if (create_command): # allows to choose between the two possible results
        response = {
                    'state' : True,
                    'msg' : text_server
                    } 
    else:
        response = {
                    'state' : False,
                    'msg' : text_server,
                    'sleep' : 0 # the station sends a new request after 'sleep' seconds
                    } 

    r = make_response(json.dumps(response, separators=(',',':')))  
    
    return r # send the response to the station

# Stations send their data to the following page. The json is then recorded in the station db.
@app.route ('/stations/<station_id>', methods = ['POST'])
def get_data(station_id):

    data = request.get_json() # this is the dict created from the json request sent by the station    station_data = {} # empty dictionary 
    station_data ['temperature'] = data ['temperature']
    station_data ['humidity'] = data ['humidity']
    station_data ['light'] = data ['light']
    station_data ['noise'] = data ['noise'] # scale from 0 to 10
    station_data ['people']  = data ['people'] # congestion from 0 to 10
    station_data ['ranking'] = ranking.rank_station(station_data)
    
    
    station_data ['station_id'] = station_id
    
    print station_data
    
    save_data(station_data) # pass station data to elaboration/db
   
    # create the response
    if (get_command):
        response = { 
                    'state' : True, # continue sending data
                    'msg' : text_server,
                   }
    else: 
        response = {
                    'state' : False, # stop sending data
                    
                    'sleep' : 0, # station will send a restart request after 'sleep' seconds
                    
                    'msg' : text_server
                    
                    }   
         
    r = make_response(json.dumps(response, separators=(',',':')))  
    
    return r # send the response to the station

   
'''
Save data in the database
'''
def save_data(station_data):
    refresh_station_data(station_data, station_data['station_id'])

'''
Restart the station
'''
@app.route ('/stations/<station_id>/restart', methods = ['GET'])
def restart_station(station_id):
    # create the response
    if (restart_command):
        response = { 
                    'state' : True, # restart sending data
                    'msg' : text_server,
                    }
    else:
        response = {
                    'state' : False, # do not send data yets
                    'msg' : text_server,
                    'sleep' : 0 # station will send a request in 'sleep' seconds
                    }
         
    r = make_response(json.dumps(response, separators=(',',':')))  
    
    return r # send the response to the station

'''
Main: init_stations -> get_data() -> save_data -
                    ^--------------------------|
'''
if __name__ == '__main__':
    init()    
    app.run ('0.0.0.0', port = 8000, debug = True)
