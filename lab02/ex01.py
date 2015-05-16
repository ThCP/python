'''
Created on 23/mar/2015

@author: POLITO\s191436
'''

from sys import argv
import os
import mutagen
from mutagen.mp3 import MP3

file_list = []

class track(object):
    def __init__(self, name, audio):
        self.name = name
        self.length = audio.length
        self.bitrate = audio.bitrate
        
        
class tracks (object):
    def __init__(self, collection):
        


def crawlDirs(root_directory):
    for dir in os.walk(root_directory, followlinks=True):
        
        for filename in dir[2]:
            if filename.endswith(".mp3"):
                file_list.append(track(filename, MP3(filename)))
                #audio = MP3(filename)
                #file_list.append(audio)
            '''
            or filename.endswith(".flac"):
                i+=1
                audio = 
                file_list.append(object)
            '''
    
                
def index(root):
    crawlDirs(root)
    for i in file_list:
        print "%s length %f bitrate %d" % (i.name, i.audio.info.length, i.audio.info.bitrate)
  
def search(tag_name, text):
    pass

def list():
    pass

def main ():
    output = []
    
    command = ""
    
    while command != "exit": 
        command = raw_input("Insert the command: ")
        if command == "index":
            index (argv[2])
        elif command == "search":
            search(argv[2], argv[3])
        elif command == "list":
            list()    
    elif argv[1] == "list":
        list()
        
    elif argv[1] == "exit":
        print "Exiting program"
    else:
        print "Unknown command %d, exiting"
    
if __name__ == '__main__':
    main()
    