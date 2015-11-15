'''
Created on 25/mag/2015

@author: Luca Mezzatesta
'''
import wave
import math
import os

import numpy as np
from scipy.io import wavfile

RATE = 44100
REC_TIME= 10

FileNameTmp = '/home/pi/MarcoPoli/MarcoPoli/StationApp/Recordings/noise.wav'

def get_noise():

    # Recording noise
    command = "arecord -f cd -r "+str(RATE)+" -D plughw:0 -d "+str(REC_TIME)+" "+FileNameTmp
    os.system(command)

    # Opening noise file
    noise = wave.open(FileNameTmp,'rb')

    # Getting noise data
    sampFreq, snd = wavfile.read(FileNameTmp)
    snd = snd/(2.**15)

    # Selecting only the first channel
    s1 = snd[:,0]

    # Calculating rms value
    rms_val = math.sqrt(np.mean(s1**2))

    # Deleting noise file
    os.system("rm " + FileNameTmp);

    # Returning rms value * 100 (values: 1 to 23?)
    return int(rms_val*100)
