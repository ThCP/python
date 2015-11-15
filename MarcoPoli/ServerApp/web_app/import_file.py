        # -*- coding: utf-8 -*-


'''
Created on 25/mag/2015

@author: Riccardo Cappuzzo
'''

import time
from destinations_db_functions import insert_new_destination

path = 'C:\\Users\\Riccardo\\git\\MarcoPoli\\ServerApp\\data\\d2.csv'
def read_file(path): # I read the file one time, path is the absolute path of the file I'm using as source. It shouldn't change so for out purposes it works
    csv = open(path)
    c = 0
    d = []
    for line in csv:
        data = convert (line)
        
        if (data.has_key('lat') and data.has_key('lon')): # extracts only the destinations which have a lat. and a lon. We don't care about those with no coordinates.
            if not data['name'].__eq__(''): # destinations with empty name are corridors, we can decide what should be done with these
                insert_new_destination(data)
                c+=1
                d.append(data)

    log = open('log.txt', 'a')
    log.write(time.strftime("%c") + " - " + 'Inserted destination in destinations table \n' )
    log.close()
    print 'added %d destinations' % c
    
    return d
    
def convert (line):
    data = {}
    line = line.rstrip()
    type(line)
    
    line_split = line.split(':')
    data['bl_id'] = line_split[0] # building id
    data['fl_id'] = line_split[1] # floor id
    data['rm_id'] = line_split[2] # room id
    data['lat'] = line_split[3] # latitude
    data['lon'] = line_split[4] # longitude
    data['name'] = line_split[5] # name 
    data['rm_type'] = line_split[10] # room type
    
    if ( (not (data['lat'].__eq__('') or data['lat'].__eq__('0,0000000000000000'))) and (not (data['lon'].__eq__('') or data['lon'].__eq__('0,0000000000000000'))) ):
        return data
  
    else:
        data = {}
        return data
    

if __name__ == '__main__':
    read_file(path)