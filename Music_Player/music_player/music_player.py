'''
Created on 16/apr/2015

@author: riccardo
'''
from subprocess import Popen, PIPE

class Player:
    def __init__(self):
        #self.player = Popen ("mplayer -slave -quiet -nolirc -msglevel all=-1 -idle", stdin=PIPE, stdout=PIPE, shell=True)
        pass
    def play (self, filename):
        #self.player.stdin.write("loadfile \"%s\"\n"%filename)   
        pass
    
    def stop (self):
        #self.player.stdin.write("stop\n")
        pass      