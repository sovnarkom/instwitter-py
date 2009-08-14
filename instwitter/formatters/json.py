'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from . import Formatter
from json import loads

class RawJSON(Formatter):
    
    _format = '.json'

    
class JSON(RawJSON):
    
    def format(self, data):
        return loads(data, encoding='utf-8')