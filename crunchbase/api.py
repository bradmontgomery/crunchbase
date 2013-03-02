from .endpoint import Endpoint
from .settings import CRUNCHBASE_API_URL, CRUNCHBASE_API_KEY


class ImproperlyConfigured(Exception):
    """Raised when using the CrunchBase class without an api key."""
    pass


class CrunchBase(object):

    def __init__(self, *args, **kwargs):
        api_key = kwargs.get('api_key', CRUNCHBASE_API_KEY)
        if api_key is None:
            raise ImproperlyConfigured(
                "You must set a CRUNCHBASE_API_KEY before you can use the API"
            )
        self.params = {"api_key": api_key}
        self.endpoint = Endpoint(url=CRUNCHBASE_API_URL, extension='.js')

    def __call__(self, path, params=None):
        if params:
            self.params.update(params)
        return self.endpoint(path, params=self.params)

    # ------------------------------------------------------------------------
    #
    # Entities, Search, Lists, all have the same .js extension, but the
    # Permalink & TechCrunchPost Entities do not.
    #
    # :(
    #
    # ------------------------------------------------------------------------

    def _toggle_endpoint_extension(self):
        # ugly hack
        if self.endpoint.extension:
            self.endpoint.extension = ""
        else:
            self.endpoint.extension = ".js"

    def permalink(self, path, params):
        """Query for an Entity's permalink.

        Examples:

            cb = CrunchBase()
            cb.permalink('companies', {'name': 'Google'})

        Results in a request to:

            /companies/permalink?name=Google

        """
        self._toggle_endpoint_extension()
        result = self.__call__(path + ".permalink", params)
        self._toggle_endpoint_extension()
        return result

    def posts(self, path, params):
        """Query for TechCrunch Posts about an Entity.

        Examples:

            cb = CrunchBae()
            cb.posts('financial-organizations', {'name': 'Sequoia Capital'})

        Results in a request to:

            /financial-organizations/posts?name=Sequoia%20Capital

        """
        self._toggle_endpoint_extension()
        result = self.__call__(path + ".posts", params)
        self._toggle_endpoint_extension()
        return result
