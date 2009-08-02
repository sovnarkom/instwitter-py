'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from . import RESTAPI, authneeded
 
class AccountAPI(RESTAPI):
    
    @authneeded
    def account_verify_credentials(self):
        path = self._get_method_path('account/verify_credentials')
        return self._get_request_data(path, None, True)
    
    def account_rate_limit_status(self):
        path = self._get_method_path('account/rate_limit_status')
        return self._get_request_data(path, None, self.can_authorize())

    @authneeded
    def account_end_session(self):
        path = self._get_method_path('account/end_session')
        return self._post_request_data(path, None, True)

    @authneeded
    def account_update_delivery_device(self, device: ('sms', 'im', 'none')):
        params = self._filter_method_params(locals())
        path = self._get_method_path('account/update_delivery_device')
        return self._post_request_data(path, params, True)

    @authneeded
    def account_update_profile_colors(self,
                              profile_background_color=None, 
                              profile_text_color=None,
                              profile_link_color=None,
                              profile_sidebar_fill_color=None,
                              profile_sidebar_border_color=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('account/update_profile_colors')
        return self._post_request_data(path, params, True)

    @authneeded
    def account_update_profile_image(self, file_name=None): 
        path = self._get_method_path('account/update_profile_image')
        return self._multipart_post_file_request_data(path, None, file_name, True)

    @authneeded
    def account_update_profile_background_image(self, file_name=None, tile=None): 
        params = self._filter_method_params(locals(), ['file_name'])
        path = self._get_method_path('account/update_profile_image')
        return self._multipart_post_file_request_data(path, params, file_name, True)

    @authneeded
    def account_update_profile(self,
                               name=None, 
                               email=None,
                               url=None,
                               location=None,
                               description=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('account/update_profile')
        return self._post_request_data(path, params, True)
