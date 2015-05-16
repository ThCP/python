'''
Created on 13/mag/2015

@author: Riccardo
'''

class Station(object):
    '''
    classdocs
    '''
    station_data = {
            '''
            all the station data
            '''
    
            'stationID' : '000',
            'stationIP' : '0.0.0.0',
            'lat' : '0000000',
            'long' : '0000000',
    
            }

    def __init__(self, data):
        '''
        Constructor
        '''
        self.station_data = data