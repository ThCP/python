'''
Created on 18/mag/2015
@author: Riccardo Cappuzzo
'''
import sqlite3

station_data = {
                'station_id' : '00001',
                'station_ip' : '10.115.113.44/5000',
                'lat' : 0,
                'long' : 0
                }

####################################################
################## !! STATIONS !! ##################

################## SEARCH ENTRIES ##################
def fetch_station_data (station_id):
    sql = 'SELECT * FROM stations WHERE SID = ?;'

    conn = sqlite3.connect("stations.db")
    c = conn.cursor()
    c.execute(
              sql,
              (station_id,)
              )
    result = c.fetchone()
    c.close()
    print "station data:"
    print result

def fetch_all_stations():
    sql = 'SELECT * FROM stations'
    conn = sqlite3.connect("stations.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    result = c.fetchall()
    c.close()
    return result

################## CREATE ENTRIES ##################    
def create_station_table():
    
    sql = 'CREATE TABLE stations ( SID CHAR (5), SIP CHAR (15), LAT DECIMAL(9,6), LONG DECIMAL(9,6) );'
    
    conn = sqlite3.connect("stations.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    print "db created"

    c.close()

def insert_new_station (station_data):
    
    sid = station_data['station_id']
    sip = station_data['station_ip']
    lat = station_data['lat']
    long = station_data['long']
    
    sql = 'INSERT INTO stations (SID, SIP, LAT, LONG) VALUES (?,?,?,?)'
        
    conn = sqlite3.connect("stations.db")
    c = conn.cursor()
    c.execute ( sql, (sid, sip, lat, long) )
    conn.commit()
    print 'added station %s ' % sid
    
    c.close()

################## UPDATE ENTRIES ##################
def update_station_data (station_data, station_ID):

    sid = station_data['station_id']
    sip = station_data['station_ip']
    lat = station_data['lat']
    long = station_data['long']
       
    sql = 'UPDATE stations SET SID = ?, SIP = ?, LAT = ?, LONG = ? WHERE SID = ?;'   
        
    conn = sqlite3.connect("stations.db")
    c = conn.cursor()
    c.execute ( sql, (sid, sip, lat, long, station_ID) )
    conn.commit()
    print 'updated station %s ' % sid
    
    c.close()
    
####################################################
##################   !! USERS !!  ##################

################## SEARCH ENTRIES ##################
def fetch_user_by_ID():
    pass

def print_all_users ():
    pass

################## CREATE ENTRIES ##################    
def insert_new_user (user_data):
    pass    
    
################## UPDATE ENTRIES ##################

####################################################
################### DESTINATIONS ###################

################## SEARCH ENTRIES ##################
def fetch_destination_by_name(name):
    pass

def fetch_destination_by_ID(ID):
    pass

def fetch_destination_by_type(type): # classroom, study room, bar, laboratory
    pass
def fetch_destination_by_rankl(rank):
    pass

################## CREATE ENTRIES ##################    
def create_ranking_table():
    pass

def insert_destinations_in_ranked_table():
    pass
    
################## UPDATE ENTRIES ##################
# we need a parallel table which contains the ranking of the room, and we update that one
def update_rank_destination():
    pass
    
    
    
if __name__ == '__main__':
    # create_station_table()
    #insert_new_station(station_data)
    fetch_station_data(station_data['station_id'])
    res = fetch_all_stations()
    
    for i in res:
        sid = i[0]
        print sid