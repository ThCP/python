'''
Created on 18/mag/2015
@author: Riccardo Cappuzzo
'''
import sqlite3

conn = sqlite3.connect("database.db")
####################################################
################## !! STATIONS !! ##################

################## SEARCH ENTRIES ##################
def fetch_station_data ():
    pass

################## CREATE ENTRIES ##################    
def create_station_db():
    pass

def insert_new_station (station_data):
    pass
        
################## UPDATE ENTRIES ##################
def update_station_data (station_data, station_ID):
    pass

####################################################
##################   !! USERS !!  ##################

################## SEARCH ENTRIES ##################
def fetch_user_by_ID():
    pass

def print_all_users ():
    pass

################## CREATE ENTRIES ##################    
def insert_new_user (user_data):
    pass    
    
################## UPDATE ENTRIES ##################

####################################################
################### DESTINATIONS ###################

################## SEARCH ENTRIES ##################
def fetch_destination_by_name(name):
    pass

def fetch_destination_by_ID(ID):
    pass

def fetch_destination_by_type(type): # classroom, study room, bar, laboratory
    pass

def fetch_destination_by_rankl(rank):
    pass

################## CREATE ENTRIES ##################    
def create_ranking_table():
    pass

def insert_destinations_in_ranked_table():
    pass
    
################## UPDATE ENTRIES ##################
# we need a parallel table which contains the ranking of the room, and we update that one
def update_rank_destination():
    pass
    
    
    
if __name__ == '__main__':
    pass