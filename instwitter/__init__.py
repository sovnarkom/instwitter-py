'''
Twitter API client library for Python 3.x

Somebugs Software Lab (http://somebugs.com)
© 2009 Alexander Chichenin 

Contacts:

sovnarkom@somebugs.com,
http://twitter.com/sovnarkom

———————————————————————————————————————————————————————————————————————————————

Supports:

Twitter REST API (July 2009 version)
Twitter Search API (July 2009 version)
Twitter OAuth API (July 2009 version, via external oauth library)
Twitter Streaming API (July 2009 alpha version)

Depends on:

OAuth Python library by Leah Culver
(ported version included without installer)  
'''

__author__ = 'Alexander Chichenin <sovnarkom@somebugs.com>'
__version__ = '0.9.0'


class TwitterAPI(object):
    _host = 'twitter.com'

    def __init__(self, formatter_type, user_agent='InsTwitter/0.1'):
        super().__init__()
        self._user_agent = user_agent
        self._headers = {'User-Agent': user_agent}
        self.formatter = formatter_type()
        self._format = self.formatter._format 

    def _get_method_path(self, method):
        return '/' + method + self._format

    def _filter_method_params(self, args, delargs=[]):
        params = dict()
        for key in args:
            if args[key] is not None and key != 'self' and key not in delargs:
                value = args[key]
                if isinstance(value, bool):
                    value = str(value).lower()
                elif isinstance(value, tuple):
                    value = ','.join(value)
                params[key] = value
        if params != {}:
            return params
        else:
            return None

    def _process_response(self, response):
        try:
            if response.status == 200:
                return self.formatter.format(response.read())
            else:
                raise InsTwitterResponseError(response.status, response.read())
        except Exception as e:
            raise InsTwitterProcessError('Unable to process request with exception: ' + str(e))
            
            
class InsTwitterError(Exception):
    pass

class InsTwitterProcessError(Exception):
    pass

class InsTwitterResponseError(InsTwitterError):
    
    def __init__(self, error_code, formatted_response=None):
        self._error_code = error_code
        self._formatted_response = formatted_response
        
    def __str__(self):
        return repr(self._error_code) + ': ' + repr(self._formatted_response)