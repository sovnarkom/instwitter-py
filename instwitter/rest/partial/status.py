'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import RESTAPI, authneeded
 
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
    def status_retweet(self, id):
        path = self._get_method_path('statuses/retweet/' + id)
        return self._post_request_data(path, {}, True) 

    @authneeded
    def status_destroy(self, id):
        path = self._get_method_path('statuses/destroy/' + id)
        return self._post_request_data(path, None, True, 'DELETE') 

    def statuses_public_timeline(self):
        path = self._get_method_path('statuses/public_timeline')
        return self._get_request_data(path)

    @authneeded
    def statuses_friends_timeline(self, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('statuses/friends_timeline')
        return self._get_request_data(path, params, True)

    @authneeded
    def statuses_home_timeline(self, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('statuses/home_timeline')
        return self._get_request_data(path, params, True)

    @authneeded
    def statuses_retweeted_by_me(self, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('statuses/retweeted_by_me')
        return self._get_request_data(path, params, True)

    @authneeded
    def statuses_retweeted_to_me(self, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('statuses/retweeted_to_me')
        return self._get_request_data(path, params, True)

    @authneeded
    def statuses_retweets_of_me(self, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('statuses/retweets_of_me')
        return self._get_request_data(path, params, True)

    def statuses_user_timeline(self, id=None, user_id=None, screen_name=None, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('statuses/user_timeline/' + id)
        else:
            path = self._get_method_path('statuses/user_timeline')
        return self._get_request_data(path, params, self.can_authorize())
    
    @authneeded
    def statuses_mentions(self, since_id=None, max_id=None, count=None, page=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('statuses/mentions')
        return self._get_request_data(path, params, True)
