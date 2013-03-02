CrunchBase
==========

This is a Python Library for the Crunchbase API.

Disclaimer
----------

This project is a complete rewrite of the original, and it breaks backward
compatibility. Please report any issues at
`bradmontgomery/crunchbase <https://github.com/bradmontgomery/crunchbase/issues>`_.

Any feedback on this work is greatly appreciated. Feel free to open an issue
to critique and/or make suggestions.


Dependencies
------------

This Library requires the following:

* `requests <http://python-requests.org>`_
* json (included in Python 2.6+) or `simplejson <http://pypi.python.org/pypi/simplejson/>`_


Installation
------------

Either clone this repo, and place it somewhere on your PYTHONPATH, or use pip
to install directly from this repo::

    pip install git+git://github.com/bradmontgomery/crunchbase.git@refactor#egg=crunchbase


API Documentation
-----------------

The CrunchBase API docs are available at `<http://developer.crunchbase.com/docs>`_.
Please refer to those docs in order to understand the API.


Usage
-----

This wrapper closely follows the published api. To get started, you first need
to set your API key (Register for a key at `<http://developer.crunchbase.com/>`_).
By default, this library looks for you key in an environment variable named
``CRUNCHBASE_API_KEY``::

    >>> from os import environ
    >>> environ['CRUNCHBASE_API_KEY'] = 'YOUR-KEY-HERE'

Now, you can create an instance of the ``CrunchBase`` class::

    >>> from cunchbase import api
    >>> cb = api.CrunchBase()

Then, you can call this instance directly, specifying the ``namespace`` and
``permalink`` values as a dotted path. Typical requests to the CrunchBase API
looks something like this::

    curl http://api.crunchbase.com/v/1/<namespace>/<permalink>.js

So, requests using this library will look something like this::

    >>> data = cb('namespace.permalink')

Additionally, query string parameters can be specified as a ``params``
dictionary::

    >>> data = cb('search', params={'query': 'iphone', 'page': '2'})

This would perform the following search::

    curl http://api.crunchbase.com/v/1/search.js?query=iphone&page=2


Additional Examples
-------------------

Retrieve data for Facebook::

    >>> data = cb('company.facebook')

Retrieve information about a person::

    >>> data = cb('person.brad-fitzpatrick')

Retrieve information about a financial organization::

    >>> data = cb('financial-organization.accel-partners')

List companies::

    >>> data = cb('companies')

List products::

    >>> data = cb('products')


Permalink Entities
------------------

The API to query a Permalink Entity is slightly different from the above
examples. The ``CrunchBase.permalink`` method allows you to query this data.

Retrieve Google's permalink data::

    >>> data = cb.permalink('companies', {'name': 'Google'})

Retrieve the permalink for a product::

    >>> data = cb.permalink('products', {'name': 'iPhone'})

Retrieve the permalink for a Financial Organization::

    >>> data = cb.permalink(
            'financial-organizations':
            {'name': 'Sequoia Capital'}
        )


TechCrunch Posts API
--------------------

Similar to the Permalink Entity API, there is a ``CrunchBase.posts`` method
that lets you see how many times a particular company has been written about
on TechCrunch?

See how often "Sequoia Captial" gets written about::

    >>> data = cb.posts('financial-organizations', {'name': 'Sequoia Capital'})

See TechCrunch posts about "Ron Conway"::

    >>> data = cb.posts('people', {'first_name': 'Ron', 'last_name': 'Conway'})


License
-------

This code was originally licensed under the WTFPL license, but is now
distributed under the terms of the MIT license, by permission of the original
author. See the ``LICENSE.txt`` file.
