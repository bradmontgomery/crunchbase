"""
Settings for the crunchbase api. These can be set with environment variables,
or they can be set directly before using the api.

"""
from os import environ

CRUNCHBASE_API_SCHEME = environ.get("CRUNCHBASE_API_SCHEME", "http")
CRUNCHBASE_API_BASE_URL = environ.get(
    "CRUNCHBASE_API_BASE_URL",
    "api.crunchbase.com"
)
CRUNCHBASE_API_VERSION = environ.get("CRUNCHBASE_API_VERSION", "1")

CRUNCHBASE_API_URL = "{0}://{1}/v/{2}/".format(
    CRUNCHBASE_API_SCHEME,
    CRUNCHBASE_API_BASE_URL,
    CRUNCHBASE_API_VERSION
)

CRUNCHBASE_API_KEY = environ.get("CRUNCHBASE_API_KEY", None)
