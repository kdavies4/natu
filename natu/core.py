# !/usr/bin/python # pylint: disable=I0011, C0302
# -*- coding: utf-8 -*-
r"""Core classes of natu

As shown in the diagram below, there are two types of units: scalar units
and lambda units.  Scalar units are quantities, but lambda units are not.
Lambda units are essentially invertible functions that map between numbers
and quantities.  All units and quantities are dimensioned objects, meaning
that their physical dimension is recorded (even if dimensionless).

.. inheritance-diagram:: DimensionedObject Unit ScalarUnit LambdaUnit Quantity

Numbers, scalar units, and quantities can be used together in mathematical
expressions as long as the expression is dimensionally consistent.
Numbers (:class:`float`, :class:`int`, :class:`~fractions.Fraction`, etc.)
are considered dimensionless.

Lambda units can only be used with numbers and quantities in special
cases.  A lambda unit can be applied to generate a quantity for use in the
rest of a mathematical expression.  The multiplication operator (``*``) is
overloaded so that a number times a lambda unit calls the unit's method to
map the number to a quantity.  Likewise, the division operator (``/``)
uses a lambda unit to map a quantity to a number.

The tables below summarize the type of result given by simple mathematical
operations among numbers, scalar units, lambda units, and quantities.  The
product or quotient of a number and a quantity or scalar unit is a
quantity.  This is the case even if the number is zero; the product of
zero and a unit or quantity still carries the dimension of the unit or
quantity.  A quantity evaluates to *True* if its value is nonzero, but it
is not equal to zero unless its value is zero and it is dimensionless.

The display unit of the first term in addition or subtraction takes
precedence.  If the first term is a number and the second term is a
dimensionless quantity, the result is a number.

Results of multiplication and division:

+--------------+---------------------------+
|              | 2nd argument              |
|              +----+--------+--------+----+
| 1st argument | N  | Q      | S      | L  |
+==============+====+========+========+====+
| N            | N  | Q      | Q      | Q  |
+--------------+----+--------+--------+----+
| Q            | Q  | Q [1]_ | Q [1]_ | N  |
+--------------+----+--------+--------+----+
| S            | Q  | Q [1]_ | S [1]_ | -- |
+--------------+----+--------+--------+----+
| L            | -- | --     | --     | -- |
+--------------+----+--------+--------+----+

Results of addition and subtraction:

+--------------+-------------------------------+
|              | 2nd argument                  |
|              +--------+--------+--------+----+
| 1st argument | N      | Q      | S      | L  |
+==============+========+========+========+====+
| N            | N      | N [2]_ | N [2]_ | -- |
+--------------+--------+--------+--------+----+
| Q            | Q [2]_ | Q      | Q      | -- |
+--------------+--------+--------+--------+----+
| S            | Q [2]_ | Q      | Q      | -- |
+--------------+--------+--------+--------+----+
| L            | --     | --     | --     | -- |
+--------------+--------+--------+--------+----+

Key:

- N: :class:`~numbers.Number`
- Q: :class:`Quantity`
- S: :class:`ScalarUnit`
- L: :class:`LambdaUnit`
- --: Not allowed

.. [1] If the result is dimensionless, it is returned as a number instead.
.. [2] The quantity must be dimensionless.

Here are some consequences of this design:

- Is ``0*ppm`` equal to zero? Yes
- Is ``0*m`` equal to zero? No
- Does ``0*m`` evaluate to ``False``? Yes
- Is ``0*m`` dimensionless? No
- Is ``m/ft`` a quantity or a number? Number (float)
- Is ``ohm*S`` a quantity or a number? Number (1.0)
- Is ``m*m`` a unit? Yes (``'m2'``)
- Is ``1*m*m`` a unit? No (only a quantity)
- Is ``1*ppm`` a unit or a number? Neither (a dimensionless quantity)
- Is ``m + 0`` (or ``0 + m``) valid? No
- Is ``ppm + 0`` (and ``0 + ppm``) valid? Yes
- Is ``ppm + 0`` a quantity or a number? Quantity (1 ppm)
- Is ``0 + ppm`` a quantity or a number? Number (1e-6)
- What is the display unit of ``ft + m``? ``'ft'``
- Is ``m*10`` valid? Yes (``Quantity(10, 'L', 'm') (10.0 m)``)
- Is ``degC*10`` valid? No (use ``10*degC`` instead)

Classes in this module:

- :class:`CoherentRelations` - List of coherent relations among units

- :class:`CompoundDimension` - Dictionary that contains base physical
  dimensions as keys and exponents of those dimensions as values

- :class:`CompoundUnit` - Dictionary that contains the base factors of a
  display unit as keys and exponents of those units as values

- :class:`DimensionedObject` - Base type that tracks physical dimension
  and display unit

- :class:`LambdaUnit` - Unit that involves a offset or other operations
  besides scaling

- :class:`Quantity` - Class to represent a physical quantity

- :class:`ScalarUnit` - Unit that involves just a scaling factor

- :class:`Unit` - Base class for a unit

- :class:`Units` - Dictionary of units with dynamic prefixing

- :class:`UnitsModule` - Class that wraps the :class:`Units` dictionary as
  a module

.. warning::  Be careful if you use this package to produce conversion
   factors.  A factor may be the reciprocal of what you first think.  By
   the phrase "convert from x to y" (where x and y are units), we mean
   "convert from an expression of the quantity in x to an expression of
   the quantity in y".  "Quantity in unit" is generally equivalent to
   "quantity *divided by* unit", and to get from *Q*/x (where *Q* is a
   quantity) to *Q*/y, we must multiply by x/y.  As a practical example,
   the conversion factor from feet to meters is ``ft/m`` (0.3048) using
   :mod:`natu.units`.

   - Adapted from SciMath
     (http://docs.enthought.com/scimath/units/intro.html, accessed
     7/10/2014)

Known issues:

- Python's built-in :func:`sum` will only accept dimensionless
  quantities.  Consider using :func:`natu.math.fsum` instead.
"""

# pylint: disable=I0011, C0103, C0111, C0301, C0325, E0213, E1101, F0401, R0903
# pylint: disable=I0011, W0142, W0212, W0223, W0621

# Always use floating division:
from __future__ import division

