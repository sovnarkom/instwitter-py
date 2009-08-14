'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import RESTAPI, authneeded
 
class NotificationAPI(RESTAPI):
    
    @authneeded
    def notification_follow(self, id=None, user_id=None, screen_name=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('notifications/follow/' + id)
        else:
            path = self._get_method_path('notifications/follow')
        return self._post_request_data(path, params, True)         

    @authneeded
    def notification_leave(self, id=None, user_id=None, screen_name=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('notifications/leave/' + id)
        else:
            path = self._get_method_path('notifications/leave')
        return self._post_request_data(path, params, True)         
