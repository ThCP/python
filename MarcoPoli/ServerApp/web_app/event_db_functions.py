'''
Created on 18/giu/2015

@author: Riccardo
'''
from event_db_queries import fetch_all_events


'''
Created on 01/giu/2015

@author: Riccardo Cappuzzo
'''

import sqlite3

db_name = 'events.db'

################# CREATE ENTRIES ####################
def insert_new_event (data):
     
    sql = '''
            INSERT INTO events 
            (
                event_id,
                rm_id, 
                bl_id,
                fl_id,
                name,
                event_start_date,
                event_start_time,
                event_end_date,
                event_end_time
            )
            VALUES
            (?,?,?,?,?,?,?,?,?);
        '''

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute ( sql,
                (data['event_id'],
                data['rm_id'], 
                data['bl_id'],
                data['fl_id'],
                data['name'],
                data['event_start_date'],
                data['event_start_time'],
                data['event_end_date'],
                data['event_end_time']
                
                ) 
               )
    conn.commit()
    
    c.close()

################## UPDATE ENTRIES ##################
def update_event_data (event_data, event_ID):
    
    sql = '''
            UPDATE events SET 
                name = ?,
                rm_id = ?,
                bl_id = ?,
                fl_id = ?,
                event_start_date = ?,
                event_start_time = ?,
                event_end_date = ?
                event_end_time = ?
            WHERE event_id = ?
            ;
        '''
    
        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute ( sql,(
                event_data['name'],
                event_data['rm_id'], 
                event_data['bl_id'],
                event_data['fl_id'],
                event_data['event_start_date'],
                event_data['event_start_time'],
                event_data['event_end_date'],
                event_data['event_end_time'],
                event_ID
                ) 
               )
    conn.commit()
    c.close()
    
################## REMOVE ENTRY ##################
def delete_event_data_by_end_date_and_id (event_ID, event_end_date):
    
    sql = '''
            DELETE FROM events
            WHERE event_ID =?
            AND ? < date('now')
            ;
        '''

        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute ( sql, (event_ID,event_end_date) )
    conn.commit()
    c.close()
    
def delete_event_data_by_end_date ():
    
    sql = '''
            DELETE FROM events
            WHERE event_id  IN
                ( SELECT event_id
                  FROM events
                  WHERE event_end_date = date('now')
                  AND event_end_time < time ('now', 'localtime')
                  )
            OR event_id IN (SELECT event_id
                  FROM events
                  WHERE event_end_date < date('now')
                  )
            
            ;
        '''

        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute ( sql )
    conn.commit()
    c.close()
    
def delete_event_data (event_ID):
    
    sql = '''
            DELETE FROM events
            WHERE event_ID =?
            ;
        '''

        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute ( sql, (event_ID,) )
    conn.commit()
    c.close()
    
if __name__ == '__main__':
    
#     conn = sqlite3.connect(db_name)
#     c = conn.cursor()
#     c.execute ( 'SELECT time(\'now\', \'localtime\')')
#     conn.commit()
#     r = c.fetchone()
#     c.close()
#     print r
#     
    delete_event_data('0001')
    delete_event_data('0002')
    delete_event_data('0003')
    delete_event_data('0004')
    #delete_event_data('0005')
    event_data = {
                  'event_id' : '0001',
                  'rm_id' : 'Q008',
                  'fl_id' : 'XPTE',
                  'bl_id' : 'TO_CEN03',
                  'name' : 'Test Event #1',
                  'event_start_date' : '2015-07-23',
                  'event_start_time' : '09:13',
                  'event_end_date' : '2015-08-23',
                  'event_end_time' : '10:14'
                  }
    #delete_event_data('0003')
    insert_new_event(event_data)
    event_data = {
                  'event_id' : '0002',
                  'rm_id' : 'A001',
                  'fl_id' : 'XPTE',
                  'bl_id' : 'TO_CEN03',
                  'name' : 'Test Event #2',
                  'event_start_date' : '2015-07-22',
                  'event_start_time' : '09:13',
                  'event_end_date' : '2015-07-23',
                  'event_end_time' : '10:14'
                  }
    insert_new_event(event_data)
    
    event_data = {
                  'event_id' : '0004',
                  'rm_id' : 'I005',
                  'fl_id' : 'XPTE',
                  'bl_id' : 'TO_CEN03',
                  'name' : 'Test Event #3',
                  'event_start_date' : '2015-09-23',
                  'event_start_time' : '09:13',
                  'event_end_date' : '2015-09-24',
                  'event_end_time' : '10:14'
                  }
    
    insert_new_event(event_data)
    
    event_data = {
                  'event_id' : '0003',
                  'rm_id' : 'A001',
                  'fl_id' : 'XPTE',
                  'bl_id' : 'TO_CEN03',
                  'name' : 'Test Event #4',
                  'event_start_date' : '2015-06-23',
                  'event_start_time' : '09:13',
                  'event_end_date' : '2015-06-23',
                  'event_end_time' : '23:12'
                  }
    insert_new_event(event_data)
    for i in fetch_all_events():
        print i
    
    