#!/usr/bin/python
"""Aliases for constants and units of acceleration, with support for prefixes
"""
# pylint: disable=I0011, E0611

from . import _update_module
from ..units import _units, g_0

_update_module(__name__, _units, g_0.dimension)
