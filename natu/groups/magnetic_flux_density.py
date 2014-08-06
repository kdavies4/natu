#!/usr/bin/python
"""Aliases for constants and units of magnetic flux density, with support for prefixes
"""
# pylint: disable=I0011, E0611

from . import _update_module
from ..units import _units, T

_update_module(__name__, _units, T.dimension)
