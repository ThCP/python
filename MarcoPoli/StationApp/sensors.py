'''
Created on 15/mag/2015

@author: Luca Mezzatesta
'''

import rest
from noise import get_noise
from motion import get_motion

# the sensor's base_url
base_url = 'http://localhost:8083'

'''
Fetch data from Z-Wave multiple sensors module and from the microphone
'''
def fetch_data():

    # Data dictionary
    sensors_data = fetch_zwavedata()
    sensors_data['noise'] = fetch_noise()
    sensors_data['people'] = fetch_npeople()
    
    return sensors_data

'''
Fetch data from the ZWave
'''
def fetch_zwavedata():
    sensors_data = { 'temperature':-1, 'humidity':-1,'light':-1 }
    
    # get the ZWave Device (there should be only one)
    all_devices = rest.send( url = base_url+'/ZWaveAPI/Data/0')
    
    # get temperature
    temperature = all_devices['devices']['2']['instances']['0']['commandClasses']['49']['data']['1']['val']['value']
    # get humidity 
    humidity = all_devices['devices']['2']['instances']['0']['commandClasses']['49']['data']['3']['val']['value']
    # get light
    light = all_devices['devices']['2']['instances']['0']['commandClasses']['49']['data']['5']['val']['value']
    
    
    sensors_data['temperature']=float(temperature)
    sensors_data['humidity']=float(humidity)
    sensors_data['light']=float(light)
    
    return sensors_data 

'''
Fetch noise from microphone
'''
def fetch_noise():
    return get_noise()

'''
Get the number of people from noise data
'''
def fetch_npeople():
    res = []
    for i in range(0,2):
        res.append( get_motion() )

    return max(res)
