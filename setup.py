from setuptools import setup
from crunchbase import __version__, __author__

setup(
    name="python-crunchbase",
    version=__version__,
    author=__author__,
    author_email="mehta.apurva@gmail.com",
    description="Libraries for interacting with the Crunchbase API",
    long_description=open('README.rst').read(),
    url="http://github.com/bradmontgomery/crunchbase",
    license="MIT",
    packages=['crunchbase'],
    include_package_data=True,
    package_data={'': ['README.rst', 'AUTHORS.txt', 'LICENSE.txt']},
    zip_safe=False,
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ]
)