# So that math is the modules from the Python Standard Library:
from __future__ import absolute_import

__author__ = "Kevin Davies"
__email__ = "kdavies4@gmail.com"
__copyright__ = ("Copyright 2013-2014, Kevin Davies, Hawaii Natural Energy "
                 "Institute, and Georgia Tech Research Corporation")
__license__ = "BSD-compatible (see LICENSE.txt)"

__all__ = ('CoherentRelations CompoundDimension CompoundUnit DimensionedObject '
           'Quantity Unit ScalarUnit LambdaUnit Units UnitsModule'.split())

import math
import re

from os.path import dirname
from types import ModuleType
from functools import wraps
# from warnings import warn
from .util import format_e, product, str2super
from ._prefixes import PREFIXES
from .config import simplification_level, use_quantities, unit_replacements
from .exponents import Exponents, split_code, u, i

try:
    from configparser import (RawConfigParser, ParsingError,
                              Error as ConfigParserError)
except ImportError:
    # For Python 2:
    from ConfigParser import (RawConfigParser, ParsingError,
                              Error as ConfigParserError)

# Compile the formatted unit replacements.
UNIT_REPLACEMENTS = {fmt:
                     [(re.compile(rpl[0]), rpl[1]) for rpl in rpls]
                     for fmt, rpls in unit_replacements.items()}


# Standard functions
# ------------------

def assert_homogeneous(*args):
    r"""Assert that *\*args* have the same dimension.

    If any argument does not have a :attr:`~DimensionedObject.dimension`
    property, it is assumed to be dimensionless.

    **Example:**

    >>> from natu.units import m, ft, s
    >>> assert_homogeneous(m, ft)
    >>> assert_homogeneous(m, s) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    AssertionError: The quantities must have the same dimension.


    """
    dim = dimension(args[0])
    for arg in args[1:]:
        assert dimension(arg) == dim, \
            "The quantities must have the same dimension."


def dimension(quantity):
    """Return the dimension of *quantity*.

    If *quantity* does not have a :attr:`~DimensionedObject.dimension`
    property, it is assumed to be dimensionless and an empty
    :class:`CompoundDimension` is returned.

    **Example:**

    >>> from natu.units import Pa
    >>> print(dimension(Pa))
    M/(L*T2)
    """
    try:
        return quantity.dimension
    except AttributeError:
        return CompoundDimension()


def dimensionless_value(x):
    """Return the value of the quantity if it is dimensionless.

    Otherwise, raise a :class:`TypeError`.
    """
    try:
        if x.dimensionless:
            return x._value
    except AttributeError:
        return x
    raise TypeError("The quantity is not dimensionless.")


def display(quantity):
    """Return the display unit of *quantity*.

    If *quantity* does not have a :attr:`~DimensionedObject.display`
    property, then an empty :class:`CompoundUnit` is returned.

    **Example:**

    >>> from natu.units import m
    >>> print(display(100*m))
    m
    """
    try:
        return quantity.display
    except AttributeError:
        return CompoundUnit()

def merge(value, prototype):
    """Merge *value* into a new :class:`Quantity` with the properties
    (:attr:`~Quantity.dimension` and :attr:`~Quantity.display`) of
    *prototype*.

    If *prototype* is not a :class:`~natu.core.Quantity`, then *value* is
    returned directly---as a quantity.

    **Example:**

    >>> from natu.units import m, km
    >>> from natu.core import merge
    >>> merge(value(1000*m), km)
    Quantity(1000, 'L', 'km') (1.0 km)
    """
    try:
        return Quantity(value, prototype.dimension, prototype.display)
    except AttributeError:
        return value


def prohibited(self, other):
    """Not allowed; raises a TypeError"""
    # pylint: disable=I0011, W0613
    raise TypeError("In-pace assignments aren't allowed for units.")


def quantity_only(operation):
    """Return a method that raises a :class:`TypeError` with a message
    pertinent to :class:`LambdaUnit`.
    """

    def prohibited(self, other):
        """Not allowed; raises a TypeError"""
        # pylint: disable=W0613
        raise TypeError(operation.capitalize() + " is only allowed for "
                        "quantities.  Use the lambda unit to generate a "
                        "quantity first.")
    return prohibited

def _times(code):
    """Return a string representing multiplication, depending on the format
    code.
    """
    if code == 'H':
        return '&nbsp;'
    if code == 'L':
        return '\,'
    return ' '

def value(x):
    """Return the :attr:`_value` attribute of *x* if it exists.

    Otherwise, return *x* directly (pass-through).

    **Example:**

    >>> from natu.units import m
    >>> value(10*m) # doctest: +SKIP
    10

    .. testcleanup::
       >>> assert abs(value(10*m) - 10) < 1e-10
    """
    try:
        return x._value
    except AttributeError:
        return x

# Decorators
# ----------


def add_unit(meth):
    """Decorate a function to add a unit to the formatted representation.
    """
    @wraps(meth)
    def wrapped(self, code):
        # Get the display unit.
        self.display = Quantity.unitspace.simplify(self.display)
        unit = Quantity.unitspace(**self.display)
        unit_dim = dimension(unit)
        assert self.dimension == unit_dim, (
            "The display unit ({0.display}; dimension {1}) and the quantity "
            "(dimension {0.dimension}) are incompatible.").format(self,
                                                                  unit_dim)

        # Parse the format code.
        number_code, unit_code = split_code(code)

        # Create the unit string.
        unit_str = format(self.display, unit_code)
        try:
            for rpl in UNIT_REPLACEMENTS[unit_code]:
                unit_str = rpl[0].sub(rpl[1], unit_str)
        except KeyError:
            pass

        return meth(self / unit, number_code, unit_code) + unit_str

    return wrapped


def as_scalarunit(meth):
    """Decorate *meth* so that it returns a :class:`ScalarUnit` if both
    arguments are :class:`ScalarUnit` instances and the result is not
    dimensionless.
    """
    @wraps(meth)
    def wrapped(self, other):
        result = meth(self, other)
        if isinstance(other, ScalarUnit) and isinstance(result, Quantity):
            return ScalarUnit(result._value, result._dimension, result._display)
        return result

    return wrapped


