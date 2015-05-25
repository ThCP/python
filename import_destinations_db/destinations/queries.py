'''
Created on 25/mag/2015

@author: Riccardo Cappuzzo

This file contains all the queries.

'''

import sqlite3

def fetch_destination_data (station_id):
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

def fetch_all_destinations():
    sql = 'SELECT * FROM stations'
    conn = sqlite3.connect("stations.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    result = c.fetchall()
    c.close()
    return result
