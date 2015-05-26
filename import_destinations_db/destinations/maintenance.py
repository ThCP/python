'''
Created on 25/mag/2015

@author: Riccardo Cappuzzo

This file contains all the update/insert/delete commands for the destination database

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

    conn = sqlite3.connect("destinations.db")
    c = conn.cursor()
    c.execute ( sql,
                (data['rm_id'], 
                data['bl_id'],
                data['fl_id'],
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
def update_destination_data (destination_data, destination_ID):
   
    sql = '''
            UPDATE destinations SET 
                rm_id = ?, 
                bl_id = ?,
                fl_id = ?,
                lat = ?,
                lon = ?,
                name = ?,
                rm_cat = ?,
                rm_type = ?,
                dv_id = ?,
                dp_id = ?
            WHERE rm_id = ?
            ;
        '''

        
    conn = sqlite3.connect("destination.db")
    c = conn.cursor()
    c.execute ( sql,
                (destination_data['bl_id'], 
                destination_data['fl_id'],
                destination_data['rm_id'],
                destination_data['lat'],
                destination_data['lon'],
                destination_data['name'],
                destination_data['rm_cat'],
                destination_data['rm_type'],
                destination_data['dv_id'],
                destination_data['dp_id'],
                destination_ID
                ) 
               )
    conn.commit()
    c.close()
    
################## REMOVE ENTRY ##################
def delete_destination_data (destination_ID):
   
    sql = '''
            DELETE FROM destinations
            WHERE rm_id = ?
            ;
        '''

        
    conn = sqlite3.connect("destination.db")
    c = conn.cursor()
    c.execute ( sql, (destination_ID,) )
    conn.commit()
    c.close()
    