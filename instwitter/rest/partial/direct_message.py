'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import RESTAPI, authneeded
 
class DirectMessageAPI(RESTAPI):
    
    @authneeded
    def direct_messages(self, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('direct_messages')
        return self._get_request_data(path, params, True)

    @authneeded
    def direct_message_sent(self, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('direct_messages/sent')
        return self._get_request_data(path, params, True)

    @authneeded
    def direct_message_new(self, user=None, screen_name=None, user_id=None, text=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('direct_messages/new')
        return self._post_request_data(path, params, True) 
    
    @authneeded
    def direct_message_destroy(self, id):
        path = self._get_method_path('direct_messages/destroy/' + id)
        return self._post_request_data(path, None, True, 'DELETE') 
