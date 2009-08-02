'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from . import RESTAPI, authneeded
 
class StatusAPI(RESTAPI):
    
    def status_show(self, id):
        path = self._get_method_path('statuses/show/' + id)
        return self._get_request_data(path)
    
    @authneeded
    def status_update(self, status, in_reply_to_status_id=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('statuses/update')
        return self._post_request_data(path, params, True) 

    @authneeded
    def status_destroy(self, id):
        path = self._get_method_path('statuses/destroy/' + id)
        return self._post_request_data(path, None, True, 'DELETE') 