def copy_props(func):
    """Decorate a function to return a :class:`~natu.core.Quantity` that
    matches the first argument except for the computed value.
    """
    @wraps(func)
    def wrapped(x, y):
        return merge(func(x, y), x)

    wrapped.__doc__ += (
        "\nThe :attr:`dimension` and :attr:`display` properties of the first "
        "\nterm are propagated to the result.\n")
    return wrapped


def homogeneous(func):
    """Decorate a function to accept quantities of the same dimension.
    """
    @wraps(func)
    def wrapped(x, y):
        assert_homogeneous(x, y)
        return func(value(x), value(y))

    wrapped.__doc__ += (
        "\nThe terms must have the same dimension.  A quantity can only be "
        "\nadded to, compared to, or subtracted from a non-quantity if the "
        "\nquantity is dimensionless.\n")
    return wrapped


# Classes
# -------

class DefinitionError(Exception):

    """Error in the definition of a unit or constant in an INI file
    """
    pass

class CompoundDimension(Exponents):

    """Dictionary that contains base physical dimensions as keys and
    exponents of those dimensions as values

    This is :class:`natu.exponents.Exponents`---only extended and renamed
    for clarity.  Please see that class for details.

    **Example:**

    >>> dim = CompoundDimension('L/T')*2
    >>> dim
    CompoundDimension({'L': 2, 'T': -2})
    >>> print(dim)
    L2/T2
    """
    # pylint: disable=I0011, R0904
    pass


class CompoundUnit(Exponents):

    """Dictionary that contains the base units of a display unit as keys
    and exponents of those units as values

    This is :class:`natu.exponents.Exponents`---only extended and renamed
    for clarity. Please see that class for details.

    **Example:**

    >>> unit = CompoundUnit('m/s')*2
    >>> unit
    CompoundUnit({'m': 2, 's': -2})
    >>> print(unit)
    m2/s2
    """
    # pylint: disable=I0011, R0904
    pass

# Note that in the DimensionedObject below, dimension and display are properties
# that return copies of the internal _dimension and _display attributes.
# Generally, only dimension and display should be accessed from the outside to
# prevent mutating the internal _dimension and _display dictionaries.  However,
# in the code below, this rule is strategically broken to avoid the overhead of
# making copies.


class DimensionedObject(object):

    """Base type that tracks physical dimension and display unit

    **Initialization arguments:**

    - *dimension*: Physical dimension

         This can be a :class:`CompoundDimension` instance, a standard
         Python_ dictionary (:class:`dict`) of the same form, or a string
         following the syntax described in
         :meth:`~natu.exponents.Exponents.fromstr`.

    - *display*: Display unit

         This can be a :class:`CompoundUnit` instance, a standard Python_
         dictionary (:class:`dict`) of the same form, or a string
         following the syntax described in
         :meth:`~natu.exponents.Exponents.fromstr`.

    Here, the physical dimension and the display unit are not checked for
    consistency.
    """

    def __init__(self, dimension, display):
        """Initialize by setting the physical dimension and display unit.

        See the top-level class documentation.
        """
        self._dimension = CompoundDimension(dimension)
        self._display = CompoundUnit(display)

    @property
    def dimension(self):
        """Physical dimension"""
        return self._dimension.copy()

    @property
    def dimensionless(self):
        """*True* if the instance is dimensionless"""
        return not self._dimension

    @property
    def display(self):
        """Display unit"""
        return self._display.copy()

    @display.setter
    def display(self, display):
        """Set the display unit.

        *display* can be a :class:`CompoundUnit` instance, a standard
        Python_ dictionary (:class:`dict`) of the same form, or a string
        following the syntax described in
        :meth:`~natu.exponents.Exponents.fromstr`.

        Here, the display unit is not checked for dimensional consistency
        (with :attr:`dimension`).
        """
        self._display = CompoundUnit(display)


