#!/usr/bin/python
"""Contains a class with methods to represent and operate on the product of
factors with exponents
"""
# split_code(), _format(), and _FORMATS are based on pint.formatting
# (https://github.com/hgrecco/pint, 7/11/14):
# - Copyright 2013 by Pint Authors
# - BSD license

# pylint: disable=I0011, C0103, E0213, R0904, W0142, W0223, W0621

from __future__ import division

import re

from collections import Counter
from fractions import Fraction
from .util import get_group, num2super

# Default keyword arguments sent to format()
_DEFAULT_FORMAT = dict(
    mul='*',
    div='/',
    group='({0})',
    base_fmt=lambda x: x,
    exp_fmt=lambda x: '(%s)' % x if isinstance(x, Fraction) else '%s' % x,
)

# Map format specifications to sets of keyword arguments for format.
_FORMATS = {
    '': _DEFAULT_FORMAT,
    'H':  # HTML
    dict(_DEFAULT_FORMAT,
         mul='&nbsp;',
         div=None,
         exp_fmt=lambda x: '<sup>%s</sup>' % x,
         ),
    'L':  # LaTeX
    dict(_DEFAULT_FORMAT,
         mul='\,',
         div=None,
         group=r'\left({0}\right)',
         base_fmt=lambda x: r'\mathrm{%s}' % x,
         exp_fmt=lambda x: ('^{%s}' % x
                             if isinstance(x, Fraction) or x < 0 else
                             '^%s' % x),
         ),
    'M':  # Modelica
    dict(_DEFAULT_FORMAT,
         mul='.',
         ),
    'U':  # Unicode
    dict(_DEFAULT_FORMAT,
         mul=' ',
         div=None,
         exp_fmt=num2super,
         ),
    'V':  # Verbose
    dict(_DEFAULT_FORMAT,
         mul=' * ',
         div=' / ',
         exp_fmt=lambda x: ('**(%s)' % x if isinstance(x, Fraction) else
                             '**%s' % x),
         ),
    }

_KNOWN_FORMATS = frozenset(_FORMATS)


def split_code(code):
    """Split a string format code into standard and exponent-specific parts.
    """
    # Based on pint.formatting (https://github.com/hgrecco/pint, 7/11/14).
    # Copyright 2013 by Pint Authors
    # License: BSD

    std_fmt = ''
    exp_fmt = ''
    for char in code:
        if char in _KNOWN_FORMATS:
            if exp_fmt:
                raise ValueError("Multiple exponent format codes found")
            exp_fmt = char
        else:
            std_fmt += char
    return std_fmt, exp_fmt


def _format(factors, **kwargs):
    """Format the product of (base, exponent) pairs as a string

    **Parameters:**

    - *factors*: List of (base, exponent) pairs

       Each base is a string that represents the base of a factor.  Each
       exponent is a number (:class:`numbers.Number` instance).

    - *mul*: String used to represent multiplication

    - *div*: String used to represent division

         If *div* is *None*, then negative powers are used instead of division.

    - *group*: Format used to group an expression

         This string must contain '{0}' as a placeholder for the grouped
         expression.  If *group* is *None*, the multiple division operators will
         be used if necessary.

    - *base_fmt*: Function that takes a base and formats it as a string

    - *exp_fmt*: Function that takes an exponent and formats it as a string
    """
    # pylint: disable=I0011, R0912

    if not factors:
        return ''

    # Process the arguments.
    mul = kwargs['mul']
    div = kwargs['div']
    group = kwargs['group']
    base_fmt = kwargs['base_fmt']
    if div:
        exp_fmt = lambda x: kwargs['exp_fmt'](abs(x))
    else:
        exp_fmt = kwargs['exp_fmt']

    # Generate lists of strings of the numerator and denominator terms.
    num_terms = []
    den_terms = []
    for b, e in sorted(factors):
        base = base_fmt(b)
        if e == 1:
            num_terms.append(base)
        elif e > 0:
            num_terms.append(base + exp_fmt(e))
        elif e == -1 and div:
            den_terms.append(base)
        else:
            den_terms.append(base + exp_fmt(e))

    if not div:
        # Show as product using negative exponents.
        return mul.join(num_terms + den_terms)

    # Show as ratio, where all factors have positive exponents.
    num = mul.join(num_terms) or '1'

    if not den_terms:
        return num

    if group:
        den = mul.join(den_terms)
        if len(den_terms) > 1:
            den = group.format(den)
    else:
        den = div.join(den_terms)

    return div.join([num, den])

