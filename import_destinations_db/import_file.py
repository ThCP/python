'''
Created on 25/mag/2015

@author: Riccardo
'''

import sys
import database
from destinations.maintenance import insert_new_destination

path1 = "C:\\Users\\Riccardo\\Programmazione\\workspace\\import_destinations_db\\DATA_TO_CEN03_XPTE_XP01.csv"
path = 'C:\\Users\\Riccardo\\Programmazione\\workspace\\import_destinations_db\\data2.csv'
example = 'TO_CEN03,XP01,A001,,,,"32,52",,"24,1",VERT,SCALA,,ATU.,AMM'
example2 = 'TO_CEN03,XP01,A002,"45,0628790000000000","7,6609320000000100",Locale Test Impianti Speciali,"23,28",330,"19,5",UFF,UFF_TEC_AM,,ARE.,EDILOG'
def read_file(path):
    csv = open(path)
    
    for line in csv:
        data = convert (line)
        insert_new_destination(data)
    '''
    '''
def convert (line):
    data = {}
    line = line.rstrip()
    
    line_split = line.split(':')
    print line_split
    data['bl_id'] = line_split[0] # building id
    data['fl_id'] = line_split[1] # floor id
    data['rm_id'] = line_split[2] # room id
    data['lat'] = line_split[3] # latitude
    data['lon'] = line_split[4] # longitude
    data['name'] = line_split[5] # name 
    data['rm_cat'] = line_split[9] # room category
    data['rm_type'] = line_split[10] # room type
    data['dv_id'] = line_split[12] # structure type
    data['dp_id'] = line_split[13] # structure
    
#     c = 0
#     for i in line_split:
#         print i + '\t........................................\t%d' % c
#         c+=1
#     
#     for i in data:
#         print i + ' ' + data[i]
#     
    return data

if __name__ == '__main__':
    read_file(path)