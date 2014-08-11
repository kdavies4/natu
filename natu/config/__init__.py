#!/usr/bin/python
# -*- coding: utf-8 -*-
r"""Configuration settings

This module contains the following settings (defaults summarized in
parentheses):

- *definitions* (`base-SI.ini <base-ini.html>`_, `derived.ini
  <derived-ini.html>`_, `BIPM.ini <BIPM-ini.html>`_, and `other.ini
  <other-ini.html>`_ from the installation directory) - List of files that
  define the constants and units

- *use_quantities* (*True*) - *True* to use quantities to track dimensions
  and display units

     If *use_quantities* is *False*, then the constants and scalar units
     are :class:`float` instances rather than :class:`~natu.core.Quantity`
     and :class:`~natu.core.ScalarUnit` instances.  This reduces the
     computational overhead of the :mod:`natu` module to nearly zero
     while still allowing variables to be specified using various units.
     However, this disables dimension checking and the string formatting of
     quantities as the product of a number and a unit, so it is probably
     best to leave *use_quantities* set to *True* until you have validated
     your unit-dependent code.

- *simplification_level* (2) - Number of non-minimizing substitutions
  that can be made in seeking the best display unit

     A higher number increases the likelihood that the simplest display
     unit will be found, but it also increases the time required to
     process :func:`str`, :func:`print`, :func:`format`, and related
     functions.

- *unit_replacements*
  (in LaTeX_ ('L' format code):
  'deg' → '^{\\circ}',
  'ohm' → '\\Omega', and
  'angstrom' → '\\AA';
  in Unicode_ ('U' format code):
  'deg' → '°',
  'ohm' → 'Ω', and
  'angstrom' → 'Å') - Dictionary of special replacements
  for formatting a unit string

     Each key is a format code and each value is a list of tuples of 1)
     the string to be replaced and 2) the string that it should be
     replaced with.

To change a setting from the default, import this module and change the
setting before importing any other :mod:`natu` submodules.

**Examples:**

To turn off unit simplification:

>>> from natu import config
>>> config.simplification_level = 0

or to append a custom file of unit definitions:

>>> config.definitions.append('custom.ini')

Then use the rest of :mod:`natu`, for instance

>>> from natu.units import *

.. testcleanup::
   >>> print(kg/m/s)
   kg/(m*s)


.. _Unicode: https://en.wikipedia.org/wiki/Unicode
.. _LaTeX: http://www.latex-project.org/
"""
# pylint: disable=I0011, C0103

# List of unit definition files
from os import path
dname = path.dirname(__file__)
definitions = [path.join(dname, fname) for fname in
               ['base-SI.ini', 'derived.ini', 'BIPM.ini', 'other.ini']]
del path, dname

# True to track dimensions and display units:
use_quantities = True

# Number of non-minimizing substitutions that can be made in seeking the
# best display unit:
simplification_level = 2

# Dictionary of special replacements for formatting a unit string
unit_replacements = {'L':  # In LaTeX
                     [('deg', r'^{\circ}'),
                      ('ohm', r'\Omega'),
                      ('angstrom', r'\AA')],
                     'U':  # In Unicode format
                     [('deg', '°'),
                      ('ohm', 'Ω'),
                      ('angstrom', 'Å')],
                    }