class Quantity(DimensionedObject):

    """Class to represent a physical quantity

    **Initialization arguments:**

    - *value*: Value of the quantity (a :class:`numbers.Number` instance)

         This can be expressed as the product of a number and the value of
         a unit.  The value of a quantity is independent of the unit; the
         number scales inversely to the unit.

    - *dimension*: Physical dimension

         This can be a :class:`CompoundDimension` instance, a standard
         Python_ dictionary (:class:`dict`) of the same form, or a string
         following the syntax described in
         :meth:`~natu.exponents.Exponents.fromstr`.

    - *display*: Display unit

         This can be a :class:`CompoundUnit` instance, a standard Python_
         dictionary (:class:`dict`) of the same form, or a string
         following the syntax described in
         :meth:`~natu.exponents.Exponents.fromstr`.

    **Properties:**

    - :attr:`dimension`: Physical dimension as a
      :class:`CompoundDimension`

    - :attr:`dimensionless`: *True* if the quantity is dimensionless

    - :attr:`display`: Display unit as a :class:`CompoundUnit`

    :attr:`dimension` and :attr:`dimensionless` are read-only, but
    :attr:`display` can be set using the same options as the *display*
    argument above.

    **Examples:**

    Instantiation and simple operations:

    >>> import natu.units
    >>> mass = Quantity(1, 'M', 'kg')
    >>> velocity = Quantity(1, 'L/T', 'm/s')
    >>> energy = mass*velocity**2
    >>> print(energy.dimension)
    L2*M/T2
    >>> print(energy.display)
    kg*m2/s2

    However, it is easier to create a quantity as the product of a number
    and unit(s); see :mod:`natu.units`.

    Changing the display unit:

    >>> mass.display = 'lb'
    >>> print(mass) # doctest: +ELLIPSIS
    2.20462... lb

    Note that the value is unchanged:

    >>> mass # doctest: +ELLIPSIS
    Quantity(1, 'M', 'lb') (2.20462... lb)

    Although the :attr:`display` property can be changed, quantities are
    otherwise immutable.  The in-place operators create new instances:

    >>> initial_id = id(velocity)
    >>> velocity *= 0.5
    >>> id(velocity) == initial_id
    False


    .. _Python: https://www.python.org/
    """

    unitspace = None

    def __init__(self, value, dimension, display=''):
        """Initialize a quantity by setting the value, physical dimension,
        and display unit.

        See the top-level class documentation.
        """
        # Set the value.
        self._value = value

        # Set the dimension and display unit.
        DimensionedObject.__init__(self, dimension, display)

    @copy_props
    @homogeneous
    def __add__(x, y):
        """x.__add__(y) <==> x + y
        """
        return x + y

    def __radd__(x, y):
        """x.__radd__(y) <==> y + x
        """
        return y + dimensionless_value(x)

    @copy_props
    @homogeneous
    def __sub__(x, y):
        """x.__sub__(y) <==> x - y
        """
        return x - y

    def __rsub__(x, y):
        """x.__add__(y) <==> y - x
        """
        return y - dimensionless_value(x)

    def __neg__(x):
        """x.__neg__() <==> -x
        """
        return merge(-x._value, x)

    def __pos__(x):
        """x.__pos__() <==> x
        """
        return x

    def __mul__(x, y):
        """x.__mul__(y) <==> x*y
        """
        try:
            value = y._value * x._value
        except AttributeError:
            if isinstance(y, DimensionedObject):
                return NotImplemented  # Defer; y could be a LambdaUnit.
            return Quantity(y * x._value, x.dimension, x.display)
        dimension = y._dimension + x._dimension
        if dimension:
            return Quantity(value, dimension, y._display + x._display)
        return value

    __rmul__ = __mul__

    def __truediv__(x, y):
        """x.__truediv__(y) <==> x/y
        """
        try:
            value = x._value / y._value
        except AttributeError:
            if isinstance(y, DimensionedObject):
                return NotImplemented  # Defer; y could be a LambdaUnit.
            return Quantity(x._value / y, x.dimension, x.display)
        dimension = x._dimension - y._dimension
        if dimension:
            return Quantity(value, dimension, x._display - y._display)
        return value

    __div__ = __truediv__

    def __rtruediv__(x, y):
        """x.__rtruediv__(y) <==> y/x
        """
        try:
            value = y._value / x._value
        except AttributeError:
            return Quantity(y / x._value, -x._dimension, -x._display)
        dimension = y._dimension - x._dimension
        if dimension:
            return Quantity(value, dimension, y._display - x._display)
        return value

    __rdiv__ = __rtruediv__

    def __pow__(x, y):
        """x.__pow__(y) <==> pow(x, y)

        Only the 2-argument version of :func:`pow` is supported since the
        value of a quantity is not generally an integer.
        """
        if y == 0:
            return 1
        try:
            y = dimensionless_value(y)
        except TypeError:
            raise TypeError("The exponent must be dimensionless.")
        except AttributeError:
            pass
        return x.__class__(x._value ** y, x._dimension * y, x._display * y)

    def __rpow__(x, y):
        """y.__pow__(x) <==> pow(x, y)

        This is only implemented for dimensionless quantities.

        Only the two-argument version of :func:`pow` is supported since
        the value of a quantity is not generally an integer.
        """
        if x.dimensionless:
            return y ** x._value
        raise TypeError("The exponent must be dimensionless.")

    @add_unit
    def __format__(number, number_code, unit_code):
        """Format the quantity as a string according to *code*.
        """
        number_str = format_e(format(number, number_code), unit_code)
        return number_str + _times(unit_code)

    def __str__(self):
        """Return a string representing the quantity as the product of a
        number and a unit.

        **Example:**

        >>> from natu.units import *
        >>> print(1*m)
        1.0 m
        """
        return format(self)

    def __repr__(self):
        """Return a formal string representation of the quantity.

        The first part (``Quantity(...)``) is the expression that would
        generate the quantity.  The part in the last parentheses is the
        value as the generalized product of a number and a unit.

        **Example:**

        >>> from natu.units import *
        >>> 1*m
        Quantity(1, 'L', 'm') (1.0 m)
        """
        # Run this first to simplify self.display:
        string = format(self)

        return ("Quantity({0._value:g}, '{0._dimension}', '{0._display}') "
                "({1})").format(self, string)

    def __int__(self):
        """Return the quantity as an integer.

        This is only possible if the quantity is dimensionless.
        """
        return int(dimensionless_value(self))

    def __float__(self):
        """Return the quantity as a float.

        This is only possible if the quantity is dimensionless.
        """
        return float(dimensionless_value(self))

    def __trunc__(self):
        """Return the :class:`numbers.Real` value *x* truncated to an
        :class:`numbers.Integral` (usually a long integer).

        This method is used by :func:`natu.math.trunc` and relies on
        :func:`math.trunc`.
        """
        return math.trunc(float(self))

    def __abs__(self):
        """x.__abs__() <==> abs(x)
        """
        return merge(abs(self._value), self)

    def __eq__(x, y):
        """x.__eq__(y) <==> x==y
        To be considered equal, it is not necessary that quantities have
        the same display unit (:attr:`display`)---only the same value and
        dimension.
        """
        try:
            return (x._dimension == y._dimension and
                    x._value == y._value)
        except AttributeError:
            return x.dimensionless and x._value == y

    def __ne__(x, y):
        """x.__ne__(y) <==> x!=y

        To be considered equal, it is not necessary that quantities have
        the same display unit (:attr:`display`)---only the same value and
        dimension.  A quantity is equal to zero if its value is zero,
        regardless of dimension.
        """
        try:
            return (x._dimension != y._dimension or
                    x._value != y._value)
        except AttributeError:
            return not x.dimensionless or x._value != y

    def __bool__(self):
        """self != 0
        """
        return self._value != 0

    __nonzero__ = __bool__  # For Python2

    @homogeneous
    def __ge__(x, y):
        """x.__ge__(y) <==> x>=y
        """
        return x >= y

    @homogeneous
    def __le__(x, y):
        """x.__le__(y) <==> x<=y
        """
        return x <= y

    @homogeneous
    def __gt__(x, y):
        """x.__gt__(y) <==> x>y
        """
        return x > y

    @homogeneous
    def __lt__(x, y):
        """x.__lt__(y) <==> x<y
        """
        return x < y

    @homogeneous
    def __divmod__(x, y):
        """x.__divmod__(y) <==> divmod(x, y)
        """
        return x // y, x % y

    @homogeneous
    def __rdivmod__(x, y):
        """x.__rdivmod__(y) <==> divmod(y, x)
        """
        return y // x, y % x

    @homogeneous
    def __floordiv__(x, y):
        """x.__floordiv__(y) <==> x//y
        """
        return x // y

    @homogeneous
    def __rfloordiv__(x, y):
        """x.__rfloordiv__(y) <==> y//x
        """
        return y // x

    @homogeneous
    def __mod__(x, y):
        """x.__mod__(y) <==> x%y
        """
        return x % y

    @homogeneous
    def __rmod__(x, y):
        """x.__mod__(y) <==> y%x
        """
        return y % x


