'''
Created on 04/mag/2015

@author: Luke

This method contains the functions needed by the server which manages
the sensor network to respond to requests issued by the stations.

'''

'''
Initialize all the stations present in a file:
STATION_CODE | STATION_ADDRESS | STATION_POSITION | etc.
'''

from flask import Flask, request
from flask.templating import render_template
from flask.helpers import make_response
import json
import rest

# GLOBAL VARIABLES
app = Flask ('server_app')
server_addr = "http://10.15.2.129:5000" # debug, ip addr of the machine which is running the server

@app.route('/') # debug, check if the server is reachable 
def index():
    return render_template('index.html')

@app.route('/newstation', methods = ['POST'])
def new_station ():
    # TODO: check if the station is already present in the db
    new_station = {}
    data = request.get_json() # this is the dict created from the json request sent by the station
    new_station ['station_id'] = data ['station_id']
    new_station ['lat'] = data ['lat']
    new_station ['lon'] = data ['lon']
    new_station ['ip'] = request.host_url # gets the address of the station from the request
    
    # put the new station in the database
    
    # create the response
    response = { 
                'msg' : 'init_complete',
                #'state' : True
                }
     
    r = make_response(json.dumps(response, separators=(',',':')))  
    
    return r # send the response to the station


'''
Get data from the stations
'''
@app.route ('/stations/<station_id>', methods = ['POST'])
def get_data(station_id):
   
    data = request.get_json()  # this is the dict created from the json request sent by the station
    
    # elaborate the data
    elaborate_data(data)
    # store data in db
    save_data()
    '''
    check state in db: if the state is "STOP" then the response will stop the while loop
    otherwise, the while proceeds normally
    '''
    state = check_state() # state is a dictionary which contains the state and a message
    print 'state = %r ' % state['state']
    # generate standard response
    
    r = make_response(json.dumps(state, separators = (',',':')))
    
    return r # return standard response

'''
Save data in the database
'''
def save_data():
    pass

'''
Elaborate the data
'''

def elaborate_data(data):
    pass


'''
Return the station state in the database as a dictionary which contains the state
and (in case) the error message
'''
def check_state():
    
    if (True): # check in the db if the station has to stop
        # the station must stop, msg is given by the code in the db
        # "True" for debugging purposes
        state = {
                 'state' : 0,
                 'msg' : 'placeholder' # when the db will be implemented, there will be a list of messages
                 }
    else:
        state = {
                 'state' : 1
                 }
    return state
    

'''
Main: init_stations -> get_data() -> save_data -
                    ^--------------------------|
'''
if __name__ == '__main__':
    app.run ('0.0.0.0', port = 5000, debug = True)
