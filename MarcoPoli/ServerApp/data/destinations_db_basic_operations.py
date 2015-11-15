'''
Created on 01/giu/2015

@author: Riccardo Cappuzzo


This file contains the create_destinations_table() and the delete_destinations_table() functions


'''

import sqlite3,time

def create_destination_table():

    sql = """
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

    
    conn = sqlite3.connect("destinations.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    
    c.close()

    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Created destinations table \n' )
    log.close()


def delete_destination_table():
    """Deletes the destinations table"""
    sql = 'DROP TABLE destinations;'
    
    conn = sqlite3.connect("destinations.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    
    c.close()
    
    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Deleted destinations table' + "\n")
    log.close()
    
if __name__ == '__main__':
    create_destination_table()
    #delete_destination_table()