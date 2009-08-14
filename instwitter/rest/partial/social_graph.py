'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import RESTAPI

class SocialGraphAPI(RESTAPI):
   
    def social_graph_friends_ids(self,  id=None, user_id=None, screen_name=None, page=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('friends/ids/' + id)
        else:
            path = self._get_method_path('friends/ids')
        return self._get_request_data(path, params, False)
        
    def social_graph_followers_ids(self,  id=None, user_id=None, screen_name=None, page=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('followers/ids/' + id)
        else:
            path = self._get_method_path('followers/ids')
        return self._get_request_data(path, params, False)