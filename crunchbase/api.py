from .endpoint import Endpoint
from .settings import CRUNCHBASE_API_URL, CRUNCHBASE_API_KEY


class CrunchBase(object):

    def __init__(self, *args, **kwargs):
        self.endpoint = Endpoint(url=CRUNCHBASE_API_URL, extension='.js')
        self.params = {"api_key": CRUNCHBASE_API_KEY}

    def __call__(self, path, params=None):
        if params:
            self.params.update(params)
        return self.endpoint(path, params=self.params)
