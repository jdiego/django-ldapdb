# -*- coding: utf-8 -*-
# This software is distributed under the two-clause BSD license.
# Copyright (c) The django-ldapdb2 project

import sys

if sys.version_info < (3, 8):
    import pkg_resources

    __version__ = pkg_resources.get_distribution('django-ldapdb2').version

else:
    import importlib.metadata

    __version__ = importlib.metadata.version('django-ldapdb2')

VERSION = __version__
