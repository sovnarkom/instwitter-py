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

class RESTAPI(TwitterAPI, Authenticator):
    
    _format = '' 
    
    def __init__(self, formatter_type, user_agent='InsTwitter/0.1'):
        super().__init__(formatter_type, user_agent)

    def _get_request_data(self, path, params=None, authorize=False):
        if params is not None:
            qpath = path + '?' + urlencode(params)
        else:
            qpath = path
        conn = StrHTTPConnection(self._host)
        headers = dict(self._headers)
        if authorize:
            self._add_auth_header(headers, 'GET', path, params)
        conn.request('GET', qpath, None, headers)
        response = conn.getresponse()
        return self._process_response(response)

    def _post_request_data(self, path, params=None, authorize=False, method='POST'):
        if params is not None:
            body = urlencode(params)
        conn = StrHTTPConnection(self._host)
        headers = dict(self._headers)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        if authorize:
            self._add_auth_header(headers, method, path, params)
        conn.request(method, path, body, headers)
        response = conn.getresponse()
        return self._process_response(response)

    def _multipart_post_file_request_data(self, path,
                                        params=None, filename=None,
                                        authorize=False, method='POST'):
        conn = StrHTTPConnection(self._host)
        headers = dict(self._headers)
        content_type, body = encode_multipart_formdata(params, [("image", filename, open(filename, mode='rb').read())])
        headers['Content-Type'] = content_type
        headers['Content-Length'] = str(len(body))
        if authorize:
            self._add_auth_header(headers, method, path)
        conn.request(method, path, body, headers)
        response = conn.getresponse()
        return self._process_response(response)


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
