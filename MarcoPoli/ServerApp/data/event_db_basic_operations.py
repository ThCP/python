'''
Created on 18/giu/2015

@author: Riccardo Cappuzzo
'''


import sqlite3,time

def create_event_table():

    sql = """
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

    
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    
    c.close()

    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Created events table \n' )
    log.close()


def delete_event_table():
    """Deletes the events table"""
    sql = 'DROP TABLE events;'
    
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    
    c.close()
    
    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Deleted events table' + "\n")
    log.close()
    
if __name__ == '__main__':
    create_event_table()
    #delete_event_table()