class Unit(DimensionedObject):

    """Base class for a unit

    In-place assignments are blocked because the value of a unit is
    predefined and should not be changed.
    """

    def __init__(self, dimension, display, prefixable=False):
        """Initialize by setting the dimension, display unit, and
        prefixable flag.

        See the top-level class documentation.
        """
        DimensionedObject.__init__(self, dimension, display)
        self._prefixable = prefixable

    @property
    def prefixable(self):
        """*True* if the unit can be prefixed

        **Example:**

        >>> from natu.units import m, ft
        >>> m.prefixable
        True
        >>> ft.prefixable
        False
        """
        return self._prefixable

    # No in-place operations
    __iadd__ = prohibited
    __idiv__ = prohibited
    __ifloordiv__ = prohibited
    __imul__ = prohibited
    __ipow__ = prohibited
    __isub__ = prohibited
    __itruediv__ = prohibited


class ScalarUnit(Quantity, Unit):

    """Unit that involves just a scaling factor

    **Initialization arguments:**

    - *value*: Value of the quantity (a :class:`numbers.Number` instance)

         This can be expressed as the product of a number and the value of
         a unit.  A value of a quantity is independent of the unit; the
         number scales inversely to the unit.

    - *dimension*: Physical dimension

         This can be a :class:`CompoundDimension` instance, a standard
         Python_ dictionary (:class:`dict`) of the same form, or a string
         following the syntax described in
         :meth:`~natu.exponents.Exponents.fromstr`.

    - *display*: Display unit

         This can be a :class:`CompoundUnit` instance, a standard Python_
         dictionary (:class:`dict`) of the same form, or a string
         following the syntax described in
         :meth:`~natu.exponents.Exponents.fromstr`.

    - *prefixable*: *True* if the unit can be prefixed

    **Properties:**

    - :attr:`dimension`: Physical dimension as a
      :class:`CompoundDimension`

    - :attr:`dimensionless`: *True* if the quantity is dimensionless

    - :attr:`display`: Display unit as a :class:`CompoundUnit`

    - :attr:`prefixable`: *True* if the unit can be prefixed

    :attr:`dimension`, :attr:`dimensionless`, and :attr:`prefixable` are
    read-only, but :attr:`display` can be set using the same options as
    the *display* argument above.

    **Examples:**

    >>> from natu.units import kg, m, s
    >>> # F
    >>> kg
    ScalarUnit(1, 'M', 'kg', False) (kg)
    >>> kg*m**2/s**2
    ScalarUnit(1, 'L2*M/T2', 'J', False) (J)

    Note that it's possible to change the display unit:

    >>> m.display = 'ft'
    >>> m # doctest: +ELLIPSIS
    ScalarUnit(1, 'L', 'ft', True) (3.2808... ft)

    .. testcleanup::
       >>> m.display = 'm'

    Now any quantity generated from m will display in ft instead.
    However, notice that the value is unchanged; m still represents the
    same length.
    """

    def __init__(self, value, dimension, display='', prefixable=False):
        """Initialize a scalar unit by setting the value, physical
        dimension, display unit, and prefixable flag.

        See the top-level class documentation.
        """
        # pylint: disable=I0011, W0231

        # Set the value.
        self._value = value

        # Set the dimension, display unit, and prefixable flag.
        Unit.__init__(self, dimension, display, prefixable)

    @classmethod
    def fromQuantity(cls, quantity, display, prefixable=False):
        """Convert a quantity (instance of :class:`Quantity`) to a scalar
        unit.

        The value and dimension are taken from *quantity*.  The display
        unit must be provided (via *display*).

        **Example:**

        >>> from natu.units import ns
        >>> shake = ScalarUnit.fromQuantity(10*ns, 'shake')

        .. testcleanup::
           >>> from natu import units
           >>> units.shake = shake
           >>> shake
           ScalarUnit(1e-08, 'T', 'shake', False) (shake)
        """
        quantity.__class__ = cls
        quantity.display = display
        quantity._prefixable = prefixable
        return quantity

    def __repr__(self):
        """Return a formal string representation of the scalar unit.

        The first part (``ScalarUnit(...)``) is the expression that would
        generated the unit.  The part in the last parentheses is the
        value as the product of a number and a unit.
        """
        # Run this first to simplify self.display (see Units.load_ini):
        string = format(self)

        return ("ScalarUnit({0._value:g}, '{0._dimension}', '{0._display}', "
                "{0._prefixable}) ({1})").format(self, string)

    @as_scalarunit
    def __mul__(x, y):
        """x.__mul__(y) <==> x*y
        """
        return Quantity.__mul__(x, y)

    __rmul__ = __mul__

    @as_scalarunit
    def __truediv__(x, y):
        """x.__truediv__(y) <==> x/y
        """
        return Quantity.__truediv__(x, y)

    __div__ = __truediv__

    @as_scalarunit
    def __rtruediv__(x, y):
        """x.__truediv__(y) <==> x/y
        """
        return Quantity.__rtruediv__(x, y)

    __rdiv__ = __rtruediv__

    @add_unit
    def __format__(number, number_code, unit_code):
        """Format the scalar unit as a string according to *code*.
        """

        TOLERANCE = 1e-14
        if abs(number - 1) < TOLERANCE:
            # Exclude the number since it's nearly 1.
            return ''
        else:
            number_str = format_e(format(number, number_code), unit_code)
            return number_str + _times(unit_code)


