'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import RESTAPI, authneeded
 
class BlockAPI(RESTAPI):
    
    @authneeded
    def block_create(self, id):
        path = self._get_method_path('blocks/create/' + id)
        return self._post_request_data(path, None, True)         

    @authneeded
    def block_destroy(self, id): 
        path = self._get_method_path('blocks/destroy/' + id)
        return self._post_request_data(path, None, True, 'DELETE')
    
    @authneeded
    def block_exists(self, id=None, user_id=None, screen_name=None): 
        params = self._filter_method_params(locals(), ['id'])
        if id is not None:
            path = self._get_method_path('blocks/' + id)
        else:
            path = self._get_method_path('blocks')
        return self._get_request_data(path, params, True)
    
    @authneeded
    def blocks_blocking(self, page): 
        params = self._filter_method_params(locals())
        path = self._get_method_path('blocks/blocking')
        return self._get_request_data(path, params, True)
    
    @authneeded
    def blocks_blocking_ids(self): 
        path = self._get_method_path('blocks/blocking/ids')
        return self._get_request_data(path, None, True)