#!/usr/bin/python
# -*- coding: utf-8 -*-
"""General supporting functions

**Functions:**

- :func:`delayed_exit` - Exit with a message and a delay.

- :func:`flatten_list` - Flatten a nested list.

- :func:`format_e`: Format the scientific notation in a numeric string

- :func:`get_group` - Return a tuple with the contents of a parenthetical
  expression and everything after it.

- :func:`list_packages` - Return a list of the names of a module and its
  subpackages.

- :func:`multiglob` - Return a set of filenames that match sets of pathnames
  and extensions.

- :func:`num2super` - Convert a number to Unicode_ superscript.

- :func:`product` - Return the product of a list of numbers.

- :func:`replace` - Perform a list of replacements on the text in a list of
  files.

- :func:`str2super` - Convert a numeric string to Unicode_ superscript.

- :func:`yes` - Ask a yes/no question and return *True* if the answer is 'Y'
  or 'y'.


.. _Unicode: http://www.unicode.org/
"""
from __future__ import division, unicode_literals

__author__ = "Kevin Davies"
__email__ = "kdavies4@gmail.com"
__copyright__ = ("Copyright 2013-2014, Kevin Davies, Hawaii Natural Energy "
                 "Institute, and Georgia Tech Research Corporation")
__license__ = "BSD-compatible (see LICENSE.txt)"

# pylint: disable=I0011, C0103

# from functools import reduce # Valid in Python 2.6+, required in Python 3

import os
import re
import sys
import time

from glob import glob
from pkgutil import walk_packages

def delayed_exit(message="Exiting...", t=0.5):
    """Exit with a message (*message*) and a delay of *t* seconds.

    **Example:**

    >>> delayed_exit() # doctest: +SKIP
    Exiting...
    """
    print(message)
    time.sleep(t)
    exit()

def flatten_list(l, ltypes=(list, tuple)):
    """Flatten a nested list.

    **Arguments:**

    - *l*: List (may be nested to an arbitrary depth)

          If the type of *l* is not in ltypes, then it is placed in a list.

    - *ltypes*: Tuple (not list) of accepted indexable types

    **Example:**

    >>> flatten_list([1, [2, 3, [4]]])
    [1, 2, 3, 4]
    """
    # Based on
    # http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html,
    # 10/28/2011
    ltype = type(l)
    if ltype not in ltypes:  # So that strings aren't split into characters
        return [l]
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if l[i]:
                l[i:i + 1] = l[i]
            else:
                l.pop(i)
                i -= 1
                break
        i += 1
    return ltype(l)

def format_e(num_str, code):
    """Format the scientific notation in a numeric string

    **Arguments:**

    - *num_str*: A numeric string

         If the string does not contain 'e' (no scientific notation), then it is
         returned directly.

    - *code*: Format code

         'H' is for HTML, 'L' is for LaTeX_, and 'U' is for Unicode_.


    .. _LaTeX: http://www.latex-project.org/

    """
    # TODO: Add examples.
    num_str = num_str.replace('E', 'e')
    try:
        base, exp = num_str.split('e')
    except ValueError:
        pass
    else:
        exp = exp.lstrip('+')
        if exp[0] == '-':
           exp = '-' + exp[1:].lstrip('0')
        else:
            exp = exp.lstrip('0')
        if code == 'H':
            return base + '&times;10<sup>%s</sup>' % exp
        if code == 'L':
            return base + r' \times 10^{%s}' % exp
        if code == 'P':
            return base + r'✕10' + str2super(exp)
    return num_str

def get_group(expr):
    """Return 1) the contents of a parenthetical expression and 2)
    everything after it.

    The parenthetical expression starts at the beginning of *expr* and may
    be nested.

    **Example:**

    >>> get_group("((abc)*d)*2") # doctest: +SKIP
    ('(abc)*d', '*2')

    .. testcleanup::
       >>> assert get_group("((abc)*d)*2") == ('(abc)*d', '*2')
    """
    i = 0
    count = 0
    length = len(expr)
    while i < length:
        if expr[i] == '(':
            count += 1
        elif expr[i] == ')':
            count -= 1
        if count == 0:
            return expr[1:i], expr[i + 1:]
        i += 1


def list_packages(package):
    """Return a list of the names of a package and its subpackages.

    This only works if the package has a :attr:`__path__` attribute, which
    is not the case for some (all?) of the built-in packages.

    **Example:**

    >>> from natu import groups
    >>> for package in list_packages(groups):
    ...     print(package)
    natu.groups
    natu.groups.acceleration
    natu.groups.amount
    natu.groups.angle
    natu.groups.area
    natu.groups.charge
    natu.groups.conductance
    natu.groups.constants
    natu.groups.current
    natu.groups.dimensionless
    natu.groups.energy
    natu.groups.force
    natu.groups.frequency
    natu.groups.length
    natu.groups.magnetic_flux
    natu.groups.magnetic_flux_density
    natu.groups.mass
    natu.groups.potential
    natu.groups.power
    natu.groups.pressure
    natu.groups.resistance
    natu.groups.si
    natu.groups.temperature
    natu.groups.time
    natu.groups.velocity
    natu.groups.volume
    """
    # Based to unutbu's response at
    # http://stackoverflow.com/questions/1707709

    # pylint: disable=I0011, W0612

    names = [package.__name__]
    for __, name, __ in walk_packages(package.__path__,
                                      prefix=package.__name__ + '.',
                                      onerror=lambda x: None):
        names.append(name)
    return names


