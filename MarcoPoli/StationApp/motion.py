'''
Created on 25/mag/2015

@author: Luca Mezzatesta
'''

import io
import picamera
from time import sleep
from PIL import Image

COLOR_DIFF_LIMIT = 20 # Color invariation
SLEEP_TIME = 2

'''
Main Method
'''
def get_motion():

    images = []
    
    # Capture the first image
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.resolution = (64,36)
        camera.start_preview()
        camera.capture(stream, format='jpeg')
    stream.seek(0)

    images.append(Image.open(stream))

    sleep(SLEEP_TIME)

    # Capture the second image
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.resolution = (64,36)
        camera.start_preview()
        camera.capture(stream, format='jpeg')
    stream.seek(0)

    images.append(Image.open(stream))

    # Comparing images
    x = 0
    y = 0
    diff = 0

    while( x < images[0].size[0]):
        while( y < images[0].size[1] ):
            img1 = images[1].getpixel((x,y))
            val1 = img1[0]+img1[1]+img1[2]
            img2 = images[0].getpixel((x,y))
            val2 = img2[0]+img2[1]+img2[2]

            abs_value = abs(val2-val1)

            if( abs_value > COLOR_DIFF_LIMIT ):
                diff += 1

            y += 1

        x+=1
        y=0

    return (diff*100)/(images[0].size[0]*images[0].size[1])
