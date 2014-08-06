#!/usr/bin/python
"""Aliases for the `SI units`_


.. _SI units: http://en.wikipedia.org/wiki/International_System_of_Units
"""
# pylint: disable=I0011, C0103, E0611

from . import _update_module
from ..units import _units

# [BIPM2006, Table 1]: SI base units
# g is included so that it can be used with other prefixes than k.
units = {symbol: _units[symbol] for symbol in 'm kg g s A K mol cd'.split()}

# [BIPM2006, Table 3]: Coherent derived units in SI with special names and
# symbols
units.update({symbol: _units[symbol] for symbol in
              ('rad sr Hz N Pa J W C V F ohm S Wb T H degC lm lx Bq Gy '
               'Sv kat'.split())})

_update_module(__name__, units)
