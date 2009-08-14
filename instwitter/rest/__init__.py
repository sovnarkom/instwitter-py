'''
Created on Jul 31, 2009

@author: aleksandrcicenin
'''

from .. import InsTwitterError, InsTwitterResponseError
from .. import TwitterAPI
from ..authenticators import Authenticator, authneeded


from urllib.parse import urlencode
from http.client import HTTPConnection, HTTPResponse
from mimetypes import guess_type
from email.generator import _make_boundary 

from http.client import MULTIPLE_CHOICES, MOVED_PERMANENTLY, FOUND, \
                        SEE_OTHER, TEMPORARY_REDIRECT

REDIRECTS = (MULTIPLE_CHOICES, MOVED_PERMANENTLY, FOUND, 
             SEE_OTHER, TEMPORARY_REDIRECT)

class RESTAPI(TwitterAPI, Authenticator):
    
    _format = '' 
    
    def __init__(self, formatter_type, user_agent=None):
        super().__init__(formatter_type, user_agent)
        self.max_redirects = 100 
        
    def _get_request_data_solving_redirects(self, method, path, data, headers):
        conn = StrHTTPConnection(self._host)
        r = 0
        while r < self.max_redirects:
            conn.request(method, path, data, headers)
            response = conn.getresponse()
            if response.status in REDIRECTS:
                path = response.getheader('Location', path) # TODO: unparse host 
                r += 1
            else:
                break
        if r == self.max_redirects:
            raise InsTwitterResponseError('Redirects exceeded!')
        return response

    def _get_request_data(self, path, params=None, authorize=False):
        if params is not None:
            qpath = path + '?' + urlencode(params)
        else:
            qpath = path
        headers = dict(self._headers)
        if authorize:
            self._add_auth_header(headers, 'GET', path, params)
        return self._process_response(
            self._get_request_data_solving_redirects('GET', qpath, None, headers)
        )

    def _post_request_data(self, path, params=None, authorize=False, method='POST'):
        if params is not None:
            body = urlencode(params)
        headers = dict(self._headers)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        if authorize:
            self._add_auth_header(headers, method, path, params)
        return self._process_response(
            self._get_request_data_solving_redirects(method, path, body, headers)
        )

    def _multipart_post_file_request_data(self, path,
                                        params=None, filename=None,
                                        authorize=False, method='POST'):
        headers = dict(self._headers)
        content_type, body = encode_multipart_formdata(
            params, [("image", filename, open(filename, mode='rb').read())]
        )
        headers['Content-Type'] = content_type
        headers['Content-Length'] = str(len(body))
        if authorize:
            self._add_auth_header(headers, method, path)
        return self._process_response(
            self._get_request_data_solving_redirects(method, path, body, headers)
        )


class StrHTTPResponse(HTTPResponse):
    
    def read(self, amt=None):
        return super().read(amt).decode()


class StrHTTPConnection(HTTPConnection):
    response_class = StrHTTPResponse


def encode_multipart_formdata(fields, files):
    BOUNDARY = _make_boundary()
    CRLF = ('\r\n').encode()
    L = []
    if fields is not None:
        for key in fields:
            L.append(('--' + BOUNDARY).encode())
            L.append(('Content-Disposition: form-data; name="%s"' % key).encode())
            L.append(('').encode())
            L.append(fields[key].encode())
    for (key, filename, value) in files:
        L.append(('--' + BOUNDARY).encode())
        L.append(('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename)).encode())
        L.append(('Content-Type: %s' % get_content_type(filename)).encode())
        L.append(('').encode())
        L.append(value)
    L.append(('--' + BOUNDARY + '--').encode())
    L.append(('').encode())
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body


def get_content_type(filename):
    return guess_type(filename)[0] or 'application/octet-stream'
