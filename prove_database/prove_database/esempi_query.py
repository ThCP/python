'''
Created on 18/mag/2015

@author: Riccardo Cappuzzo

'''

import sqlite3

# create a connection which represents the database
conn = sqlite3.connect("test.db")

# once I have created a connection I create a cursor which allows me to perform SQL commands
c = conn.cursor()

# I then proceed to execute SQL commands
def create_database():
    c.execute (
               '''
               CREATE TABLE 
               '''               
               )

#data = {}

# when creating entries from a collection I need to use placeholders
def insert_single_row ():
    data = [('field1', 'field2', 'field3'),] 
    print data
    c.execute(
              '''
            SELECT *
              '''
    
              )

def retrieve_single_row ():
    c.execute (
               '''
               SELECT *
               '''
               
               )
    #fetch one row of the result
    c.fetchone()
    #fetch all the rows
    c.fetchall()


# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
#conn.commit()

c.execute('SELECT * FROM stocks')
for i in c.fetchall():
    print i

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
