########
  natu
########

**Natural units in Python**

.. warning:: This project is currently in a pre-release state.  It will be
   officially released once the unit tests are complete.

natu is a free, open-source package to represent physical quantities.  There are
`many Python packages that deal with units and quantities <seealso.html>`_, but
natu is uniquely system-independent.  The units are derived from physical
constants with adjustable values and dimensions.  The value of a unit is
factored into a quantity so that the quantity is not "in" any particular unit.
This has the following advantages:

- **Flexible**: Different unit systems, including `natural units`_ (hence the
  name "natu"), can be represented by simply adjusting the `base physical
  constants <base-ini.html>`_.
- **Simple**: Unit conversion is inherent.  This results in quick computations
  and a small code base (about  1500 lines).  By default, dimensions and display
  units are tracked to catch errors and for string formatting.  This can be
  disabled to nearly eliminate the computational overhead while still providing
  the core features.
- **Intuitive**: Each unit is a fixed quantity that is treated as a
  mathematical entity.  A variable quantity is expressed as the product of a
  number and a unit, as stated in [BIPM2006]_.
- **Representative**: The design reflects the way modern units are defined.
  Standards organizations such as NIST_ assign values to universal physical
  constants so that the values of units can be determined by physical
  experiments instead of prototypes.
- **Scalable**: The values of the base physical constants can scaled to prevent
  exponent overflow, regardless of the units used [Davies2012]_, [#f1]_.

natu incorporates some of the best features of the `existing packages
<seealso.html>`_:

- Units with offsets and even nonlinear functions are supported.  For example:

  >>> from natu.units import degC, K
  >>> 0*degC + 100*K
  100.0 degC

  >>> from natu.units import dB
  >>> (10/dB + 10/dB)*dB  # Multiply by adding logarithms.
  100.0

- Prefixes are automatically applied.  For example:

  >>> from natu.units import km, m
  >>> km/m
  1000

- Display units are simplified using `coherent relations`_ automatically
  gathered from the unit definitions:

  >>> from natu.units import kg, m, s
  >>> 1*kg*m**2/s**2
  1.0 J

- Units are automatically sorted into convenient submodules such as
  :mod:`natu.groups.length`.

- Nearly 40 physical constants are included.  For example:

  >>> from natu.groups.constants import c
  >>> c
  299792458.0 m/s

- Additional constants and units can be easily added to the `definition files
  <definitions.html>`_ or defined in code.

- There are drop-in, quantity-aware replacements for :mod:`math` and
  :mod:`numpy`.  Quantities can be used in NumPy_ arrays or vice versa (see
  `here
  <http://nbviewer.ipython.org/github/kdavies4/natu/blob/master/examples/tutorial.ipynb#Arrays-and-other-data-types>`_).

- There are no dependencies except for the :mod:`numpy` replacements (previous
  feature).

- Units can have fractional powers.  For example:

  >>> from fractions import Fraction
  >>> m**Fraction(1, 2)
  ScalarUnit m(1/2) with dimension L(1/2) (not prefixable)

- Units and quantities can be formatted for HTML, LaTeX_, Unicode_, and
  Modelica_.  For example:

  >>> '{:H}'.format(10*m**2)
  '10.0&nbsp;m<sup>2</sup>'

  This renders in HTML as 10.0 m\ :sup:`2`\ .

- Rationalized and unrationalized unit systems are supported.


Please `see the tutorial
<http://nbviewer.ipython.org/github/kdavies4/natu/blob/master/examples/tutorial.ipynb>`_
for more examples.  The links in the sidebar give the `installation instructions
<install.html>`_ and more information.

**License terms and development**

natu is published under a `BSD-compatible license <license.html>`_.  Please
share any improvements you make, preferably as a pull request to the ``master``
branch of the `GitHub repository`_.  There are useful development scripts in
the `hooks folder <https://github.com/kdavies4/natu/blob/master/hooks/>`_.  If
you find a bug, have a suggestion, or just want to leave a comment, please `open
an issue <https://github.com/kdavies4/natu/issues/new>`_.

.. toctree::
   :hidden:

   natu.config
   natu.groups
   natu.math
   natu.numpy
   natu.units


.. _natural units: http://en.wikipedia.org/wiki/Natural_units
.. _GitHub repository: https://github.com/kdavies4/natu
.. _NIST: http://www.nist.gov/
.. _BIPM: http://www.bipm.org/
.. _Celsius: http://en.wikipedia.org/wiki/Celsius
.. _decibel: http://en.wikipedia.org/wiki/Decibel
.. _coherent relations: http://en.wikipedia.org/wiki/Coherence_(units_of_measurement)
.. _NumPy: http://www.numpy.org/
.. _statcoulomb: http://en.wikipedia.org/wiki/Statcoulomb
.. _Unicode: https://en.wikipedia.org/wiki/Unicode
.. _LaTeX: http://www.latex-project.org/
.. _Modelica: https://www.modelica.org/documents/ModelicaSpec33Revision1.pdf

.. rubric:: References

.. [Davies2012] K. Davies and C. Paredis, "`Natural Unit Representation in
                Modelica
                <http://www.ep.liu.se/ecp_article/index.en.aspx?issue=076;article=082>`_,"
                in Modelica Conference (Munich, Germany), Modelica Assoc.,
                Sep. 2012.
.. [BIPM2006] International Bureau of Weights and Measures (BIPM),
              "`The International System of Units (SI)
              <http://www.bipm.org/utils/common/pdf/si_brochure_8_en.pdf>`_,"
              8th ed., 2006.

.. rubric:: Footnotes

.. [#f1] Post by C. Bruns at
   http://stackoverflow.com/questions/2125076/unit-conversion-in-python
   (Feb. 5, 2010):

      "Units are NOT necessarily stored in terms of SI units internally.  This
      is very important for me, because one important application area for us is
      at the molecular scale.  Using SI units internally can lead to exponent
      overflow in commonly used molecular force calculations."
