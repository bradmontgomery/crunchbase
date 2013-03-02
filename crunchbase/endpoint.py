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
import requests


class EndpointUnavailable(Exception):
    pass


class Endpoint(object):
    """A generic api endpoint."""

    def __init__(self, url, extension='', cache_paths=[]):
        """Sets the API's base URL and creates a cache for results.

        If the api requires an extension (such as .js or .json), that can be
        specified with ``extension``. This will be appended to all api URI's.

        By default, a call to a path will result in another HTTP Request. If
        you don't want this, you can specify a list of paths in `cache_paths`.
        For example, if you want to cache results from::

            httpbin.api('user-agent')

        You could create the endpoint with the following::

            class HttpBin(object):
                api = Endpoint(
                    url='http://httpbin.org',
                    cache_paths=['user-agent']
                )

        """
        self.url = url + '/' if not url.endswith('/') else url
        self.cache = {}
        self.extension = extension
        self.cache_paths = cache_paths

    def __set__(self, obj, val):
        raise AttributeError("Endpoints are Read-Only")

    def _build_uri(self, path):
        """Build the uri for the endpoint."""
        path = "/".join(path.split('.'))
        return ''.join([self.url, path, self.extension])

    def _request(self, uri, params=None):
        """Send the http request and return a python dict."""
        resp = requests.get(uri, params=params)
        if resp.status_code == 200:
            if callable(resp.json):
                return resp.json()  # Requests > 1.0
            else:
                return resp.json  # Requests < 1.0
        else:
            raise EndpointUnavailable("No response from {0}".format(uri))

    def __call__(self, path, params=None):
        """Query the specified endpoint.

        * ``path``: a string containing a dotted endpoint path.
            e.g. "foo.bar" -> "foo/bar"
        * ``params``: a dict to use as query string params.
            e.g. {'key':'secret'} -> ?key=secret

        """
        if path in self.cache_paths and path in self.cache:
            return self.cache[path]
        else:
            uri = self._build_uri(path)
            result = self._request(uri, params=params)
            if path in self.cache_paths:
                self.cache[path] = result
            return result
