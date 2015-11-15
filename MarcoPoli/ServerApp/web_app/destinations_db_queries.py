'''
Created on 25/mag/2015

@author: Riccardo Cappuzzo

This file contains all the queries.

'''

import sqlite3

db_name = 'MarcoPoli.db'

def fetch_destination_by_id (destination_id): # destination_id is a dictionary which contains the 3 values of the primary key, bl_id, fl_id, rm_id
    sql = 'SELECT * FROM MarcoPoli WHERE bl_id = ? AND fl_id = ? AND rm_id = ?;'

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(
              sql,
              (destination_id['bl_id'], destination_id['fl_id'], destination_id['rm_id'])
              )
    result = c.fetchone()
    c.close()
    return result

def fetch_all_destinations():
    sql = 'SELECT * FROM destinations'
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(
              sql
              )
    result = c.fetchall()
    c.close()
    return result

def fetch_destination_by_type (destination_type, fl_id):
    
    print destination_type
    
    if (destination_type.__eq__('aula')):
        sql = 'SELECT * FROM destinations WHERE rm_type = \'AULA\''
    elif (destination_type.__eq__('laboratorio')):
        sql = 'SELECT * FROM destinations WHERE rm_type = \'LAB_DIDAT\''
    elif (destination_type.__eq__('bar')):
        sql = 'SELECT * FROM destinations WHERE rm_type = \'BAR\''
    elif (destination_type.__eq__('libreria')):
        sql = 'SELECT * FROM destinations WHERE rm_type = \'LIBRERIA\''
    elif (destination_type.__eq__('biblioteca')):
        sql = 'SELECT * FROM destinations WHERE rm_type = \'BIBLIO\''
    else:
        sql = 'SELECT * FROM destinations'
        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    if (fl_id.__eq__('')):
        sql = sql + ';'
        c.execute(
                  sql
                  )
        
    else:
        sql = sql + ' AND fl_id = ?;'
        c.execute(
                  sql,
                  (fl_id,)
                  )
    result = c.fetchall()
    c.close()
    print result
    return result
 
if __name__ == '__main__':
    res = []
    res = fetch_all_destinations()
    
    for i in res:
        print i