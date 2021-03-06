'''
Created on 25/mag/2015

@author: Riccardo Cappuzzo

This function creates the destinations database.
Call this only once, if the structure of the db is wrong, 
delete it and restart. CAREFUL WHEN DELETING

'''
import sqlite3

def create_destination_table():
    """Creates the database, call this only once."""
    sql = """
        CREATE TABLE destinations 
        (  
            bl_id char(8),
            fl_id char(4),
            rm_id char(4),
            lat char(20),
            lon char(20),
            name char(64),
            rm_cat char(4),
            rm_type char(12),
            dv_id char(4),
            dp_id char(8),
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

    print "Executed sql query: " + sql

if __name__ == '__main__':
    create_destination_table()
    