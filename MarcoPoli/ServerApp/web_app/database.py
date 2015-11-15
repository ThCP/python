'''
Created on 06/set/2015

@author: Riccardo
'''

import sqlite3,time

def create_database():

    sql1 = """
        CREATE TABLE destinations 
        (  
            bl_id char(8), 
            fl_id char(4),
            rm_id char(4),
            lat char(20),
            lon char(20),
            name char(64),
            rm_type char(12),
            station_id char (8) NULL,
            primary key 
            (
                bl_id,
                fl_id,
                rm_id
            )
        );
    """
    
    sql2 = """    
        CREATE TABLE events 
        (  
            event_id char(4),
            bl_id char(8), 
            fl_id char(4),
            rm_id char(4),
            name char(64),
            event_start_date char(10),
            event_start_time char(6),
            event_end_date char(10),
            event_end_time char(6),      
            primary key 
            (
                event_id
            )
        );
    
    """
    sql3 = """    
        CREATE TABLE stations 
        ( 
            SID CHAR (5) NOT NULL, 
            LAT CHAR (20), 
            LON CHAR (20), 
            LIGHTING FLOAT,
            HUMIDITY FLOAT,
            TEMPERATURE FLOAT,
            NOISE FLOAT,
            PEOPLE FLOAT,
            RANKING FLOAT,
            PRIMARY KEY (SID)
            );
        """

    
    conn = sqlite3.connect("MarcoPoli.db")
    c = conn.cursor()
    c.execute(
              sql1
              )
    c.execute(
              sql2
              )
    c.execute(
              sql3
              )
    
    
    c.close()

    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Created MarcoPoli.db \n' )
    log.close()
    
if __name__ == '__main__':
    create_database()
    #delete_destination_table()