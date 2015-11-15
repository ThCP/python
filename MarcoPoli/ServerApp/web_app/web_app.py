'''
Created on 04/mag/2015

@author: Riccardo Cappuzzo
'''
from flask import Flask, request
from flask.helpers import make_response
from flask.templating import render_template
import json
from server_app.station_db_functions import fetch_all_stations_sorted_by_ranking
from destinations_db_queries import fetch_destination_by_type
from event_db_queries import fetch_all_events
from event_db_functions import delete_event_data_by_end_date
from destinations_db_queries import fetch_destination_by_id

app = Flask(__name__, static_url_path='')

'''
Main page: map + buttons
'''
@app.route('/')
def index():# renders the index page    
    return render_template('index.html')
    
@app.route('/refresh/stations', methods=['GET'])
def refresh_stations(): # used to fetch the new data from stations (get request) or to fetch a filtered list of destinations (post containing the filter)    
    response = fetch_all_stations_sorted_by_ranking()

    r = make_response(json.dumps(response, separators=(',',':')))
    return r

@app.route('/refresh/destinations', methods=['POST'])
def refresh_destinations():
        
    ss = str(request.form.keys()) # takes the content of the form (multidict) and casts it to a string
    ss = ss.lstrip('[\'') # removes the unneeded characters at the beginning and at the end of the string
    ss = ss.rstrip('\']')
    queries = json.loads(ss) # creates the dict reading the json message
    chosen_destinations = generate_result (queries)
    r = make_response(json.dumps(chosen_destinations, separators=(',',':') ))
    return r

@app.route('/refresh/events', methods=['GET'])
def refresh_events():
    delete_expired_events()
    all_events = fetch_all_events()
    
    response = []
    for i in all_events:
        r = []
        r.extend(i)
        fetch = {}
        fetch['rm_id'] = str(i[3])
        fetch['fl_id'] = str(i[2])
        fetch['bl_id'] = str(i[1])
        dest = fetch_destination_by_id(fetch)
        r.append(dest[3])
        r.append(dest[4])
        r.append(dest[5])
        t = tuple(r)
        response.append(t)
    
    r = make_response(json.dumps(response, separators=(',',':')))
    return r

def delete_expired_events():
    delete_event_data_by_end_date()
    
def generate_result (queries):
    fl = queries['Floor']
    floor = int(fl)
    # translate the floor into the code used in the database
    if floor == 0:
        fl_id = 'XPTE'
    elif floor == 1:
        fl_id = 'XP01'
    elif floor == 2:
        fl_id = 'XP02'
    elif floor == 3:
        fl_id = 'XP03'
    else:
        fl_id = ''
    
    res = []
    
    # add destinations as needed
    if (queries['Laboratory']):
        res.extend(fetch_destination_by_type('laboratorio', fl_id))
    if (queries['Room']):
        res.extend(fetch_destination_by_type('aula', fl_id))
    if (queries['Bar']):
        res.extend(fetch_destination_by_type('bar', fl_id))
    if (queries['Library']):
        res.extend(fetch_destination_by_type('biblioteca', fl_id))
        
    return res

if __name__ == '__main__':
    app.run ('0.0.0.0', port = 5000, debug = True)
    