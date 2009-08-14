'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import RESTAPI, authneeded
 
class UserAPI(RESTAPI):
    
    def user_show(self, id=None, user_id=None, screen_name=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('users/show' + id)
        else:
            path = self._get_method_path('users/show')
        return self._get_request_data(path, params, self.can_authorize())
    
    def user_friends(self,  id=None, user_id=None, screen_name=None, page=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('statuses/friends' + id)
        else:
            path = self._get_method_path('statuses/friends')
        return self._get_request_data(path, params, self.can_authorize())

    @authneeded
    def user_followers(self, id=None, user_id=None, screen_name=None, page=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('statuses/followers' + id)
        else:
            path = self._get_method_path('statuses/followers')
        return self._get_request_data(path, params, True)
