'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from . import RESTAPI

class SearchAPI(RESTAPI):
    
    _host = 'search.twitter.com'
    
    def search(self, q, callback=None, lang=None, rpp=None, page=None, since_id=None, geocode=None, show_user=None):
        params = self.filter_method_params(locals())
        path = self._get_method_path('search')
        return self._get_request_data(path, params)
    
    def search_trends(self):
        path = self._get_method_path('trends')
        return self._get_request_data(path)
    
    def search_current(self, exclude=None):
        params = self.filter_method_params(locals())
        path = self._get_method_path('trends/current')
        return self._get_request_data(path, params)
    
    def search_daily(self, date=None, exclude=None):
        params = self.filter_method_params(locals())
        path = self._get_method_path('trends/daily')
        return self._get_request_data(path, params)
    
    def search_weekly(self, date=None, exclude=None):
        params = self.filter_method_params(locals())
        path = self._get_method_path('trends/weekly')
        return self._get_request_data(path, params)