def multiglob(pathnames, extensions={'*.mat'}):
    r"""Return a set of filenames that match a pathname pattern.

    Unlike Python's :func:`glob.glob` function, this function runs an additional
    expansion on matches that are directories.

    **Arguments:**

    - *pathnames*: String or set of strings used to match files or folders

         This may contain Unix shell-style patterns:

         ============   ============================
         Character(s)   Role
         ============   ============================
         \*             Matches everything
         ?              Matches any single character
         [seq]          Matches any character in seq
         [!seq]         Matches any char not in seq
         ============   ============================

   - *extensions*: Filename pattern or set of patterns that should be used to
     match files in any directories generated from *pathnames*

        These may also use the shell-style patterns above.
    """
    # TODO: Add an example.
    # **Example:**
    # >>> multiglob("examples/ChuaCircuit/*/") # doctest: +SKIP
    # ['examples/ChuaCircuit/1/dsres.mat', 'examples/ChuaCircuit/2/dsres.mat']
    # .. testcleanup::
    #    >>> sorted(multiglob("examples/ChuaCircuit/*/"))
    #    ['examples/ChuaCircuit/1/dsres.mat', 'examples/ChuaCircuit/2/dsres.mat']

    # Since order is arbitrary, the doctest is skipped here and included in
    # tests/tests.txt instead.
    fnames = set()
    for pathname in flatten_list(pathnames):
        items = glob(pathname)
        for item in items:
            if os.path.isdir(item):
                for ext in set(extensions):
                    fnames = fnames.union(glob(os.path.join(item, ext)))
            else:
                fnames.add(item)
    return fnames


# Exponential formatting
# Based on pint.formatting (https://github.com/hgrecco/pint, 7/11/14):
# - Copyright 2013 by Pint Authors
# - BSD license

def num2super(num):
    """Convert a number to Unicode_ superscript.
    """
    assert num % 1 == 0, "Only whole numbers are supported."
    # As of 7/16/14, there is no Unicode decimal or division sign.
    return str2super('%i' % num)

# In Python3, can do this (simpler and probably faster):
# EXP_TRANS = str.maketrans('0123456789', _UNICODE_EXPS)
# def num2super(num):
#     """Return a number as a Unicode superscript.
#     """
#     assert num % 1 == 0, "Only whole numbers are supported."
#     return ('%i' % num).replace('-', '⁻').translate(EXP_TRANS)

_UNICODE_EXPS = '⁰¹²³⁴⁵⁶⁷⁸⁹'

def str2super(num_str):
    """Convert a numeric string to Unicode_ superscript.
    """
    exp_str = num_str.replace('-', '⁻')
    for n in range(10):
        exp_str = exp_str.replace(str(n), _UNICODE_EXPS[n])
    return exp_str


def product(factors):
    """Return the product of a sequence of numbers (*factors*).

    **Example:**

    >>> product([1, 2, 3])
    6
    """
    # import operator
    # return reduce(operator.mul, factors, 1)
    # Avoid multiplication if only one factor:
    if not factors:
        return 1
    prod = factors[0]
    for factor in factors[1:]:
        prod = prod * factor  # *= not used because it isn't allowed by units
    return prod


def replace(fnames, rpls):
    r"""Perform a list of replacements on the text in a list of files.

    **Arguments:**

    - *fnames*: Filename or list of filenames

    - *rpl*: List of replacements to make

         Each entry is a tuple of (*src*, *dest*), where *dest* is a string that
         will replace the *src* string.  Each string can use Python's :mod:`re`
         expressions; see https://docs.python.org/2/library/re.html for details.

    **Example:**

    >>> fname = 'temp.txt'
    >>> with open(fname, 'w') as f:
    ...     __ = f.write("apple orange banana")
    >>> replace([fname], [('ba(.*)', r'ba\1\1')])
    >>> with open(fname, 'r') as f:
    ...     print(f.read())
    apple orange banananana

    .. testcleanup::
       >>> os.remove(fname)
    """

    # Compile the regular expressions.
    for i, (old, new) in enumerate(rpls):
        rpls[i] = (re.compile(old), new)

    # Read each file and make the replacements.
    for fname in flatten_list(fnames):
        with open(fname, 'r+') as f:
            text = f.read()
            for (old, new) in rpls:
                text = old.sub(new, text)
            f.seek(0)
            f.write(text)
            f.truncate()

# Getch classes based on
# http://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/,
# accessed 5/31/14

class _Getch(object):

    """Get a single character from the standard input.
    """

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix(object):

    """Get a single character from the standard input on Unix.
    """

    def __init__(self):
        # pylint: disable=I0011, W0611, W0612
        import tty

    def __call__(self):
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows(object):

    """Get a single character from the standard input on Windows.
    """
    # pylint: disable=I0011, W0611, W0612

    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


def yes(question):
    """Ask a yes/no question and return *True* if the answer is 'Y' or 'y'.

    **Arguments:**

    - *question*: String representing the question to the user

    **Example:**

    >>> if yes("Do you want to print hello (y/n)?"): # doctest: +SKIP
    ...     print("hello")
    """
    getch = _Getch()
    sys.stdout.write(question + ' ')
    answer = getch()
    print(answer)
    return answer.lower() == 'y'
