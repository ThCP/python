'''
Created on 19/giu/2015

@author: Riccardo Cappuzzo

This script ranks the stations on the basis of the data gathered by the sensors.
This is the preliminary version, it is possible to change the ranking by acting 
on the weight dictionaries below.

The ranges are still empirical, testing should be performed in order to have a 
more precise result.

Algorithm by
@author: Luca Mezzatesta


'''

import time

alpha = 5 # another value used when normalizing

weights_standard = {
                    'light' : 0,
                    'noise' : 0.4,
                    'people' : 0.3,
                    'humidity' : 0,
                    'temperature' : 0.3
                    }

weights_lunchtime = {
                    'light' : 0,
                    'noise' : 0.2,
                    'people' : 0.6,
                    'humidity' : 0,
                    'temperature' : 0.2
                    }

# create ranking of station
def rank_station (raw_data):
    current_time = time.localtime()
    
    # Hour and minutes extracted from the local time in order to decide which weight to use
    hh = current_time[3]
    mm = current_time[4]
    
    station_data = station_data_normalization (raw_data)

    if raw_data['temperature'] <= 10.0 or raw_data['temperature'] >= 32.0: # this temperature is in degrees
        #temperature too low
        rank = 0
    elif raw_data['humidity'] >= 80.0:
        #humidity too high
        rank = 0
    else: 
        if (hh>=11 and mm >= 30) and hh < 14: # lunchtime
            # use weights_lunchtime
            total = weights_lunchtime['noise'] * station_data['noise'] + \
                    weights_lunchtime['temperature'] * station_data['temperature'] + \
                    weights_lunchtime['humidity'] * station_data['humidity'] + \
                    weights_lunchtime['people'] * station_data['people'] + \
                    weights_lunchtime['light'] * station_data['light']
        else:
            # use standard weights
            total = weights_standard['noise'] * station_data['noise'] + \
                    weights_standard['temperature'] * station_data['temperature'] + \
                    weights_standard['humidity'] * station_data['humidity'] + \
                    weights_standard['people'] * station_data['people'] + \
                    weights_standard['light'] * station_data['light']
        
        rank = 100 - total
    return rank
        
def station_data_normalization (raw_data): # reduces all the station values to a 0-100 scale.
    
    t = raw_data['temperature']
    n = raw_data['noise']
    
    station_data = {}
    
    station_data['temperature'] = ( t - alpha) / ( 40.0 - alpha) * 100.0
    station_data['noise'] = n / 25.0 * 100.0 
    
    station_data['humidity'] = raw_data['humidity']
    station_data['people'] = raw_data['people']
    station_data['light'] = raw_data['light']
    
    return station_data


if __name__ == '__main__': # used for debugging purposes
    station_data = {
                    'temperature' : 16,
                    'light' : 30,
                    'noise' : 2,
                    'people' : 10,
                    'humidity' : 20
                    }
    print rank_station(station_data)
    