# Basic regular expressions:
u = r'\d+'  # Unsigned integer
i = '[+-]?' + u  # Integer
fl1 = i + r'\.(?:' + u + ')?(?:[Ee]' + i + ')?' # Float due to decimal point
fl2 = i + r'(?:\.' + u + ')?(?:[Ee]' + i + ')'  # Float due to exponential
fl = '(?:%s)|(?:%s)' % (fl1, fl2)  # Float
fr = i + '/' + u  # Fraction

# Regular expression parser for a base and an exponent:
base = '([A-Za-z][A-Za-z_]*)'
exponent = r'(?:(?:\((%s)\))|(%s)|(%s))' % (fr, fl, i)
remainder = '(.*)'
parser = re.compile('%s%s?%s?' % (base, exponent, remainder))
del fl1, fl2, fl, fr, base, exponent, remainder


def _split(factor):
    """Split a factor into a base, an exponent, and a remainder.
    """
    # Parse the factor.
    base, exp_fr, exp_fl, exp_i, remainder = parser.match(factor).groups()

    # Cast the exponent into the appropriate number type.
    if exp_fr is not None:
        exp = Fraction(exp_fr)
    elif exp_fl is not None:
        exp = float(exp_fl)
    elif exp_i is not None:
        exp = int(exp_i)
    else:
        exp = 1

    return base, exp, remainder


