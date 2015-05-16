'''
Created on 19/mar/2015

@author: riccardo
'''


sam = {'age': 10, 'height': 42, 'weight': 175,'instrument': 'fiddle'}
mary = {'age': 41, 'height': 70, 'weight': 160, 'instrument': 'piano'}
bertha = {'age':32, 'height': 97, 'weight': 587, 'instrument': 'cello'}
david = {'age':100, 'height': 84, 'weight': 0.5, 'instrument': 'cello'}
people = {'Sam': sam,'Mary': mary,'Bertha': bertha,'David': david}

key = raw_input("insert the instrument: ")

players = {
         
         }

for a in people:
    if people[a]["instrument"] == key: # from dict people extract entry a, then go in entry 
        players[a] = people[a]         # a and extract entry instrument

print players

