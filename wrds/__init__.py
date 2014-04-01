# -*- coding: utf-8 -*-

"""
WRDS Python Data Access Library
==============================

WRDS-Py is a library for extracting data from WRDS data sources and getting it into Pandas.

    >>> import wrds
    >>> data = wrds.sql('select * from Crsp.msi', index='DATE')
    >>> data.head()

There will be more added to this, including additional data processing methods.

"""

__title__ = 'wrds-py'
__version__ = '0.1.0'
__author__ = 'Eric Stein'
__copyright__ = '2014 Wharton Research Data Services'

from .sql import SQLConnection