class LambdaUnit(Unit):

    """Unit that involves a offset or other operations besides scaling

    **Initialization arguments:**

    - *toquantity*: Function that maps a number to a quantity

    - *tonumber*: Function that maps a quantity to a number

    - *dimension*: Physical dimension

         This can be a :class:`CompoundDimension` instance, a standard
         Python_ dictionary (:class:`dict`) of the same form, or a string
         following the syntax described in
         :meth:`~natu.exponents.Exponents.fromstr`.

    - *display*: Display unit

         This can be a :class:`CompoundUnit` instance, a standard Python_
         dictionary (:class:`dict`) of the same form, or a string
         following the syntax described in
         :meth:`~natu.exponents.Exponents.fromstr`.

    - *prefixable*: *True* if the unit can be prefixed

    **Properties:**

    - :attr:`dimension`: Physical dimension as a
      :class:`CompoundDimension`

    - :attr:`dimensionless`: *True* if the quantity is dimensionless

    - :attr:`display`: Display unit as a :class:`CompoundUnit`

    - :attr:`prefixable`: *True* if the unit can be prefixed

    :attr:`dimension`, :attr:`dimensionless`, and :attr:`prefixable` are
    read-only, but :attr:`display` can be set using the same options as
    the *display* argument above.

    **Examples:**

    >>> from natu.units import degC, K
    >>> degC # doctest: +ELLIPSIS
    LambdaUnit(...)
    >>> 25*degC/K
    298.15
    """

    def __init__(self, toquantity, tonumber, dimension, display='',
                 prefixable=False):
        """Initialize a lambda unit by setting the function and its
        inverse, physical dimension, display unit, and prefixable flag.

        See the top-level class documentation.
        """
        # pylint: disable=I0011, R0913
        # Set the methods that map a number to a quantity and vice versa.
        self._toquantity = toquantity
        self._tonumber = tonumber

        # Set the dimension, display unit, and prefixable flag.
        Unit.__init__(self, dimension, display, prefixable)

    def __repr__(self):
        """Return a formal string representation of the lambda unit.

        The first part (``ScalarUnit(...)``) is the expression that would
        generated the unit.  The part in the last parentheses is the
        value as a number and a unit.
        """
        return ("LambdaUnit({0._tonumber}, {0._toquantity}, '{0._dimension}', "
                "'{0._display}', {0._prefixable})").format(self)

    def __str__(self):
        """Return an informal string represention of the lambda unit.
        """
        note = ("dimensionless LambdaUnit" if self.dimensionless else
                "LambdaUnit with dimension " + self._dimension)
        display_note = "displays as %s" % self._display
        prefixable_note = "prefixable" if self._prefixable else "not prefixable"
        return "; ".join([note, display_note, prefixable_note])

    def __pow__(x, y):
        """x.__pow__(y) <==> pow(x, y)

        Only the 2-argument version of :func:`pow` is supported.  In
        addition, y must be 1, 0, or -1.  With y=1, the result is the
        lambda unit itself.  With y=0, the result is 1 (unity).  With
        y=-1, the result is the inverse of the lambda unit.
        """
        if y == 1:
            return x
        if y == 0:
            return 1
        if y == -1:
            return LambdaUnit(x._tonumber, x._toquantity,  # Swapped
                              -x._dimension, -x._display)
        raise TypeError("Lambda units can only be raised to the power of -1, "
                        "0, or 1.")

    def __rmul__(unit, number):
        """unit.__rmul__(number) <==> number*unit
        """
        display = unit.display
        if isinstance(number, Quantity):
            assert number.dimensionless, ("The argument to the lambda unit "
                                          "must be dimensionless.")
            display += number.display
            as_quantity = False
        else:
            as_quantity = bool(display)
        try:
            quantity = unit._toquantity(number)
        except AssertionError:
            raise AssertionError("The number isn't a valid argument for the "
                                 "lambda unit.")
        if isinstance(quantity, Quantity):
            quantity.display = display
            return quantity
        elif as_quantity:
            return Quantity(quantity, {}, display)
        return quantity

    def __rtruediv__(unit, quantity):
        """unit.__rtruediv__(quantity) <==> quantity/unit
        """
        display = -unit._display
        if isinstance(quantity, Quantity):
            display += quantity.display
            as_quantity = False
        else:
            as_quantity = display and unit.dimensionless
        try:
            number = unit._tonumber(quantity)
        except AssertionError:
            raise AssertionError("The quantity isn't a valid argument for the "
                                 "inverse of the lambda unit.")
        if isinstance(number, Quantity):
            assert number.dimensionless, ("The result of the inverse of the "
                                          "lambda unit should be "
                                          "dimensionless.")
            number.display = display
            return number
        elif as_quantity:
            # E.g., keep unit of B-1 when doing 1/B but not unit of K/degC when
            # doing 300*K/degC.
            return Quantity(number, {}, display)
        return number

    __rdiv__ = __rtruediv__

    # Provide helpful messages for the unsupported methods (that are supported
    # by Quantity).
    def __mul__(self, other):
        """Not supported
        """
        # pylint: disable=I0011, R0201
        raise AttributeError("The lambda unit can only be used on the right "
                             "side of a product.")

    def __truediv__(self, other):
        """Not supported
        """
        # pylint: disable=R0201, W0613
        raise AttributeError("The lambda unit can only be used as the "
                             "denominator of a quotient.")

    __div__ = __truediv__

    # Addition, etc.
    __add__ = quantity_only('Addition')
    __radd__ = quantity_only('Addition')
    __pos__ = quantity_only('The positive operator')
    # Subtraction, etc.
    __sub__ = quantity_only('Subtraction')
    __rsub__ = quantity_only('Subtraction')
    __neg__ = quantity_only('Negation')
    # Exponentiation
    __rpow__ = quantity_only('Exponentiation')
    # Modulo
    __mod__ = quantity_only('The modulo operator')
    __rmod__ = quantity_only('The modulo operator')
    # Division modulo
    __divmod__ = quantity_only('Division modulo')
    __rdivmod__ = quantity_only('Division modulo')
    # Floor division
    __floordiv__ = quantity_only('Floor division')
    __rfloordiv__ = quantity_only('Floor division')
    # Comparison
    __cmp__ = quantity_only('Comparison')
    __ge__ = quantity_only('Comparison')
    __gt__ = quantity_only('Comparison')
    __le__ = quantity_only('Comparison')
    __lt__ = quantity_only('Comparison')
    __nonzero__ = quantity_only('Comparison')
    # Other
    __abs__ = quantity_only('Absolute value')


