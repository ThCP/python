'''
Created on 04/mag/2015

@author: Luca Mezzatesta

COMMUNICATION PROCESS
'''

import rest
import time
import json
from flask import Flask, request, jsonify
from flask.helpers import make_response
from flask.templating import render_template
import os


'''
Global variables
'''
app = Flask(__name__)

DEBUG = True
state = 0   # 0 = startup session
            # 1 = send data to the server
lat = None
lon = None
station_id = None
server_addr = 'http://10.15.3.164:5000' # for debug purposes, this is the ip of the pc which runs the server
station_addr = 'http://10.15.3.164:8000'
    
'''
Send data to the server and receive from the server 
commands.
THIS SHOULD BE IMPLEMENTED ON THE "DATA THREAD"
'''

##DELETE
##def exchange_data(): 
##    send_addr = server_addr+"/stations/"+station_id 
##    # example result: http://10.15.2.132:5000/stations/00000001
##    
##    debug_data = {
##                  'data' : 'placeholder'
##                  }
##    
##    res = rest.send("POST", send_addr, json.dumps(debug_data, separators=(',',':')), {'Content-Type':'application/json'} )
##    
##    # commented below for debugging
##    #res = rest.send("POST", send_addr, jsonify(fetch_data), {'Content-Type':'application/json'} )
##    return res # this response contains the commands issued by the server

'''
Starting the station
'''
@app.route('/start', methods=["POST"])
def start():
    data = request.get_json()
    state = data['state']       # state value from json file should be always True if this method is used by the server
    msg = data['msg']           # message from the server (used for troubleshooting)

    # Writing on pipe-file (kind of)
    f = open("pipe.txt", "w")
    f.write(state)
    f.close
    
    # Writing on log.txt file
    f = open("log.txt", "a")
    f.write(time.strftime("%c") + " - " + msg +'\n')
    f.close

    msg = 'Station '+station_id+': Start'
    return jsonify({'msg':msg})

'''
Stopping the station
'''
@app.route('/stop', methods=["POST"])
def stop():
    data = request.get_json()
    state = data['state']
    msg = data['msg']

    # Writing on log.txt file
    f = open("log.txt", "a")
    f.write(time.strftime("%c") + " - " + msg +'\n')
    f.close

    # Writing on pipe-file (kind of)
    f = open("pipe.txt", "w")
    f.write(state)
    f.close
    
    msg = 'Station '+station_id+': Stop'
    return jsonify({'msg':msg})

    
## DELETE!
##    while(state):
##        res = exchange_data() # the response is a dictionary which contains the state and a msg from the server
##        print 'res = %r ' % res
##        state = res['state'] # this may become false depending on the response from the server
##        
##        if ( state == False): # the loop has been stopped, res['msg'] contains the reason
##            f = open("log.txt", "a") # write on the log file
##            f.write(time.strftime("%c") + " - " + res['msg'] +'\n')
##            f.close
##        else:
##            time.sleep(SLEEP)
##        
##    response = {
##                'msg' : 'station %s has stopped' % station_id
##                }
##    
##    f = open("log.txt", "a") # write on the log file
##    f.write(time.strftime("%c") + " - " + response['msg'] +'\n')
##    f.close
##    return make_response(json.dumps(response, separators = (',',':')))

## DELETE! 
##@app.route('/')
##def index ():
##    return render_template('index_station.html', id = station_id)

'''
Getting the current state
'''
def get_state():
    return state;

'''
Main
'''
if __name__ == '__main__':
    os.system("python station_data.py &")
    app.run(host='0.0.0.0', port=8000, debug=True)
