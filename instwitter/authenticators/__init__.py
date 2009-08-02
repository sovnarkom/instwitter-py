
from base64 import b64encode 
import oauth
from .. import InsTwitterError
 
class Authenticator(object):

    _signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1() 

    def __init__(self):
        self._can_authorize = False

    def set_basic_authentication(self, login, password):
        self._login = login
        self._password = password
        self._can_authorize = True
        self._auth_method = 'basic'
         

    def set_oauth_authentication(self, credits):
        (self._consumer_key, 
        self._consumer_secret,
        self._token_key,
        self._token_secret) = credits 

        self._can_authorize = True
        self._auth_method = 'oauth'
    
    def toggle_authentication(self, on=True):
        self._can_authorize = on
    
    def can_authorize(self):
        return self._can_authorize

    def _add_auth_header(self, headers, http_method, path, params={}):
        if self._auth_method == 'basic':
            headers['Authorization'] = 'Basic ' + b64encode((self._login + ':' + self._password).encode()).decode()
        elif self._auth_method == 'oauth':
            consumer = oauth.OAuthConsumer(self._consumer_key, self._consumer_secret)
            token = oauth.OAuthToken(self._token_key, self._token_secret)
            request = oauth.OAuthRequest.from_consumer_and_token(consumer, token, http_method, 'http://' + self._host + path, params)
            request.sign_request(self._signature_method, consumer, token)
            headers.update(request.to_header())    


class InsTwitterAuthorizeError(InsTwitterError):
    pass


def authneeded(method):
    def decorate(self, *vargs, **kvargs):
        if self.can_authorize():
            return method(self, *vargs, **kvargs)
        else:
            raise InsTwitterAuthorizeError('Need to authorize before calling "' + method.__name__ + '" method!' )
    return decorate

