#!/usr/bin/python
""":mod:`numpy`, adapted for use with physical quantities

Many of the functions only accept dimensionless quantities, and they
operate on the underlying values---not the values as represented in a
particular display unit.  To operate on values in a display unit would be
to favor a particular unit, which is against the `design of the package
<index.html>`_.

The constants (*pi*, *e*) are exactly as they are in :mod:`numpy`.

These functions accept floats, integers, and dimensionless quantities:

- Hyperbolic functions: :func:`arccosh`, :func:`arcsinh`, :func:`arctanh`,
  :func:`cosh`, :func:`sinh`, and :func:`tanh`

They functions are the same as those from :mod:`numpy`.  The functions cast
quantities cast as floats and return floats.

These functions accept angle as a quantity:

- :func:`cos`, :func:`sin`, and :func:`tan`

These functions accept floats, integers, and dimensionless quantities:

- :func:`acos`, :func:`asin`, :func:`atan`, and :func:`atan2`

They return angles as quantities.

These functions are no longer applicable and have been deleted since angle
is a quantity:

- :func:`degrees`, :func:`radians`, :func:`rad2deg`, and :func:`deg2rad`

All other functions are directly imported from :mod:`numpy`.  However, some of
these need to be adapted (`Issue #7
<https://github.com/kdavies4/natu/issues/7>`_).
"""

from __future__ import absolute_import

from numpy import *
from . import _decorators as decor

# TODO: Update numpy.info for the modified functions.

# Trigonometric functions
# -----------------------

cos = decor.trig(cos)
sin = decor.trig(sin)
tan = decor.trig(tan)
arccos = decor.inv_trig(arccos)
arcsin = decor.inv_trig(arcsin)
arctan = decor.inv_trig(arctan)
#arctan2 = decor.inv_trig_yx(  # TODO fix
#    arctan2,
#    """Return the arc tangent of y/x as an angle.
#
#    Unlike atan(y/x), the signs of both x and y are considered.""")
#hypot = decor.homogeneous_copy_props(hypot)  # TODO fix

# These aren't needed since angle is a quantity:
del degrees, radians, rad2deg, deg2rad

#'unwrap'

# Hyperbolic functions
# --------------------

arccosh = decor.dimensionless(arccosh)
arcsinh = decor.dimensionless(arcsinh)
arctanh = decor.dimensionless(arctanh)
cosh = decor.dimensionless(cosh)
sinh = decor.dimensionless(sinh)
tanh = decor.dimensionless(tanh)

# TODO: Support the functions below.
# The ones as strings are from numpy.core.umath.
# The ones as comments are from elsewhere in numpy.
# Both can be imported from the base of the numpy module.

# Rounding
# --------

# around
# round_
#'rint'
# fix
#'floor'
#'ceil'
#'trunc'

# Sums, products, differences
# ---------------------------
# prod
# sum
# nansum
# cumprod
# cumsum
# diff
# ediff1d
# gradient
# cross # should introduce a factor of 1/cyc
# trapz

# Exponents and logarithms
# ------------------------

#'exp'
#'expm1'
#'exp2'
#'log'
#'log10'
#'log2'
#'log1p'
#'logaddexp'
#'logaddexp2'

# Other special functions
# -----------------------
# IO
# sinc

# Floating point routines
# -----------------------
#'signbit'
#'copysign'
#'frexp'
#'ldexp'

# Arithmetic operations
# ---------------------
#'add'
#'reciprocal'
#'negative'
#'multiply'
#'divide'
#'power'
#'subtract'
#'true_divide'
#'floor_divide'
#'fmod'
#'mod'
#'modf'
#'remainder'

# Handling complex numbers
# ------------------------
# angle
# real
# imag
#'conj'

# Miscellaneous
# -------------
# convolve
# clip
#'sqrt'
#'square'
#'absolute'
#'fabs'
#'sign'
#'maximum'
#'minimum'
#'fmax'
#'fmin'
# nan_to_num
# real_if_close
# interp

# Not on webpage:
#'bitwise_and'  # broken
#'bitwise_or'  # broken
#'bitwise_xor'  # broken
#'conjugate'  # broken
#'equal'  # works as is
#'euler_gamma'
#'frompyfunc'
#'geterrobj'
#'greater'
#'greater_equal'
#'invert'
#'isfinite'  # broken
#'isinf'  # broken
#'isnan'  # broken
#'left_shift'
#'less'
#'less_equal'
#'logical_and'
#'logical_not'
#'logical_or'
#'logical_xor'
#'nextafter'
#'not_equal'
#'right_shift'
#'seterrobj'
#'spacing'

del decor
