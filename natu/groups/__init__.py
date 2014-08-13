#!/usr/bin/python
r"""Modules with groups of units

The :mod:`~natu.groups.si` module includes all of the base and derived `SI
units`_.  The :mod:`~natu.groups.constants` module contains all constants
(physical quantities which are not units).  These modules contain all of the
constants and units with the indicated dimension:

- :mod:`~natu.groups.acceleration`
- :mod:`~natu.groups.amount`
- :mod:`~natu.groups.angle`
- :mod:`~natu.groups.area`
- :mod:`~natu.groups.charge`
- :mod:`~natu.groups.conductance`
- :mod:`~natu.groups.current`
- :mod:`~natu.groups.dimensionless`
- :mod:`~natu.groups.energy`
- :mod:`~natu.groups.force`
- :mod:`~natu.groups.frequency`
- :mod:`~natu.groups.length`
- :mod:`~natu.groups.magnetic_flux`
- :mod:`~natu.groups.magnetic_flux_density`
- :mod:`~natu.groups.mass`
- :mod:`~natu.groups.potential`
- :mod:`~natu.groups.power`
- :mod:`~natu.groups.pressure`
- :mod:`~natu.groups.resistance`
- :mod:`~natu.groups.temperature`
- :mod:`~natu.groups.time`
- :mod:`~natu.groups.velocity`
- :mod:`~natu.groups.volume`

These modules require that the `SI units`_ are defined in the selected
:file:`\*.ini` files.  The `BIPM.ini file <BIPM-ini.html>`_ contains those
definitions, and it is loaded by default.

Each module can only be reloaded once.\ [#f1]_


.. _SI units: http://en.wikipedia.org/wiki/International_System_of_Units

.. rubric:: Footnotes

.. [#f1] This is not unusual in Python.  From :func:`imp.reload`:

   "In many cases, however, extension modules are not designed to be
   initialized more than once, and may fail in arbitrary ways when
   reloaded."
"""
__author__ = "Kevin Davies"
__email__ = "kdavies4@gmail.com"
__copyright__ = ("Copyright 2013-2014, Kevin Davies, Hawaii Natural Energy "
                 "Institute, and Georgia Tech Research Corporation")
__license__ = "BSD-compatible (see LICENSE.txt)"

import sys

from textwrap import fill
from ..core import DimensionedObject, UnitsModule, Unit

DOC_LINE_LENGTH = 74

def _update_module(name, units, dimension=None):
    """Update the module with name *name* (:class`str`) to contain the
    units in :class:`dict` *units*, optionally filtered to those with
    :class:`~natu.core.CompoundDimension` *dimension*.

    If *dimension* is *None*, all units are included.
    """
    # Retrieve the module.
    module = sys.modules[name]

    # Get the units and note the contents.
    if dimension is None:
        module.__doc__ += "\nContents:\n"
    else:
        units = {symbol: unit for symbol, unit in units.items()
                 if symbol != 'coherent_relations'
                 and isinstance(unit, DimensionedObject)
                 and unit.dimension == dimension}
        module.__doc__ += "\nDefault contents:\n"
    module.__doc__ += fill(", ".join(sorted(units)), DOC_LINE_LENGTH)

    # Note the prefixable units, if any.
    prefixable = [symbol for symbol, unit in units.items()
                  if isinstance(unit, Unit) and unit.prefixable]
    if prefixable:
        module.__doc__ += "\n\nPrefixable subset:\n"
        module.__doc__ += fill(", ".join(sorted(prefixable)), DOC_LINE_LENGTH)

    # Update the module.
    sys.modules[name] = UnitsModule(module, units)
