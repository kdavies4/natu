#!/usr/bin/python
"""Decorators to update the functions of Python math and Numpy umath
"""

# pylint: disable=I0011, C0103, C0111, E0611, E1101, W0141, W0142, W0621

from sys import version
from . import core
from .core import (Quantity, ScalarUnit, assert_homogeneous, homogeneous,
                    value, dimensionless_value)
from .units import rad

# TODO: Combine some of these once Python can propagate a function's signature
# up through a decorator (PEP 362?).

# functools
# ---------

if version >= '3':
    from functools import wraps
else:
    # Python2's functools.wraps requires that all of the attributes are
    # present.  We need "except AttributeError: pass" to wrap numpy ufuncs,
    # since they don't have __module__.

    from functools import WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES, partial

    # The following two functions are from Python 3.2
    # (http://hg.python.org/cpython/file/3.2/Lib/functools.py).

    def update_wrapper(wrapper, wrapped,
                       assigned=WRAPPER_ASSIGNMENTS,
                       updated=WRAPPER_UPDATES):
        """Update a wrapper function to look like the wrapped function

           wrapper is the function to be updated
           wrapped is the original function
           assigned is a tuple naming the attributes assigned directly
           from the wrapped function to the wrapper function (defaults to
           functools.WRAPPER_ASSIGNMENTS)
           updated is a tuple naming the attributes of the wrapper that
           are updated with the corresponding attribute from the wrapped
           function (defaults to functools.WRAPPER_UPDATES)
        """
        wrapper.__wrapped__ = wrapped
        for attr in assigned:
            try:
                value = getattr(wrapped, attr)
            except AttributeError:
                pass
            else:
                setattr(wrapper, attr, value)
        for attr in updated:
            getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
        # Return the wrapper so this can be used as a decorator via partial()
        return wrapper

    def wraps(wrapped,
              assigned=WRAPPER_ASSIGNMENTS,
              updated=WRAPPER_UPDATES):
        """Decorator factory to apply update_wrapper() to a wrapper function

           Returns a decorator that invokes update_wrapper() with the decorated
           function as the wrapper argument and the arguments to wraps() as the
           remaining arguments. Default arguments are as for update_wrapper().
           This is a convenience function to simplify applying partial() to
           update_wrapper().
        """
        return partial(update_wrapper, wrapped=wrapped,
                       assigned=assigned, updated=updated)

# Standard functions
# ------------------


def merge(value, prototype):
    """Merge *value* into a new :class:`~natu.core.ScalarUnit` or
    :class:`~natu.core.Quantity` with the properties (:attr:`dimension`,
    :attr:`display`, etc.) of *prototype*.

    If *prototype* is not a :class:`~natu.core.ScalarUnit` or
    :class:`~natu.core.Quantity`, then return *value* directly.
    """
    if isinstance(prototype, ScalarUnit):
        return ScalarUnit(value, prototype.dimension, prototype.display,
                          prototype.prefixable)
    return core.merge(value, prototype)


def merge_raise(value, prototype, power):
    """Same as :func:`merge`, but raise the dimension and display unit to
    to *power*
    """
    if isinstance(prototype, ScalarUnit):
        return ScalarUnit(value, power * prototype.dimension,
                          power * prototype.display, prototype.prefixable)
    try:
        return Quantity(value, power * prototype.dimension,
                        power * prototype.display)
    except AttributeError:
        return value

# Elementary wrappers
# -------------------


def arg_x(func):
    """Decorate a function to accept *x* as a keyword argument.
    """
    @wraps(func)
    def wrapped(x):
        return func(x)
    return wrapped


def arg_xi(func):
    """Decorate a function to accept *x* and *i* as keyword arguments.
    """
    @wraps(func)
    def wrapped(x, i):
        return func(x, i)
    return wrapped


def arg_yx(func):
    """Decorate a function to accept *y* and *x* as keyword arguments.
    """
    @wraps(func)
    def wrapped(y, x):
        return func(y, x)
    return wrapped


def change_doc(func, doc=None):
    """Update the docstring of a function.

    Wrap the function if the docstring is not writeable.
    """
    if doc is None:
        return func
    try:
        func.__doc__ = doc
    except AttributeError:
        @wraps(func)
        def wrapped(x):
            """Pass-through function of x"""
            return func(x)
        wrapped.__doc__ = doc
        return wrapped
    return func


