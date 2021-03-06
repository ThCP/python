'''
Created on 25/mag/2015

@author: Riccardo Cappuzzo

This file contains all the queries.

'''

import sqlite3

def fetch_destination_by_id (destination_id): # destination_id is a dictionary which contains the 3 values of the primary key, bl_id, fl_id, rm_id
    sql = 'SELECT * FROM destinations WHERE bl_id = ? AND fl_id = ? AND rm_id = ?;'

    conn = sqlite3.connect("destinations.db")
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
    conn = sqlite3.connect("destinations.db")
    c = conn.cursor()
    c.execute(
              sql
              )
    result = c.fetchall()
    c.close()
    return result


if __name__ == '__main__':
    r = fetch_destination_by_id('A001')
    print r
    