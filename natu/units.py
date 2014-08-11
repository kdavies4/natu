#!/usr/bin/python
r"""Module with all units defined by the :file:`\*.ini` files in
:attr:`natu.config.definitions`

This module cannot be reloaded.  This prevents conflicts that could arise
if the units were redefined with different `base constants <base-ini.html>`_.
"""
__author__ = "Kevin Davies"
__email__ = "kdavies4@gmail.com"
__copyright__ = ("Copyright 2013-2014, Kevin Davies, Hawaii Natural Energy "
                 "Institute, and Georgia Tech Research Corporation")
__license__ = "BSD-compatible (see LICENSE.txt)"

if __name__ == '__main__':
    # Test the contents of this file.
    import doctest
    doctest.testmod()
else:
    # Replace the module with a UnitsModule for dynamic unit prefixing.
    from sys import modules
    from .core import UnitsModule
    from .config import definitions
    modules[__name__] = UnitsModule(modules[__name__], definitions)
