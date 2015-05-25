'''
Created on 25/mag/2015

@author: Riccardo Cappuzzo

This file contains all the update/insert/delete commands

'''

import sqlite3

################# CREATE ENTRIES ####################
def insert_new_destination (data):
    
        
    sql = '''
            INSERT INTO destinations 
            (
                rm_id, 
                bl_id,
                fl_id,
                lat,
                lon,
                name,
                rm_cat,
                rm_type,
                dv_id,
                dp_id
            )
            VALUES
            (?,?,?,?,?,?,?,?,?,?);
        '''

    conn = sqlite3.connect("stations.db")
    c = conn.cursor()
    c.execute ( sql,
                (data['bl_id'], 
                data['fl_id'],
                data['rm_id'],
                data['lat'],
                data['lon'],
                data['name'],
                data['rm_cat'],
                data['rm_type'],
                data['dv_id'],
                data['dp_id']
                ) 
               )
    conn.commit()
    
    c.close()

################## UPDATE ENTRIES ##################
def update_destination_data (station_data, station_ID):

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