class CoherentRelations(list):

    """List of coherent relations among units

    Each item is a tuple consisting of a relation and a set of the
    dimensions involved in the units of the relation.  Each relation is
    expressed as a :class:`CompoundUnit` instance that resolves to unity.
    """
    pass


class Units(dict):

    """Dictionary of units with dynamic prefixing (upon access)
    """

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

        # Initialize an empty list of coherent relations.
        self.coherent_relations = CoherentRelations()

    def __getitem__(self, symbol):
        """Access a unit by *symbol* (a string).

        Prefixes are supported.
        """
        try:
            return dict.__getitem__(self, symbol)  # Standard unit
        except KeyError:
            pass  # Prefixed unit (below)

        # Default error:
        error = KeyError(symbol + " isn't a valid unit.")

        # Try prefixes.
        for len_prefix in [1, 2]:  # A prefix may have 1 or 2 characters.
            try:
                basesymbol = symbol[len_prefix:]
                baseunit = dict.__getitem__(self, basesymbol)
            except IndexError:
                # The unit isn't longer than the length of the prefix.
                raise error
            except KeyError:
                # The base symbol isn't a valid unit; try a longer prefix.
                continue
            prefix = symbol[:len_prefix]
            try:
                p = PREFIXES[prefix]
            except KeyError:
                if not use_quantities or baseunit.prefixable:
                    error = KeyError(prefix + " isn't a valid prefix.")
            else:
                if not use_quantities or baseunit.prefixable:
                    if isinstance(baseunit, ScalarUnit):
                        return ScalarUnit(p * baseunit._value,
                                          baseunit.dimension, symbol)
                    if isinstance(baseunit, LambdaUnit):
                        return LambdaUnit(lambda n: baseunit._toquantity(p * n),
                                          lambda q: baseunit._tonumber(q) / p,
                                          baseunit.dimension, symbol)
                    return p * baseunit
                error = KeyError(basesymbol + " isn't prefixable.")
        raise error

    def __call__(self, **factors):
        r"""Generate a compound unit from the unit space.

        **Arguments:**

        - *\*\*factors*: Factors of the compound unit

          The factors are expressed as keyword arguments where the keys
          are unit symbols and the values are exponents.

        **Example:**

        >>> from natu.units import _units
        >>> _units(lbf=1, inch=-2)
        ScalarUnit(6894.76, 'M/(L*T2)', 'psi', False) (psi)

        Here, the unit was automatically simplified to psi using
        :attr:`_units.coherent_relations`.
        """
        factors = [
            self[base] ** exponent for base, exponent in factors.items()]
        return product(factors)

    def load_ini(self, files):
        r"""Add units to the unit dictionary from a \*.ini file or list of
        files (*files*).

        **Examples:**

        .. code-block:: python

           >>> from natu.core import Units
           >>> from natu.config import definitions

           >>> units = Units()
           >>> units.load_ini([definitions[0]])
           >>> units.keys() # doctest: +SKIP
           ['R', 'R_K', 'R_inf', 'c', 'k_Aprime', 'k_F', 'k_J', 'rational']

        .. testcleanup::

           >>> sorted(units.keys())
           ['R', 'R_K', 'R_inf', 'c', 'k_Aprime', 'k_F', 'k_J', 'rational']
        """
        # pylint: disable=I0011, R0912, R0914

        # Temporarily add some constants, functions, classes, etc. to the unit
        # space for use in the *.ini files.
        # TODO: Avoid this cyclic import:
        from fractions import Fraction
        sqrt = lambda x: x**Fraction(0.5)
        provided = dict(pi=math.pi, exp=math.exp, log=math.log,
                        log10=math.log10, sqrt=sqrt, Quantity=Quantity,
                        ScalarUnit=ScalarUnit)
        self.update(provided)

        # Load the units from the *.ini files.
        try:
            config = RawConfigParser(interpolation=None,
                                     inline_comment_prefixes=[';'])
        except TypeError:
            config = RawConfigParser()
        config.optionxform = str  # Units are case sensitive.
        if len(config.read(files)) != len(files):
            raise DefinitionError("Failed to open/find all definition files")
        for section in config.sections():
            for symbol, value in config.items(section):
                # print(symbol)
                if symbol in self:
                    msg = ('In section "%s", overriding previous value of %s'
                           % (section, symbol))
                    # warn(msg)
                    print(msg)
                try:
                    unit = eval(value, self, self)
                    # self is provided as the global namespace as well so that it's
                    # immediately used by the lambda functions.  This doesn't allow
                    # prefixes in the lambda expressions  since eval() doesn't use
                    # __getitem__() for globals.
                    # TODO: Consider using pyparsing instead of eval() (for safety,
                    # if it isn't too slow).
                    if isinstance(unit, tuple):
                        unit, prefixable = unit
                        if isinstance(unit, tuple):
                            # The unit is a lambda unit, defined via a tuple.
                            toquantity, tonumber = unit
                            try:
                                # Evaluate the unit with an arbitrary number (zero)
                                # to determine the dimension.
                                dim = toquantity(0).dimension
                            except AttributeError:
                                # The result doesn't have a dimension; the unit must
                                # be dimensionless.
                                dim = {}
                            unit = LambdaUnit(toquantity, tonumber, dim, symbol,
                                              prefixable)
                        elif isinstance(unit, LambdaUnit):
                            # The unit is a lambda unit, defined directly.
                            unit = LambdaUnit(unit._toquantity, unit._tonumber,
                                              unit._dimension, unit._display,
                                              prefixable)
                        elif isinstance(unit, Quantity):
                            # The unit should be a scalar unit.
                            if isinstance(unit, ScalarUnit) \
                                    and 'ScalarUnit' not in value:
                                dimensions = set(unit.dimension)
                                for u in unit.display.keys():
                                    dimensions = dimensions.union(
                                        self[u].dimension)
                                relation = (unit.display - {symbol: 1}, dimensions)
                                self.coherent_relations.append(relation)
                            unit = ScalarUnit.fromQuantity(
                                unit, symbol, prefixable)
                        else:
                            # The unit is dimensionless.
                            unit = ScalarUnit(unit, {}, symbol, prefixable)
                except (AssertionError, AttributeError, ConfigParserError,
                        NameError, SyntaxError, TypeError, ValueError) as e:
                    raise DefinitionError("can't load '%s' due to %s"
                                          % (symbol, type(e).__name__))
                if isinstance(unit, Quantity) and not use_quantities:
                    # Represent quantities (including scalar units) as pure
                    # numbers.
                    unit = unit._value
                self[symbol] = unit

        # Remove the temporary items.
        for key in provided.keys():
            del self[key]
        # __builtins__ was added because self is the global arg to eval()
        # above.
        self.pop('__builtins__', None)

    def simplify(self, unit, level=simplification_level):
        r"""Simplify a compound unit.

        This function seeks to minimize the sum of the absolute values of
        the exponents of the base factors.  It avoids using any factors
        that involve dimensions not included in the original
        representation of the unit.  This function uses the internal
        :attr:`coherent_relations` list which is generated while parsing
        the \*.ini files (in :meth:`load_ini`).  It will not always find
        the simplest representation because some simplifications involve
        first making the representation more complex.

        **Arguments:**

        - *unit*: Unit to be simplified

             This can be a :class:`CompoundUnit` instance, a standard
             Python_ dictionary (:class:`dict`) of the same form, or a
             string following the syntax described in
             :meth:`~natu.exponents.Exponents.fromstr`.

        - *level*: Number of levels of recursion to perform

             This is the number of non-minimizing substitutions that can
             be made in seeking the best representation of the unit.

        **Returns:**  A :class:`CompoundUnit` instance indicating the best
        representation of the unit.

        **Example:**

        >>> # High-level:
        >>> from natu.units import *
        >>> print(kg*m**2/s**2)
        J

        >>> # Low-level:
        >>> from natu.units import _units
        >>> print(_units.simplify('kg*m2/s2'))
        J
        """
        # pylint: disable=I0011, E1103

        # Objective to minimize
        complexity = lambda x: sum(abs(exp) for exp in x.values())
        # This is the L1 norm (sum of the absolute values of the exponents),
        # making this problem L1 minimization.  There isn't a simple solution,
        # and there isn't a simple Python package to find it without a lot of
        # dependencies (as of 6/29/14).  The closest packages are scipy.linalg,
        # L1L2Py, and pyl1min (http://sourceforge.net/projects/pyl1min/).  The
        # approach below is more or less brute force.  It isn't guaranteed to
        # find the best solution, but it's straightforward to implement and
        # works well enough.

        # In case unit is a string:
        unit = CompoundUnit(unit)

        # Shortcut---no simplication:
        if level == 0 or complexity(unit) <= 1:
            return unit

        # Set of dimensions involved in the unit:
        dimensions = set(self(**unit).dimension)

        # Loop to try each of the coherent relations that involve a subset of
        # the dimensions of the unit.
        simpler = True
        while simpler:
            simpler = False
            for identity, dim in self.coherent_relations:
                # if not dim.issubset(dimensions):
                    # Skip; the relation involves different dimensions.
                #     continue
                common = set(identity).intersection(unit)
                if len(common) < len(identity) / 2 - 0.5:
                    # Skip for speed; the relation isn't worth it.
                    continue
                for factor in common:
                    factor = float(unit[factor]) / identity[factor]
                    int_factor = int(factor)
                    if int_factor == factor:
                        temp = unit - identity * int_factor
                        if level > 1:
                            temp = self.simplify(temp, level - 1)  # Recursion
                        if complexity(temp) < complexity(unit):
                            unit = temp
                            simpler = True
                            break
        return unit


