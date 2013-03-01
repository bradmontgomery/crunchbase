"""
This module contains an ``Endpoint`` class representing a REST API Endpoint.
It currently only supports GET requests to an api that returns JSON.

Usage:

1. Create a class, and include an attribute that is an Endpoint::

    class HttpBin(object):
        api = Endpoint(url='http://httpbin.org')

    httpbin = HttpBin()

2. Query the endpoints via the api, like so::

    httpbin.api('ip')  -> dict
    httpbin.api('user-agent') -> dict

    # Include querystring params as a dict
    httpbin.api('get', param={'key': 'secret'}) -> dict

3. Results are cached on the Endpoint, so subsequent access does not send
   an http requst.

    httpbin.api('ip') -> returns cached data dict

"""
try:
    import json
    assert json  # placate pyflakes
except ImportError:
    import simplejson as json
import requests


class EndpointUnavailable(Exception):
    pass


class Endpoint(object):
    """A generic api endpoint."""

    def __init__(self, url, extension=''):
        """Sets the API's base URL and creates a cache for results.

        If the api requires an extension (such as .js or .json), that can be
        specified with ``extension``. This will be appended to all api URI's.

        """
        self.url = url + '/' if not url.endswith('/') else url
        self.cache = {}
        self.extension = extension

    def __set__(self, obj, val):
        raise AttributeError("Endpoints are Read-Only")

    def _cache_key(self, path, params=None):
        """Create the key used in the ``cache`` dict."""
        if params is not None:
            path += '.'.join(params.keys())
        return path

    def _build_uri(self, path):
        """Build the uri for the endpoint."""
        path = "/".join(path.split('.'))
        return ''.join([self.url, path, self.extension])

    def _request(self, uri, params=None):
        """Send the http request and return a python dict."""
        resp = requests.get(uri, params=params)
        if resp.status_code == 200:
            return json.loads(resp.content)
        else:
            raise EndpointUnavailable("No response from {0}".format(uri))

    def __call__(self, path, params=None):
        """Query the specified endpoint.

        * ``path``: a string containing a dotted endpoint path.
            e.g. "foo.bar" -> "foo/bar"
        * ``params``: a dict to use as query string params.
            e.g. {'key':'secret'} -> ?key=secret

        """
        cache_key = self._cache_key(path, params)

        if cache_key in self.cache:
            return self.cache[path]
        else:
            uri = self._build_uri(path)
            result = self._request(uri, params=params)
            self.cache[cache_key] = result
            return result
