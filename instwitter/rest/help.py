'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from . import RESTAPI
 
class HelpAPI(RESTAPI):
    
    def help_test(self): 
        path = self._get_method_path('/help/test')
        return self._get_request_data(path)
    