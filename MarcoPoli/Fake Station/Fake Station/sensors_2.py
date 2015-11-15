'''
Created on 15/mag/2015

@author: Luca Mezzatesta
'''

from time import sleep

'''
Fetch data from Z-Wave multiple sensors module and from the microphone
'''
def fetch_data():

    # Data dictionary
    sensors_data = {'temperature':25,'humidity':14,'light':10}
    sensors_data['noise'] = 3
    sensors_data['people'] = 2

    print sensors_data

    sleep(5)
    
    return sensors_data
