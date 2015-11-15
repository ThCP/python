'''
Created on 25/mag/2015

@author: Riccardo Cappuzzo

This file contains the create_station_table() and the delete_station_table() functions

'''

import sqlite3,time

def create_station_table():
    """Creates the stations table."""
    sql = '''CREATE TABLE stations ( SID CHAR (5) NOT NULL, 
                                    LAT CHAR (20), 
                                    LON CHAR (20), 
                                    LIGHTING FLOAT,
                                    HUMIDITY FLOAT,
                                    TEMPERATURE FLOAT,
                                    NOISE FLOAT,
                                    PEOPLE FLOAT,
                                    RANKING FLOAT,
                                    PRIMARY KEY (SID)
                                    );'''
    
    conn = sqlite3.connect("..\web_app\stations.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    
    c.close()
    
    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Created stations table.' + "\n")
    log.close()

def delete_station_table():
    """Deletes the stations table"""
    sql = 'DROP TABLE stations;'
    
    conn = sqlite3.connect("..\web_app\stations.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    
    c.close()
    
    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Deleted stations table.' + "\n")
    log.close()
    
# the main is used only to create the db/delete it for debugging purposes
if __name__ == '__main__':
    create_station_table()
    #delete_station_table()