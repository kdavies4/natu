#!/usr/bin/python
"""Aliases for amounts of substance, with support for prefixes
"""
# pylint: disable=I0011, E0611

from . import _update_module
from ..units import _units, mol

_update_module(__name__, _units, mol.dimension)
