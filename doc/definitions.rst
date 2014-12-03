:orphan:

Definition files
================

natu's constants and units are defined in INI_ files.  Four files are loaded by
default:

.. toctree::

  base-ini
  derived-ini
  BIPM-ini
  other-ini

Other files can be added by appending the :attr:`definitions` list in
:mod:`natu.config`.  The files are processed sequentially, and the definitions
of symbols can reference previous symbols.  These constants, functions, and
classes are defined before the first file:

- *pi*
- :func:`~math.exp`
- :func:`~math.log`
- :func:`~math.log10`
- :func:`sqrt`
- :class:`~natu.core.Quantity`
- :class:`~natu.core.ScalarUnit`

The INI_ format is very similar to the tables in the pages for the files listed
above.  An equals sign separates the first two columns ("Symbol" and
"Expression"), a comma starts the "Prefixable" column, and a semicolon starts
the last column ("Name & notes").

The "Prefixable" column may be *True*, *False*, or empty.  A unit has a *True*
or a *False* "Prefixable" entry.  If a unit is prefixable, `SI prefixes`_ are
added upon access.  A constant has an empty "Prefixable" entry.  Constants are
never prefixable.

Single-character `SI prefixes`_ take precedence over the two-character prefix
'da' (`deca <https://en.wikipedia.org/wiki/Deca->`_).  As a hypothetical
example, if a unit with name and symbol 'am' is defined, 'dam' will refer to the
deciam, not the decametre_.  Also, non-prefixed units override the prefixed
ones.  For example, if a unit named 'dam' is established, it will override the
decametre_ (and deciam), which has the same symbol.

The "Name & notes" column is ignored.  It is only included for reference.

Some units such as `degC <http://en.wikipedia.org/wiki/Celsius>`_ and `Np
<http://en.wikipedia.org/wiki/Neper>`_ are not simple scaling factors.  The
"Expression" entry of these units contains a tuple with two functions.  The
first function maps a number to a quantity.  The second function is its inverse.
These are the first two arguments to construct a lambda unit
(:class:`~natu.core.LambdaUnit`).

`SI prefixes`_ can be applied to previous symbols except in the definition of
lambda units.

The sections of the INI_ files are only for organization (though required).  The
submodules of :mod:`natu.groups` do not rely on the sections.  The dimensions of
the derived constants and units are calculated and used instead.

.. warning::  Be sure that you use definition files from a trusted source.
   Parts of the files are processed using :func:`eval`, which is susceptible to
   malicious code.


.. _INI: http://en.wikipedia.org/wiki/INI_file
.. _SI prefixes: http://en.wikipedia.org/wiki/Metric_prefix
.. _decametre: http://en.wikipedia.org/wiki/Decametre
