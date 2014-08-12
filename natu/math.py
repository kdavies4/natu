#!/usr/bin/python
"""`Python math`_, adapted for use with physical quantities

Many of the functions only accept dimensionless quantities, and they
operate on the underlying values---not the values as represented in a
particular display unit.  To operate on values in a display unit would be
to favor a particular unit, which is against the `design of the package
<index.html>`_.

The constants (*pi*, *e*) are exactly as they are in `Python math`_.

These functions accept floats, integers, and dimensionless quantities:

- Number-theoretic and representation functions: :func:`factorial`,
  :func:`frexp`, :func:`modf`, and :func:`trunc`
- Power and logarithmic functions: :func:`exp`, :func:`expm1`,
  :func:`log10`, :func:`log1p`, and :func:`log`
- Hyperbolic functions: :func:`acosh`, :func:`asinh`, :func:`atanh`,
  :func:`cosh`, :func:`sinh`, and :func:`tanh`
- Special functions: :func:`erf`, :func:`erfc`, :func:`gamma`, and
  :func:`lgamma`

They are the same as those from `Python math`_, except the documentation of
:func:`acosh`, :func:`asinh`, and :func:`atanh` has been corrected (see
http://bugs.python.org/issue21902).  The functions cast quantities cast as
floats and return floats, except for :func:`factorial`, which casts quantities
as integers and returns integers.

All of the other functions (below) are different than those in `Python
math`_.

These functions accept angle as a quantity:

- :func:`cos`, :func:`sin`, and :func:`tan`

They return floats (as in `Python math`_).

These functions accept floats, integers, and dimensionless quantities:

- :func:`acos`, :func:`asin`, :func:`atan`, and :func:`atan2`

They return angles as quantities.

:func:`atan2` accepts accept floats, integers, and quantities of the same
dimension.  It returns angle as a quantity.

These functions are no longer applicable and have been deleted since angle
is a quantity:

- :func:`degrees` and :func:`radians`

These functions accept floats, integers, and dimensionless quantities:

- :func:`ceil` and :func:`floor`

If the input is a float or an integer, the output is a float.  If the
input is a :class:`~natu.core.Quantity` or a
:class:`~natu.core.ScalarUnit`, the result is the same and has the same
:attr:`dimension`, :attr:`display`, etc.

These functions accept floats, integers, and quantities:

- :func:`fabs` and :func:`copysign`

If the input is a float or an integer, the output is a float.  If the
input is a :class:`~natu.core.Quantity` or a
:class:`~natu.core.ScalarUnit`, the result is of the same type and has
the same :attr:`dimension`, :attr:`display`, etc. (of the first argument
in the case of :func:`copysign`).

These functions also accept floats, integers, and quantities:

- :func:`ldexp`, :func:`pow`, and :func:`sqrt`

If the input is an float or an integer, the output is a float.  If the
input is a :class:`~natu.core.Quantity` or a
:class:`~natu.core.ScalarUnit`, the result is the same.  The dimensions
and display units are handled according to the power.

:func:`fmod` accepts floats, integers, and quantities of the same
dimension. The output is always a float.

These functions also accept floats, integers, and quantities of the same
dimension:

- :func:`fsum` and :func:`hypot`

The display unit (and :attr:`prefixable` attribute, if applicable) of the
first argument or entry is propagated to the output.

These functions accept floats or quantities:

- :func:`isinf`, :func:`isfinite` (only available in Python >= 3.2), and
  :func:`isnan`

Only the value of a quantity is used; dimension and display unit are
ignored.


.. _Python math: https://docs.python.org/3/library/math.html
"""
# pylint: disable=I0011, C0103, E0601, W0401, W0614, W0622

from __future__ import absolute_import

from math import *
from fractions import Fraction
from . import _decorators as decor

# Number-theoretic and representation functions
# ---------------------------------------------
ceil = decor.dimensionless_copy_props(
    ceil,
    """Return the ceiling of x as a float or quantity.

    This is the smallest integral value >= x.""")

floor = decor.dimensionless_copy_props(
    floor,
    """Return the floor of x as a float or quantity.

    This is the largest integral value <= x.""")

copysign = decor.use_values_copy_props(copysign)

fabs = decor.use_value_copy_props(
    fabs,
    "Return the absolute value of the float or quantity x.")

fmod = decor.homogeneous(fmod)

fsum = decor.homogeneous_copy_props_iter(fsum)

try:
    isinfinite = decor.use_value(isinfinite)  # This wasn't defined until v3.2.
except NameError:
    pass

isinf = decor.use_value(
    isinf,
    "Check if float or quantity x is infinite (positive or negative).")

isnan = decor.use_value(
    isnan,
    "Check if float or quantity x is not a number (NaN).")

ldexp = decor.use_values_copy_props_xi(
    ldexp,
    "Return x * (2**i), where x is a float or a quantity.")

# factorial, frexp, modf, and trunc are ok as they are.

# Power and logarithmic functions
# -------------------------------
pow = decor.use_value_raise(pow)
sqrt = decor.use_value_raise(sqrt, Fraction(1, 2))
# exp, expm1, log, log1p, and log10 are ok as they are.

# Trigonometric functions
# -----------------------
acos = decor.inv_trig(acos, "Return the arc cosine of x as an angle.")
asin = decor.inv_trig(asin, "Return the arc sine of x as an angle.")
atan = decor.inv_trig(atan, "Return the arc tangent of x as an angle.")
atan2 = decor.inv_trig_yx(
    atan2,
    """Return the arc tangent of y/x as an angle.

    Unlike atan(y/x), the signs of both x and y are considered.""")
cos = decor.trig(cos, "Return the cosine of theta (an angle).")
sin = decor.trig(sin, "Return the sine of theta (an angle).")
tan = decor.trig(tan, "Return the tangent of theta (an angle).")
hypot = decor.homogeneous_copy_props(hypot)

# Angular conversion
# ------------------
del degrees, radians  # These aren't needed since angle is a quantity.

# Hyperbolic functions
# --------------------
acosh = decor.change_doc(acosh, "Return the inverse hyperbolic cosine of x.")
asinh = decor.change_doc(asinh, "Return the inverse hyperbolic sine of x.")
atanh = decor.change_doc(atanh, "Return the inverse hyperbolic tangent of x.")
# cosh, sinh, and tanh are ok as they are.

# Special functions
# -----------------
# erf, erfc, gamma, and lgamma are ok as they are.

del absolute_import, Fraction, decor
