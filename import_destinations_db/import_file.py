'''
Created on 25/mag/2015

@author: Riccardo
'''

import sys
import database

path1 = "C:\\Users\\Riccardo\\Programmazione\\workspace\\import_destinations_db\\DATA_TO_CEN03_XPTE_XP01.csv"
path = 'C:\\Users\\Riccardo\\Programmazione\\workspace\\import_destinations_db\\data.csv'
example = 'TO_CEN03,XP01,A001,,,,"32,52",,"24,1",VERT,SCALA,,ATU.,AMM'

def read_file(path):
    csv = open(path)
    line = ''
    line = csv.readline()
    data = convert(line)
    '''
    for line in csv:
        data = convert (line)
    '''
    
def convert (line):
    data = {}
    line = line.rstrip()
    line_split = line.split(',')
    print line_split
    data['bl_id'] = line_split[0] # building id
    data['fl_id'] = line_split[1] # floor id
    data['rm_id'] = line_split[2] # room id
    data['lat'] = line_split[3] # latitude
    data['lon'] = line_split[4] # longitude
    data['name'] = line_split[5] # name 
    data['rm_cat'] = line_split[8] # room category
    data['rm_type'] = line_split[9] # room type
    data['dv_id'] = line_split[10] # structure type
    data['dp_id'] = line_split[11] # structure
    
    
    for i in data:
        print i + ' ' + data[i]
    

if __name__ == '__main__':
    read_file(path)