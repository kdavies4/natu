########
  natu
########

**Natural units in Python**

.. warning:: This project is currently in a pre-release state because it has not
   been fully tested.  It will be officially released once the unit tests are
   complete.

natu is a free, open-source package to represent physical quantities.  There are
many Python_ packages that deal with units and quantities (see the "See also"
list below), but natu is unique because it is truly system-independent.  The
units are derived from physical constants with adjustable values and dimensions.
The value of a unit is factored into a quantity so that the quantity is not "in"
any particular unit.  This offers the following advantages:

- **Flexibility**: Different unit systems, including natural units (hence the
  name "natu"), can be represented by simply adjusting the physical constants.
- **Simplicity**: Unit conversion is inherent.  This results in quick
  computations and a small code base (<1500 lines).  By default, dimensions and
  display units are tracked to catch errors and for string formatting,
  respectively.  However, this feature can be turned off to reduce the
  computational overhead to nearly zero while still allowing input and output in
  mixed units.
- **Scalability**: Numerical scaling is independent of the units used to create
  quantities.  This can be used to prevent exponent overflow [Davies2012]_.
- **Intuitive**: Each unit is a fixed quantity which can be treated as a
  mathematical entity.  A variable quantity is expressed as the product of a
  number and a unit, as stated in [BIPM2006]_.
- **Representative**: The structure of the package reflects the way modern units
  are defined: standards organizations such as NIST_ assign values to universal
  physical constants so that the values of units can be determined by physical
  experiments instead of prototypes.

Please `view the tutorial
<http://nbviewer.ipython.org/github/kdavies4/natu/blob/master/examples/tutorial.ipynb>`_
to see how natu is used.  natu incorporates some of the best features of the
existing packages and introduces some novel features:

- All units are defined in `INI files <definitions.html>`_.  Units can be added
  or removed.
- Units can involve offsets (e.g., `degree Celsius (degC)`_) or even nonlinear
  functions (e.g., `decibel (dB)`_).
- Display units can be simplified automatically using `coherent relations`_
  gathered from the unit definitions.
- All units can be imported directly (``from natu.units import *``), selectively
  imported (``from natu.units import m, kg, s``), or used from within a package
  (``from natu import units as U; length = 10*U.m``).
- Prefixes are automatically applied to units upon import or access.
- Units are automatically copied and sorted into convenient groups (see
  `natu.groups <http://kdavies4.github.io/natu/natu.groups.html>`_).
- Rationalized or unrationalized unit systems can be represented.
- Modules are provided as drop-in quantity-aware replacements for math_ and
  numpy_.
- There are no external dependencies.  Only the `Python Standard Library`_ is
  required; numpy_ is optional.
- natu runs in Python 2 and 3.
- Fractional exponents can be used for units as well as quantities (e.g., in the
  definition of the statcoulomb_).

For the full documentation and more examples, please see the `main website`_.

For a list of changes, please see the `change log
<http://kdavies4.github.io/natu/changes.html>`_.

Installation
~~~~~~~~~~~~

The easiest way to install natu is to use pip_::

    > pip install natu

On Linux, it may be necessary to have root privileges::

    $ sudo pip install natu

Another way is to download and extract a copy of the package from the sidebar on
the left.  Run the following command from the base folder::

    > python setup.py install

Or, on Linux::

    $ sudo python setup.py install

License terms and development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

natu is published under a `BSD-compatible license
<https://github.com/kdavies4/natu/blob/master/LICENSE.txt>`_.  Please share any
improvements you make, preferably as a pull request to the ``master`` branch of
the `GitHub repository`_.  There are useful development scripts in the `hooks
folder <https://github.com/kdavies4/natu/blob/master/hooks/>`_.  If you find a
bug or have a suggestion, please `open an issue
<https://github.com/kdavies4/natu/issues/new>`_.

See also
~~~~~~~~

- `astropy.units <http://astropy.readthedocs.org/en/latest/units/>`_
- `Buckingham <http://code.google.com/p/buckingham/>`_
- `Magnitude <http://juanreyero.com/open/magnitude/>`_
- `NumericalUnits <https://pypi.python.org/pypi/numericalunits>`_
- `Pint <http://pint.readthedocs.org/>`_
- `Python-quantities <https://pypi.python.org/pypi/quantities>`_
- `Scalar <http://russp.us/scalar-guide.htm>`_
- `Scientific.Physics.PhysicalQuantities <http://dirac.cnrs-orleans.fr/ScientificPython/ScientificPythonManual/Scientific.Physics.PhysicalQuantities-module.html>`_
- `SciMath <http://scimath.readthedocs.org/en/latest/units/intro.html>`_
- `sympy.physics.units <http://docs.sympy.org/dev/modules/physics/units.html>`_
- `udunitspy <https://github.com/blazetopher/udunitspy>`_
- `Units <https://bitbucket.org/adonohue/units/>`_
- `Unum <https://bitbucket.org/kiv/unum/>`_


.. _Python: http://www.python.org/
.. _Python Standard Library: https://docs.python.org/3/library/
.. _GitHub repository: https://github.com/kdavies4/natu
.. _NIST: http://www.nist.gov/
.. _BIPM: http://www.bipm.org/
.. _pip: https://pypi.python.org/pypi/pip
.. _degree Celsius (degC): http://en.wikipedia.org/wiki/Celsius
.. _decibel (dB): http://en.wikipedia.org/wiki/Decibel
.. _coherent relations: http://en.wikipedia.org/wiki/Coherence_(units_of_measurement)
.. _statcoulomb: http://en.wikipedia.org/wiki/Statcoulomb
.. _math: https://docs.python.org/3/library/math.html
.. _numpy: http://numpy.scipy.org/
.. _main website: http://kdavies4.github.io/natu/

.. rubric:: References

.. [Davies2012] K. Davies and C. Paredis, "`Natural Unit Representation in
                Modelica <http://www.ep.liu.se/ecp_article/index.en.aspx?issue=076;article=082>`_,"
                in Modelica Conference (Munich, Germany), Modelica Assoc.,
                Sep. 2012.
.. [BIPM2006] International Bureau of Weights and Measures (BIPM),
              "`The International System of Units (SI)
              <http://www.bipm.org/utils/common/pdf/si_brochure_8_en.pdf>`_,"
              8th ed., 2006.
