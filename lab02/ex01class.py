'''
Created on 23/mar/2015

@author: POLITO\s191436
'''

import mutagen
from mutagen.mp3 import MP3
from mutagen import id3
import os

def main ():
    root_directory = ""

    #while root_directory != "exit":
        
        #root_directory = raw_input("Insert the root directory: ")
    root_directory = "."
    if root_directory == "exit":
        print "end of program"
    else: 
        crawlDirs(root_directory)

    
def findstuff (filename):
    track = id3.ID3(filename)
    val = track.getall("TIT2")
    print "val"
    print val[0]

def crawlDirs(root_directory):
    i = 0
    
    print "Root = " + root_directory
    
    for dir in os.walk(root_directory, followlinks=True):
        
        for filename in dir[2]:
            if filename.endswith(".mp3"): 
                audio = MP3(filename)
                findstuff(filename)
                print "length: %f bitrate: %d " % (audio.info.length, audio.info.bitrate)
            if filename.endswith(".flac"):
                i+=1
                print filename
    
    print "Found %d files." % i

if __name__ == '__main__':
    main()
    