'''
Created on 23/giu/2015

@author: Riccardo Cappuzzo
'''

import sqlite3

def fetch_all_events():
    sql = 'SELECT * FROM events'
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    result = c.fetchall()
    c.close()
    return result