class UnitsModule(ModuleType):

    r"""Class that wraps the :class:`Units` dictionary as a module

    **Initialization arguments:**

    - *module*: The module into which the units should be wrapped

         This must have the attributes :attr:`__name__` and
         :attr:`__doc__`.

    - *definitions*: A \*.ini file, list of files, or dictionary with
      units that should be inserted into the module

         It is not necessary to provide prefixed versions of the units
         unless they should be available via
         ``from <units module> import *``.

    Only one :class:`UnitsModule` can be instantiated from \*.ini files
    per Python session.  This prevents conflicts that might arise if the
    units were reloaded with different base constants.
    """

    def __init__(self, module, definitions):
        r"""Initialize the module with meta attributes matching those of
        *module* and units and constants from a \*.ini file or list of
        files (*definitions*).
        """
        # pylint: disable=I0011, E1002, W0233

        # Copy attributes from the original module.
        super(UnitsModule, self).__init__(module.__name__, module.__doc__)
        for attr in ['__author__', '__email__', '__copyright__', '__license__',
                     '__file__', '__package__']:
            try:
                setattr(self, attr, getattr(module, attr))
            except AttributeError:
                pass
        self.__path__ = dirname(self.__name__)  # Necessary in Python3; why?

        # Load the units.
        if isinstance(definitions, dict):
            # Create a unit dictionary from a provided dictionary.
            self._units = Units(definitions)
        else:
            # Create an empty unit dictionary.
            self._units = Units()

            # Monkey-patch the Quantity class to use only that unit dictionary.
            assert not Quantity.unitspace, (
                "The units module can only be loaded once.")
            Quantity.unitspace = self._units

            # Load units from the ini files.
            try:
                self._units.load_ini(definitions)
            except (DefinitionError, ParsingError):
                # Allow the user to fix the INI files and try to import again.
                Quantity.unitspace = None
                raise

        self.__all__ = list(self._units)

    def __getattr__(self, name):
        """Return a unit or attribute matching *name* (a string).

        Prefixes are accepted on prefixable units.
        """
        try:
            return self._units[name]
        except KeyError:
            try:
                return getattr(self._units, name)
            except AttributeError:
                raise AttributeError(name + " isn't a valid unit or attribute")

    def __setattr__(self, name, value):
        """Set an attribute (*name*) to a value (*value*).

        If *value* is a :class:`DimensionedObject`, it is added to the
        internal units dictionary (:attr:`_units`).  Otherwise, it is
        added as a standard attribute.
        """
        if isinstance(value, DimensionedObject):
            self._units[name] = value
        else:
            ModuleType.__setattr__(self, name, value)
