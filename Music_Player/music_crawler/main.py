'''
Created on 13/apr/2015

@author: riccardo
'''
from music_crawler.trackClasses import TrackList, Track
import os
from music_player.music_player import Player

def main():
    track_list = TrackList()
    player = Player()
   # read_commands(track_list, player)
    
    
def read_commands (track_list, player):
    command = ""
    
    while command != "exit":
        #read command
        cmd_string = raw_input("> ")
        cmd_split = cmd_string.split();
        cmd = cmd_split[0].strip().lower()
        print cmd
        
        #handle commands
        if (cmd == "index"):
            if len (cmd_split) != 2:
                pass
            else:
                root_folder = cmd_split[1].strip().lower()
                track_list.add(track_list.scan(root_folder))
                
        elif (cmd == "search"):
            if len (cmd_split) != 3:
                pass
            else:
                tag = cmd_split[1].strip().lower()
                value = cmd_split[2].strip().lower()
                matches = track_list.search(tag, value)
                for t in matches:
                    print "%d - %s" % (t.ID, t.path)
                
                print "Found %d matches." % len (matches)

        elif (cmd == "show"):
            if len(cmd_split) != 2:
                pass
            else:
                track_list.tracks[int(cmd_split[1])].display()
        elif (cmd == "list"):
            track_list.list()
        elif (cmd == "exit"):
            print "Program exiting."
#         elif (cmd == "play"):
#             track = track_list.tracks[int(cmd_split[1].strip())]
#             player.play(track.path)
#         elif (cmd =="stop"):
#             player.stop()
#         
        
        else:
            print "Unknown command."
            pass
        
if __name__ == '__main__':
    main()
        