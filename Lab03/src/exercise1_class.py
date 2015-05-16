'''
Created on 13/apr/2015

@author: riccardo
'''
import os
from flask import Flask
from flask.templating import render_template
from flask import request
from mutagen.id3 import ID3

app = Flask("home")

# This class should be redone from scratch, building a dictionary as "data" and then filling the dictionary

class Track (object):
    def __init__(self, name, artist, album, genre,ID):
        self.name = name
        self.artist = artist
        self.album = album 
        self.genre = genre
        self.ID = ID

class TrackList (object):
    ID = 0 
    def __init__(self):
        pass
        
    songs = []

def fetch_data (filename, tracks):
    
    #This works only for mp3 files, I should write 
    tags = ID3(filename)
    name = tags.getall("TIT2")
    artist = tags.getall("TPE1")
    album = tags.getall("TALB")
    genre = tags.getall("TCON")
    
    t = Track(name, artist, album, genre, tracks.ID)
    tracks.songs.append(t)
    
    
def scan_folder (root):
    tracks = TrackList()
    
    for directory in os.walk(root, followlinks = True):
        for filename in directory[2]:
            if filename.endswith(".mp3") or filename.endswith(".flac"):
                fetch_data(filename, tracks)
                tracks.ID+=1
                
    return tracks

def main ():
    pass

@app.route("/")
def index():
    return render_template("index.html", songs_temp = tracks.songs)

@app.route("/user.html")
def user():
    return render_template("user.html", user="John Smith")

@app.route("/tracks/<int:ID>")
def song(ID):
    track = tracks.songs[ID]
    return render_template("song.html", track=tracks.songs[ID])

if __name__ == '__main__':
    tracks = scan_folder(".")
    main()
    app.run(debug = True)
    