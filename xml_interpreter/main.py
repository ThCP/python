'''
Created on 04/set/2015

@author: Riccardo
'''

import xml.etree.ElementTree as ET
from _elementtree import tostring

if __name__ == '__main__':
    tree = ET.parse("mangalist_1440973905_-_1205197.xml")
    root = tree.getroot()
    
    for i in root:
        print i.text
    
#    for i in root.findall("./manga/manga_title"):
 #       print i.text