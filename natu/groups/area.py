#!/usr/bin/python
"""Aliases for constants and units of area, with support for prefixes
"""
# pylint: disable=I0011, E0611

from . import _update_module
from ..units import _units, m

_update_module(__name__, _units, (m ** 2).dimension)
