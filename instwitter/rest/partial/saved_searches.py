'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import RESTAPI, authneeded
 
class SavedSearchesAPI(RESTAPI):
    
    @authneeded
    def saved_searches(self):
        path = self._get_method_path('saved_searches')
        return self._post_request_data(path, None, True)         

    @authneeded
    def saved_search_show(self, id):
        path = self._get_method_path('saved_searches/show/' + id)
        return self._get_request_data(path, None, True)

    @authneeded
    def saved_search_create(self, query):
        params = self._filter_method_params(locals())
        path = self._get_method_path('saved_searches/create')
        return self._post_request_data(path, params, True)
    
    @authneeded
    def saved_search_destroy(self, id):
        path = self._get_method_path('saved_searches/destroy/' + id)
        return self._post_request_data(path, None, True, 'DELETE')