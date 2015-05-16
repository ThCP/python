'''
Created on 13/mag/2015
@author: Riccardo Cappuzzo

'''

from station_list import Station

stations = []
data = {}

def read_station_list():
    file = open ("C:\Users\Riccardo\Programmazione\workspace\prove_server\static\info.txt")
    line = "#"
    while line != "":
        s = Station(data)
        s.station_data["stationID"] = file.readline().rstrip()
        s.station_data["stationIP"] = file.readline().rstrip()
        s.station_data["lat"] = file.readline().rstrip()
        s.station_data["long"] = file.readline().rstrip()
        print s.station_data
        stations.append(s)
        line = file.readline()
    print "done"
    
    
def print_station_list():
    for i in stations:
        for k,v in i.station_data.iteritems():
            print v