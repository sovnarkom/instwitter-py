'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from . import TwitterAPI, InsTwitterResponseError
import oauth

from http.client import HTTPResponse, HTTPSConnection

class OAuthAPI(TwitterAPI):
    
    def __init__(self, consumer_key, consumer_secret):
        super().__init__()
        self._signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1() 
        self._consumer = oauth.OAuthConsumer(consumer_key, consumer_secret)
    
    def request_token(self):
        connection = HTTPSConnection(self._host)
        request = oauth.OAuthRequest.from_consumer_and_token(self._consumer, 
            http_url='https://' + self._host + '/oauth/request_token')
        request.sign_request(self._signature_method, self._consumer, None)
        connection.request(request.http_method, request.to_url())
        resp = connection.getresponse()
        if resp.status == 200: 
            self._oauth_token = oauth.OAuthToken.from_string(resp.read().decode())
            return {'key': self._oauth_token.key, 'secret': self._oauth_token.secret}
        else:
            raise InsTwitterResponseError(resp.code, resp.read().decode()) 

    def authorize_url(self, token_key, token_secret):
        token = oauth.OAuthToken(token_key, token_secret)
        request = oauth.OAuthRequest.from_consumer_and_token(self._consumer, 
            http_url='https://' + self._host + '/oauth/authorize',
            token=token)
        request.sign_request(self._signature_method, self._consumer, token)
        return request.to_url()

    def authenticate_url(self, token_key, token_secret, callback_url, force_login=False):
        token = oauth.OAuthToken(token_key, token_secret)
        params = {'oauth_callback': callback_url}
        if force_login is True:
            params['force_login'] = 'true'
        request = oauth.OAuthRequest.from_consumer_and_token(self._consumer, 
            http_url='https://' + self._host + '/oauth/authenticate',
            token=token,
            params=params)
        request.sign_request(self._signature_method, self._consumer, token)
        return request.to_url()
    
    def access_token(self, token_key, token_secret, pin=None):
        token = oauth.OAuthToken(token_key, token_secret)
        connection = HTTPSConnection(self._host)
        if pin is not None:
            pinparam = {'oauth_verifier': pin}
        else:
            pinparam = None
        request = oauth.OAuthRequest.from_consumer_and_token(self._consumer, token=token, 
            http_url='https://' + self._host + '/oauth/access_token', parameters=pinparam)
        request.sign_request(self._signature_method, self._consumer, token)
        connection.request(request.http_method, request.to_url())
        resp = connection.getresponse()
        if resp.status == 200: 
            self._oauth_token = oauth.OAuthToken.from_string(resp.read().decode())
            return {'key': self._oauth_token.key, 'secret': self._oauth_token.secret}
        else:
            raise InsTwitterResponseError(resp.code, resp.read().decode()) 
    