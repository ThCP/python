'''
Created on 13/apr/2015

@author: riccardo
'''

from mutagen import flac, mp3
import os 

class Track(object):
    '''
    classdocs
    '''

    def __init__(self, path=None):
        '''
        Constructor
        '''
        self.path = path
        
        self.ID = None
        
        self.data = self.metadata()
    
    def metadata(self):
        #dictionary
        track_data = {}
        
        # default name
        track_data['title'] = self.path[self.path.rfind('/')+1:self.path.rfind('.')]
        track_data['album'] = None
        track_data['genre'] = None
        track_data['artist'] = None
        
        #detect the current file type
        file_type = self.path[self.path.rfind('.'):]
        
        # handle FLAC files
        if file_type == ".flac":
            metadata = flac.FLAC(self.path)
            # print metadata
            try:
                track_data['title'] = metadata['title'][0]
                track_data['album'] = metadata['album'][0]
                track_data['genre'] = metadata['genre'][0]
                track_data['artist'] = metadata['artist'][0]
            except:
                pass
        #handle MP3 files
        if file_type == ".mp3":
            metadata = mp3.MP3(self.path)
            # print metadata
            try:
                if(metadata.has_key('TIT2')):
                    track_data['title'] = metadata['TIT2'].text[0]
                if(metadata.has_key('TALB')):
                    track_data['album'] = metadata['TALB'].text[0]
                if(metadata.has_key('TCON')):
                    track_data['genre'] = metadata['TCON'].text[0]
                if(metadata.has_key('TPE2')):
                    track_data['artist'] = metadata['TPE2'].text[0]
            except:
                pass
        
        return track_data
    
    def display(self):
        print "Title: %s" % self.data["title"]
        print "Artist: %s" % self.data["artist"]
        print "Album: %s" % self.data["album"]
        print "Genre: %s" % self.data["genre"]
        
class TrackList (object):
        
    def __init__(self):
        self.ID = 0
        self.tracks = []
    # scan the root folder looking for .mp3 and .flac files
    def scan(self, root_folder):
        print root_folder
        
        tracks_in_folder = []
        i = 0
    
        for directory in os.walk(root_folder, followlinks = True):
            for filename in directory[2]: # directory is a list which contains 3 entries, the last entry is the name of the file
                if filename.endswith(".mp3") or filename.endswith(".flac"):
                    new_track = Track(os.path.join(directory[0], filename))
                    #print new_track.path
                    new_track.ID = i
                    
                    tracks_in_folder.append(new_track)
                    i+=1
        return tracks_in_folder
    
    def add(self, tracks):
        
        for track in tracks:
            #reset the ID of the track setting it to the last id of the collection
            track.id = self.ID
            #adds the new track to the collection
            self.tracks.append(track)
            #updates the n. of tracks in the collection
            self.ID+=1

    #shows the content of the collection       
    def list(self):
        
        for track in self.tracks:
            print "#################################"
            track.display()
            
        print "#################################"
        
    #searches for <value> contained in <tag>    
    def search(self, tag, value):
        matches = []
        
        for track in self.tracks:
            if (track.data[tag] != None) and ((track.data[tag].lower() == value) or (track.data[tag].lower().find(value) > -1)):
                matches.append(track)
        return matches