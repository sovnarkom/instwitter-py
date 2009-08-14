'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import RESTAPI, authneeded

class FriendshipAPI(RESTAPI):
   
    @authneeded
    def friendship_create(self, id=None, user_id=None, screen_name=None, follow=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('friendships/create/' + id)
        else:
            path = self._get_method_path('friendships/create')
        return self._post_request_data(path, params, True)
    
    @authneeded
    def friendship_destroy(self, id=None, user_id=None, screen_name=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('friendships/destroy/' + id)
        else:
            path = self._get_method_path('friendships/destroy')
        return self._post_request_data(path, params, True, 'DELETE')
    
    def friendship_exists(self, user_a, user_b):
        params = self._filter_method_params(locals())
        path = self._get_method_path('friendships/exists')
        return self._get_request_data(path, params, self.can_authorize())
        
    def friendship_show(self, source_id=None, source_screen_name=None, target_id=None, target_screen_name=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('friendships/show')
        return self._get_request_data(path, params, self.can_authorize())
