'''
Created on 25/mag/2015

@author: Riccardo Cappuzzo

This file contains the functions needed to act on the stations database

'''

import sqlite3, time

################## SEARCH ENTRIES ##################    
def fetch_station_data (station_id):
    sql = 'SELECT * FROM stations WHERE SID = ?;'

    conn = sqlite3.connect("..\web_app\stations.db")
    c = conn.cursor()
    c.execute( sql, (station_id,) )
    result = c.fetchone()
    c.close()
    
    return result
    
def fetch_all_stations():
    sql = 'SELECT * FROM stations'
    conn = sqlite3.connect("..\web_app\stations.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    result = c.fetchall()
    c.close()
    
    return result

def fetch_all_stations_sorted_by_ranking():
    sql = 'SELECT * FROM stations ORDER BY ranking DESC'
    conn = sqlite3.connect("..\web_app\stations.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    result = c.fetchall()
    c.close()
    
    return result

################## CREATE ENTRIES ##################    
def insert_new_station (station_data): # insert a new station in the database
    
    sid = station_data['station_id']
    lat = station_data['lat']
    lon = station_data['lon']
    light = 0
    humidity = 0
    temperature = 0
    noise = 0
    people = 0
    ranking = 0
    
    sql = '''INSERT INTO stations (
                                SID, 
                                LAT, 
                                LON, 
                                LIGHTING,
                                HUMIDITY,
                                TEMPERATURE,
                                NOISE,
                                PEOPLE,
                                RANKING) VALUES 
                                (?,?,?,?,?,?,?,?,?);'''
    
        
    conn = sqlite3.connect("..\web_app\stations.db")
    c = conn.cursor()
    c.execute ( sql, (sid, lat, lon, light, humidity, temperature, noise, people,ranking) )
    conn.commit()
    
    c.close()
    
    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Added station ' + ' ' + sid + "\n")
    log.close()


# DELETE ENTRIES
def delete_station(station_ID): # given a sid, change the info contained in the db

    sql = '''DELETE FROM stations
                WHERE SID = ?;
    '''   
        
    conn = sqlite3.connect("..\web_app\stations.db")
    c = conn.cursor()
    c.execute ( sql, (station_ID, ) )
    conn.commit()
    
    c.close()

    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Deleted station ' + ' ' + station_ID + "\n")
    log.close()


################## UPDATE ENTRIES ##################
def update_station_data (station_data, station_ID): 
    # given a sid, change the info contained in the db
    # data changed includes latitude and longitude

    sid = station_data['station_id']
    lat = station_data['lat']
    lon = station_data['lon']
       
    sql = '''UPDATE stations 
            SET SID = ?, 
                LAT = ?, 
                LON = ?,
                LIGHTING = ?,
                HUMIDITY = ?,
                TEMPERATURE = ?,
                NOISE = ?,
                PEOPLE = ?,
                RANKING = ?
                WHERE SID = ?;
    '''   
        
    conn = sqlite3.connect("..\web_app\stations.db")
    c = conn.cursor()
    c.execute ( sql, (sid, lat, lon, 0, 0, 0, 0, 0, 0, station_ID) )
    conn.commit()
    
    c.close()


# REFRESH SENSOR DATA
def refresh_station_data (station_data, station_ID): 
    # given a sid, change the sensor info contained in the db
    
    light = station_data['light']
    humidity = station_data['humidity']
    temperature = station_data['temperature']
    noise = station_data['noise']
    people = station_data['people']
    ranking = station_data['ranking']
    
    sql = '''UPDATE stations 
            SET LIGHTING = ?,
                HUMIDITY = ?,
                TEMPERATURE = ?,
                NOISE = ?,
                PEOPLE = ?,
                RANKING = ?
                WHERE SID = ?;
    '''   
        
    conn = sqlite3.connect("..\web_app\stations.db")
    c = conn.cursor()
    c.execute ( sql, (light, humidity, temperature, noise, people, ranking, station_ID) )
    conn.commit()
    
    c.close()

if __name__ == '__main__': # the main is present for debugging purposes
    
    #print fetch_station_data('00000001')
    #print json.dumps(fetch_station_data('00000001'), sort_keys=True, indent=4, separators=(',',':'))
    #print fetch_all_stations()
    delete_station('LADISPE')
    delete_station('New_Demo_Station')
    print fetch_all_stations()
    