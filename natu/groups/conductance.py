#!/usr/bin/python
"""Aliases for constants and units of electrical conductance, with support for prefixes
"""
# pylint: disable=I0011, E0611

from . import _update_module
from ..units import _units, S

_update_module(__name__, _units, S.dimension)
