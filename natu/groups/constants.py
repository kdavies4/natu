#!/usr/bin/python
"""Aliases for physical constants, with support for prefixes
"""
# pylint: disable=I0011, C0103, E0611

from . import _update_module
from ..units import _units
from ..core import Quantity, Unit

# Constants are quantities but not units.
units = {symbol: quantity for symbol, quantity in _units.items()
         if isinstance(quantity, Quantity) and not isinstance(quantity, Unit)}
try:
    units.update({'k_A': _units['k_A']}) # Ampere's constant is a ScalarUnit.
except KeyError:
    pass

_update_module(__name__, units)
