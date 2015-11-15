    # -*- coding: utf-8 -*-


'''
Created on 01/giu/2015

@author: Riccardo Cappuzzo
'''

import sqlite3

db_name = 'MarcoPoli.db'

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
                rm_type
            )
            VALUES
            (?,?,?,?,?,?,?);
        '''

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute ( sql,
                (data['rm_id'], 
                data['bl_id'],
                data['fl_id'],
                data['lat'],
                data['lon'],
                data['name'],
                data['rm_type'],
                ) 
               )
    conn.commit()
    
    c.close()

################## UPDATE ENTRIES ##################
def update_destination_data (destination_data, destination_ID):
    
    sql = '''
            UPDATE destinations SET 
                lat = ?,
                lon = ?,
                name = ?,
                rm_type = ?
            WHERE rm_id = ? 
            AND bl_id = ?
            AND fl_id = ?
            ;
        '''
    
        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute ( sql,
                (destination_data['lat'],
                destination_data['lon'],
                destination_data['name'],
                destination_data['rm_type'],
                destination_ID['rm_id'], 
                destination_ID['bl_id'],
                destination_ID['fl_id'],
                ) 
               )
    conn.commit()
    c.close()

def assign_destination_to_station (destination_ID, station_ID):
    
    sql = '''
            UPDATE destinations SET
                station_id = ?
            WHERE rm_id = ?
            AND bl_id = ?
            AND fl_id = =
            ;
        '''
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute ( sql,
                (station_ID,
                destination_ID['rm_id'], 
                destination_ID['bl_id'],
                destination_ID['fl_id'],
                ) 
               )
    conn.commit()
    c.close()
    
################## REMOVE ENTRY ##################
def delete_destination_data (destination_ID):
   
    sql = '''
            DELETE FROM destinations
            WHERE rm_id = ? 
            AND bl_id = ?
            AND fl_id = ?
            ;
        '''

        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute ( sql, (destination_ID['rm_id'],destination_ID['bl_id'],destination_ID['fl_id']) )
    conn.commit()
    c.close()