class Exponents(Counter):

    r"""Dictionary-like class to track exponents of independent bases

    The keys are the bases and the values are the exponents.  The supported
    mathematical operations (addition, subtraction, negation, multiplication,
    and division) operate on the exponents, not on the bases.

    **Initialization signatures:**

    - :class:`Exponents`\(): Returns an :class:`Exponents` instance with an
      empty set of factors

    - :class:`Exponents`\(a=\ *exp1*, b=\ *exp2*, ...), where *exp1* and *exp2*
      are numbers: Returns an :class:`Exponents` instance that represents the
      product of symbol 'a' raised to the power of *exp1* and symbol 'b' raised
      to the power of *exp2*

    - :class:`Exponents`\(dict(a=\ *exp1*, b=\ *exp2*, ...)): Returns the same
      result as the previous signature

    - :class:`Exponents`\({a: *exp1*, b: *exp2*, ...}): Returns the same result
      as the previous signature

    - :class:`Exponents`\(*string*): Returns an :class:`Exponents` instance
      indicated by *string*

         *string* must follow the format accepted by the :meth:`fromstr`
         constructor.

    **Formatting**

    An :class:`Exponents` instance can be expressed using `string format syntax
    <https://docs.python.org/2/library/string.html#format-string-syntax>`_.  The
    format codes are:

    - '' (default):

         - Exponents directly follow the symbols of the bases.
         - '*' indicates multiplication and '/' indicates division.
         - If the denominator contains multiple factors, then they are grouped
           in parentheses.

    - 'H' (HTML):

         - Exponents are written as superscripts ('<sup>...</sup>')
         - A non-breaking space ('&nbsp;') indicates multiplication and '/'
           indicates division.
         - If the denominator contains multiple factors, then they are grouped
           in parentheses.

    - 'L' (LaTeX_ math):

         - Exponents are written as superscripts ('^...')
         - Back-to-back factors indicate multiplication and '/' indicates
           division.
         - If the denominator contains multiple factors, then they are grouped
           in parentheses.
         - The output must be typeset in LaTeX_ math mode (e.g., surround it
           with '$...$').

    - 'M' ([Modelica]_): Same as the default except '.' indicates multiplication
      instead of '*'

    - 'U' (Unicode_):

         - Exponents are indicated by Unicode_ superscripts.  Only integer
           exponents are supported.
         - A space indicates multiplication.  Negative exponents are used
           instead of division.

    - 'V' (verbose):

         - Exponents are noted by '**'.
         - ' * ' indicates multiplication and ' / ' indicates division.
         - If the denominator contains multiple factors, then they are grouped
           in parentheses.

    **Examples:**

    Initialization and representation:

    >>> x = Exponents(a=1, b=-1, c=-2)
    >>> dict(x)
    {'a': 1, 'b': -1, 'c': -2}
    >>> str(x)
    'a/(b*c2)'
    >>> format(x, 'V')
    'a / (b * c**2)'
    >>> format(x, 'H')
    'a&nbsp;b<sup>-1</sup>&nbsp;c<sup>-2</sup>'

    .. role:: raw-html(raw)
       :format: html

    The last result displays in HTML as the following:
    :raw-html:`a&nbsp;b<sup>-1</sup>&nbsp;c<sup>-2</sup>`.

    Addition:

    >>> print(x + x)
    a2/(b2*c4)

    Multiplication:

    >>> print(x*2)
    a2/(b2*c4)
    >>> str(0*x)
    ''

    Division:

    >>> print(x/2)
    a0.5/(b0.5*c)

    Negation:

    >>> print(-x)
    b*c2/a

    Subtraction:

    >>> str(x - x)
    ''

    Indexing:

    >>> x['a']
    1
    >>> x['d']
    0

    Updating:

    >>> x['a'] += 1
    >>> x['d'] += 2
    >>> x['b'] = 2
    >>> str(x)
    'a2*d2/(b2*c2)'


    .. _Unicode: https://en.wikipedia.org/wiki/Unicode
    .. _LaTeX: http://www.latex-project.org/

    .. rubric:: References

    .. [Modelica] Modelica Specification, version 3.3, p. 235--236
       (https://www.modelica.org/documents)
    """

    def update(self, *args, **kwargs):
        """update([E, ]**F) -> None

        Update this :class:`Exponents` instance from :class:`dict`/iterable *E*
        and *F*.

        If *E* is present, this does:

           ``for k in E: D[k] = E[k]``

        Then it does:

           ``for k in F: D[k] = F[k]``

        Alternatively, *E* can be a string that is compatible with the
        :meth:`fromstr` constructor.

        **Example:**

        >>> e = Exponents()
        >>> e.update(a=1)
        >>> e.update(dict(b=2), c=3)
        >>> e.update('1/d')
        >>> e # doctest: +SKIP
        Exponents({'a': 1, 'b': 2, 'c': 3, 'd': -1})

        .. testcleanup::
           >>> assert e == dict(a=1, b=2, c=3, d=-1)
        """
        try:
            # Assume args[0] is a string.
            arg = args[0].replace(' ', '')  # Remove spaces.
        except (IndexError, AttributeError):
            Counter.update(self, *args, **kwargs)
        else:
            if len(args) > 1:
                raise TypeError("update expected at most 1 arguments, got %i"
                                % len(args))
            Counter.update(self, Exponents.fromstr(arg), **kwargs)

    @classmethod
    def fromstr(cls, expr):
        """Create an :class:`Exponents` instance from a string expression.

        **Parameters:**

        - *expr*: String expression that indicates the symbols and exponents

             Each symbol may be followed directly by an exponent.  If the
             exponent is not an integer, it may be expressed using a decimal or
             as a fraction (with '/') enclosed in parentheses.  Factors may be
             multiplied('*'), divided ('/'), or grouped ('(...)').

        **Example:**

        >>> e = Exponents.fromstr('a/b/(c*d2)')
        >>> print(e)
        a/(b*c*d2)
        """
        # Note: It's not possible to use the ast module (at least not easily)
        # because a valid expression is not necessarily valid Python.  pyparser
        # is an option, but it's much slower than re.

        def process_expression(expr, exponents, add=True):
            """Process a factor from the left of a string expression (expr).

            Add (if add == True) the factor to exponents if add == True.
            Otherwise, subtract it.  Return the remainder of the expression.
            """
            # Pass if the expression is unity.
            if expr[0] == '1':
                return expr.strip('1')

            # Find the base, exponent, and remainder of the expression.
            base, exp, remainder = _split(expr)

            # Update the exponents.
            if add:
                exponents[base] += exp
            else:
                exponents[base] -= exp

            return remainder

        new = cls()
        add = True
        while len(expr) >= 1:
            if expr[0] == '(':
                # Recurse into the subexpression:
                subexpr, expr = get_group(expr)
                if add:
                    new += cls.fromstr(subexpr)
                else:
                    new -= cls.fromstr(subexpr)
            else:
                expr = process_expression(expr, new, add)

            # Get the operator for the next loop.
            if len(expr) >= 1:
                add = expr[0] == '*'
                assert add or expr[0] == '/', (
                    "The operation must be '*' or '/'.")
                expr = expr[1:]
                assert expr, "The expression can't end with an operator."

        return new

    def __add__(x, y):
        """x.__add__(y) <==> x+y"""
        copy = x.copy()
        for base, exp in y.items():
            copy[base] += exp
        return copy

    __radd__ = __add__
    __radd__.__doc__ = "x.__radd__(y) <==> y+x"

    def __iadd__(x, y):
        """x.__iadd__(y) <==> x+=y"""
        for base, exp in y.items():
            x[base] += exp
        return x

    def __sub__(x, y):
        """x.__sub__(y) <==> x-y"""
        result = x.copy()
        for base, exp in y.items():
            result[base] -= exp
        return result

    def __rsub__(x, y):
        """x.__rsub__(y) <==> y-x"""
        result = -x
        for base, exp in y.items():
            result[base] += exp
        return result

    def __isub__(x, y):
        """x.__isub__(y) <==> x-=y"""
        for base, exp in y.items():
            x[base] -= exp
        return x

    def __mul__(x, y):
        """x.__mul__(y) <==> x*y"""
        if y == 0:
            return x.__class__()
        return x.__class__({base: exp * y for base, exp in x.items()})

    __rmul__ = __mul__
    __rmul__.__doc__ = "x.__rmul__(y) <==> y*x"

    def __truediv__(x, y):
        """x.__truediv__(y) <==> x/y"""
        return x.__class__({base: exp / y for base, exp in x.items()})

    __div__ = __truediv__
    __div__.__doc__ = "x.__div__(y) <==> x/y"

    def __rtruediv__(x, y):
        """x.__rtruediv__(y) <==> y/x"""
        return x.__class__({base: y / exp for base, exp in x.items()})

    __rdiv__ = __rtruediv__
    __rdiv__.__doc__ = "x.__rdiv__(y) <==> y/x"

    def __imul__(x, y):
        """x.__imul__(y) <==> x*=y"""
        if y == 0:
            x.clear()
        else:
            for base, exp in x.items():
                x[base] = exp * y
        return x

    def __neg__(x):
        """x.__neg__() <==> -x"""
        return x.__class__({base: -exp for base, exp in x.items()})

    def __pos__(x):
        """x.__pos__() <==> x"""
        return x

    def __setitem__(x, i, y):
        """x.__setitem__(i, y) <==> x[i]=y"""
        if y == 0:
            del x[i]
        else:
            Counter.__setitem__(x, i, y)

    def __format__(self, format_code=''):
        """Format the Exponents instance according to format_code.
        """
        try:
            fmt = _FORMATS[format_code]
        except KeyError:
            raise ValueError("Unknown format code '%s' for object of type '%s'"
                             % (format_code, self.__class__.__name__))
        result = _format(self.items(), **fmt)
        return result

    def __str__(self):
        """Return an informal string representating the Exponents instance.
        """
        return format(self)
