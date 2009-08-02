'''
Created on Aug 2, 2009

@author: aleksandrcicenin
'''

from . import Formatter

from xml.dom import minidom

class RawXML(Formatter):

    _format = '.xml'
    
    
class XML(RawXML):
    
    def format(self, data):
        return minidom.parseString(data)
