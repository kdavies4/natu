########
  natu
########

**Natural units in Python**

.. warning:: This project is currently in a pre-release state because it has not
   been fully tested.  It will be officially released once the unit tests are
   complete.

natu is a free, open-source package to represent physical quantities.  There are
many Python_ packages that deal with units and quantities (see `here
<seealso>`_), but natu is uniquely system-independent.  The units are derived
from physical constants with adjustable values and dimensions.  The value of a
unit is factored into a quantity so that the quantity is not "in" any particular
unit.  This has the following advantages:

- **Flexibility**: Different unit systems, including natural units (hence the
  name "natu"), can be represented by simply adjusting the physical constants.
- **Simplicity**: Unit conversion is inherent.  This results in quick
  computations and a small code base.  By default, dimensions and display units
  are tracked to catch errors and for string formatting, respectively.  However,
  this can be turned off to reduce the computational overhead to nearly zero
  while still providing the core features.
- **Scalability**: The values of the base physical constants can scaled to
  prevent exponent overflow, regardless of the units used [Davies2012]_,
  [#f1]_.
- **Intuitive**: Each unit is a fixed quantity which can be treated as a
  mathematical entity.  A variable quantity is expressed as the product of a
  number and a unit, as stated in [BIPM2006]_.
- **Representative**: The structure of the package reflects the way modern units
  are defined: standards organizations such as NIST_ assign values to universal
  physical constants so that the values of units can be determined by physical
  experiments instead of prototypes.

natu incorporates some of the best features of the existing packages and
introduces some novel features:

- Constants and units are defined in `INI files <definitions.html>`_.  Units can
  be added or removed.
- Units with offsets (e.g., `Celsius`_) and even nonlinear functions (e.g., the
  `decibel`_) are supported.
- Display units can be simplified automatically using `coherent relations`_
  gathered from the unit definitions.
- Units are automatically copied and sorted into convenient submodules (see
  :mod:`natu.groups`).
- Prefixes are automatically available.
- Rationalized and unrationalized unit systems are supported.
- Drop-in, quantity-aware replacements are available for :mod:`math` and
  :mod:`numpy`.
- There are no external dependencies.  Only the `Python Standard Library`_ is
  required; :mod:`numpy` is optional.
- Fractional exponents can be used for units and quantities (e.g., for the
  statcoulomb_).

For example, you can do this:

    >>> from natu.units import degC, K
    >>> print(0*degC + 100*K)
    100.0 degC

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


.. _Python: http://www.python.org/
.. _Python Standard Library: https://docs.python.org/3/library/
.. _GitHub repository: https://github.com/kdavies4/natu
.. _NIST: http://www.nist.gov/
.. _BIPM: http://www.bipm.org/
.. _Celsius: http://en.wikipedia.org/wiki/Celsius
.. _decibel: http://en.wikipedia.org/wiki/Decibel
.. _coherent relations: http://en.wikipedia.org/wiki/Coherence_(units_of_measurement)
.. _statcoulomb: http://en.wikipedia.org/wiki/Statcoulomb

.. rubric:: References

.. [Davies2012] K. Davies and C. Paredis, "`Natural Unit Representation in
                Modelica <http://www.ep.liu.se/ecp_article/index.en.aspx?issue=076;article=082>`_,"
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
