'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from . import RESTAPI, authneeded
 
class TimelineAPI(RESTAPI):
    
    def status_public_timeline(self):
        path = self._get_method_path('statuses/friends_timeline')
        return self._get_request_data(path)

    @authneeded
    def status_friends_timeline(self, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('statuses/friends_timeline')
        return self._get_request_data(path, params, True)

    def status_user_timeline(self, id=None, user_id=None, screen_name=None, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('statuses/user_timeline/' + id)
        else:
            path = self._get_method_path('statuses/user_timeline')
        return self._get_request_data(path, params, self.can_authorize())
    
    @authneeded
    def status_mentions(self, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('statuses/mentions')
        return self._get_request_data(path, params, True)
