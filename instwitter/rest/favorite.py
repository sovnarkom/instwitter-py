'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from . import RESTAPI, authneeded
 
class FavoriteAPI(RESTAPI):
    
    @authneeded
    def favorites(self, id=None, page=None): 
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('favorites/' + id)
        else:
            path = self._get_method_path('favorites')
        return self._get_request_data(path, params, True)
    
    @authneeded
    def favorite_create(self, id):
        path = self._get_method_path('favorites/create/' + id)
        return self._post_request_data(path, None, True)         

    @authneeded
    def favorite_destroy(self, id): 
        path = self._get_method_path('favorites/destroy/' + id)
        return self._post_request_data(path, None, True, 'DELETE')