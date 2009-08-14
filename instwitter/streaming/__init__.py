'''
From Streaming API Documentation:
———————————————————————————————————————————————————————————————————————————————
IMPORTANT NOTE: The Streaming API is currently under an alpha test
All developers using the Streaming API must tolerate possible  unannounced 
and extended periods of unavailability, especially during off-hours,
Pacific Time. 

New features, resources and policies are being deployed on very little,
if any, notice.

Access to restricted resources is extremely limited and is only granted
on a case-by-case basis after acceptance of an additional terms of service 
document.
———————————————————————————————————————————————————————————————————————————————
'''

from .. import TwitterAPI, InsTwitterResponseError
from ..authenticators import Authenticator, authneeded 
from http.client import HTTPConnection, HTTPResponse
from urllib.parse import urlencode


class StreamingAPI(TwitterAPI, Authenticator):
    _host = 'stream.twitter.com'
    
    def _process_line(self, line):
        if line != '\n' and line != '\n\r':
            try:
                return self.formatter.format(line)
            except Exception:
                pass
        return None
        
    def _generate_stream(self, path, params):
        conn = HTTPConnection(self._host)
        headers = dict(self._headers)
        self._add_auth_header(headers, 'GET', path) 
        qpath = path + '?' + urlencode(params)
        conn.request('GET', qpath, None, headers)
        response = conn.getresponse()
        if response.status == 200:
            while not response.closed:
                result = self._process_line(response.readline().decode())
                if result is not None:
                    yield result
        else:
            raise InsTwitterResponseError(response.status, response.read().decode())
        
    # hose

    @authneeded
    def firehose(self, count=None, delimited=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('firehose')
        self._generate_stream(path, params)
    
    @authneeded
    def gardenhose(self, count=None, delimited=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('gardenhose')
        self._generate_stream(path, params)
    
    # public
    @authneeded
    def spritzer(self, delimited=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('spitzer')
        self._generate_stream(path, params)
    
    # followings
    
    @authneeded
    def birddog(self, follow, count=None, delimited=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('birddog')
        self._generate_stream(path, params)

    @authneeded
    def shadow(self, follow, count=None, delimited=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('shadow')
        self._generate_stream(path, params)
    
    # public
    @authneeded
    def follow(self, follow, delimited=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('follow')
        self._generate_stream(path, params)
    
    # track

    @authneeded
    def track(self, track, delimited=None):
        params = self._filter_method_params(locals())
        path = self._get_method_path('track')
        return self._generate_stream(path, params)

