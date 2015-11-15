'''
Created on 04/mag/2015

@author: Luke
'''
from flask import Flask, request
from flask.helpers import make_response
from flask.templating import render_template
import json
from server_app.station_db_functions import fetch_all_stations
from destinations_db_queries import fetch_destination_by_type

app = Flask(__name__, static_url_path='')

'''
Main page: map + buttons
'''
@app.route('/')
def index():# renders the index page    
    return render_template('index.html')
    
@app.route('/refresh', methods=['GET', 'POST'])
def refresh(): # used to fetch the new data from stations (get request) or to fetch a filtered list of destinations (post containing the filter)
    
    if request.method == 'GET': 
        response = fetch_all_stations()
        print response
        #response = convert_in_levels(fetch_all_stations())

        r = make_response(json.dumps(response, separators=(',',':')))
        
    elif request.method == 'POST':
        
        ss = str(request.form.keys()) # takes the content of the form (multidict) and casts it to a string
        ss = ss.lstrip('[\'') # removes the unneeded characters at the beginning and at the end of the string
        ss = ss.rstrip('\']')
        print ss
        queries = json.loads(ss) # creates the dict reading the json message
        
        chosen_destinations = generate_result (queries)
        
        for i in chosen_destinations:
            print i
        
        print json.dumps(chosen_destinations, separators=(',',':') )
        
        r = make_response(json.dumps(chosen_destinations, separators=(',',':') ))
    else:
        pass

    return r



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
    
    #print fl_id
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
def convert_in_levels (station_data): # converts the station data in levels so it's easier to show on the map the stations
    r = []
    i = []
    for g in station_data:
        i.extend(g)
        # temperature level
        if i[5] < 6.0:
            i[5] = -1 # low
        elif i[5] >= 6.0 and i[5] < 23.0:
            i[5] = 0 # normal
        else:
            i[5] = +1 #high
    
        # noise level
        if i[6] < 8.0:
            i[6] = -1 # low
        elif i[6] >= 8.0 and i[6] < 15.0:
            i[6] = 0 # normal
        else:
            i[6] = +1 #high
    
        # congestion level
        if i[7] < 30.0:
            i[7] = -1 # low
        elif i[7] >= 30.0 and i[7] < 70.0:
            i[7] = 0 # normal
        else:
            i[7] = +1 #high
        r.append(i)
    
    return r
    

if __name__ == '__main__':
    app.run(debug=True)