#!/usr/bin/python
"""Aliases for constants and units of electrical current, with support for prefixes
"""
# pylint: disable=I0011, E0611

from . import _update_module
from ..units import _units, A

_update_module(__name__, _units, A.dimension)