def copy_props(func):
    """Decorate a function to return a :class:`~natu.core.ScalarUnit` or
    :class:`~natu.core.Quantity` instance that matches the first argument
    except for the computed value.
    """
    @wraps(func)
    def wrapped(x, *args, **kwargs):
        return merge(func(x, *args, **kwargs), x)

    wrapped.__doc__ += (
        "\nThe properties of the first term (:attr:`dimension`, \n"
        "\n:attr:`display`, etc.) are copied to the result.\n")
    return wrapped


def dimensionless(func):
    """Decorate a function to accept a number or a dimensionless quantity.

    If the quantity is not dimensionless, a TypeError is raised.
    """
    @wraps(func)
    def wrapped(*args):
        return func(*map(dimensionless_value, args))

    return wrapped


def dimensionless_implicit(func):
    """Decorate a function to give a special :class:`TypeError` message about
    dimensionality.

    This is triggered when a quantity is cast as a :class:`float` or
    :class:`int` but it is not dimensionless.
    """
    @wraps(func)
    def wrapped(*args):
        try:
            return func(*args)
        except TypeError:
            raise TypeError("The quantity must be dimensionless.")

    return wrapped

# Compound wrappers
# -----------------


def dimensionless_copy_props(func, doc=None):
    """Wrap a function to accept dimensionless quantities and pass the
    dimension, display unit, etc.  Change the docstring to *doc*.
    """
    return change_doc(arg_x(copy_props(dimensionless_implicit(func))), doc)


def trig(func, doc=None):
    """Wrap a trigonometric function that accepts angle in radians to accept
    angle as a quantity.
    """
    @wraps(func)
    def wrapped(theta):
        try:
            return func(theta / rad)
        except TypeError:
            raise TypeError("The argument must be an angle or zero.")

    return change_doc(wrapped, doc)


def inv_trig(func, doc=None):
    """Wrap an inverse trigonometric function that returns angle in radians to
    return angle as a quantity.
    """
    @wraps(func)
    def wrapped(x):
        return func(x) * rad

    return change_doc(wrapped, doc)


def inv_trig_yx(func, doc=None):
    """Wrap a dual-input inverse trigonometric function that returns angle in
    radians to return angle as a quantity.
    """
    # Note that *args isn't used because the variables wouldn't be labeled in
    # the documentation.
    @arg_yx
    @homogeneous
    @wraps(func)
    def wrapped(y, x):
        return func(y, x) * rad

    return change_doc(wrapped, doc)


def homogeneous_copy_props(func):
    """Wrap a function to use the :attr:`value` of quantities and pass the
    dimension, display unit, etc. of the first argument.  Check that the
    quantities have the same dimension.
    """
    return copy_props(homogeneous(func))


def homogeneous_copy_props_iter(func):
    """Decorate a function to use the values of an iterable of quantities and
    pass the dimension, display unit, etc. of the first quantity.
    """
    @wraps(func)
    def wrapped(x):
        assert_homogeneous(*x)
        return merge(func(map(value, x)), x[0])

    return wrapped


def use_value(func, doc=None):
    """Wrap a function to use the value of a quantity.
    """
    @wraps(func)
    def wrapped(x):
        return func(value(x))

    return change_doc(wrapped, doc)


def use_value_copy_props(func, doc):
    """Wrap a function to use the :attr:`value` of a quantity and pass the
    dimension, display unit, etc.  Change the docstring to *doc*.
    """
    return change_doc(arg_x(copy_props(use_value(func))), doc)


def use_value_raise(func, y=None):
    """Wrap a function to use the value of a quantity and raise the dimension
    and display unit to a power.

    If the power (*y*) is not given as an argument to this wrapper, then it is
    an argument to the function itself.
    """
    @wraps(func)
    def wrapped(x, y):
        return merge_raise(func(value(x), y), x, y)

    @wraps(func)
    def wrapped_fixed(x):
        return merge_raise(func(value(x)), x, y)

    return wrapped if y is None else wrapped_fixed


def use_values_copy_props(func, doc=None):
    """Decorate a function to use the values of two quantities and pass the
    properties (:attr:`dimension`, :attr:`display`, etc.) of the first.
    """
    @copy_props
    @wraps(func)
    def wrapped(x, y):
        return func(value(x), value(y))

    return change_doc(wrapped, doc)


def use_values_copy_props_xi(func, doc=None):
    """Wrap a function to use the :attr:`value` of quantities and pass the
    dimension, display unit, etc. of the first argument.  Change the docstring
    to *doc*.
    """
    return change_doc(arg_xi(use_values_copy_props(func)), doc)
