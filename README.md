natu
====

**Natural units in Python**

**Warning:** This project is currently in a pre-release state because it has not
been fully tested.  It will be officially released once the unit tests are
complete.

natu is a free, open-source package to represent physical quantities.  There are
many [Python] packages that deal with units and quantities (see the
[list below](#seealso)), but natu is unique because it is truly
system-independent.  The units are derived from physical constants with
adjustable values and dimensions.  The value of a unit is factored into a
quantity so that the quantity is not "in" any particular unit.  This offers the
following advantages:

- **Flexibility**: Different unit systems, including natural units (hence the
  name "natu"), can be represented by simply adjusting the physical constants.
- **Simplicity**: Unit conversion is inherent.  This results in quick
  computations and a small code base (<1500 lines).  By default, dimensions and
  display units are tracked to catch errors and for string formatting,
  respectively.  However, this feature can be turned off to reduce the
  computational overhead to nearly zero while still allowing input and output in
  mixed units.
- **Scalability**: Numerical scaling is independent of the units used to create
  quantities.  This can be used to prevent exponent overflow [[1]](#ref1),
  [[2]](#ref2).
- **Intuitive**: Each unit is a fixed quantity which can be treated as a
  mathematical entity.  A variable quantity is expressed as the product of a
  number and a unit, as stated by [BIPM][BIPM] [[3]](#ref3).
- **Representative**: The structure of the package reflects the way modern units
  are defined: standards organizations such as [NIST] assign values to universal
  physical constants so that the values of units can be determined by physical
  experiments instead of prototypes.

Please
[view the tutorial](http://nbviewer.ipython.org/github/kdavies4/natu/blob/master/examples/tutorial.ipynb)
to see how natu is used.  natu incorporates some of the best features of the
existing packages and introduces some novel features.  For the full
documentation and more examples, visit the [main website].

#### Installation

The easiest way is to install natu is to use [pip]:

    > pip install natu

On Linux, it may be necessary to have root privileges:

    $ sudo pip install natu

Another way to install natu is to download and extract a copy of the package
from the [main website], the [GitHub repository], or the [PyPI page].  Once you
have a copy, run the following command from the base folder:

    > python setup.py install

Or, on Linux:

    $ sudo python setup.py install

#### License terms and development

natu is published under a [BSD-compatible license](LICENSE.txt).  Please
share any improvements you make, preferably as a pull request to the ``master``
branch of the [GitHub repository].  There are useful development scripts in the
[hooks folder](hooks).  If you find a bug or have a suggestion, please
[open an issue](https://github.com/kdavies4/natu/issues/new).

[![Build Status](https://travis-ci.org/kdavies4/natu.svg?branch=travis)](https://travis-ci.org/kdavies4/natu)
![ ](doc/_static/hspace.png)
[![Code Health](https://landscape.io/github/kdavies4/natu/master/landscape.png)](https://landscape.io/github/kdavies4/natu)

<a name="seealso"></a>
#### See also

- [astropy.units](http://astropy.readthedocs.org/en/latest/units/)
- [Buckingham](http://code.google.com/p/buckingham/)
- [Magnitude](http://juanreyero.com/open/magnitude/)
- [NumericalUnits](https://pypi.python.org/pypi/numericalunits)
- [Pint](http://pint.readthedocs.org/)
- [Python-quantities](https://pypi.python.org/pypi/quantities)
- [Scalar](http://russp.us/scalar-guide.htm)
- [Scientific.Physics.PhysicalQuantities](http://dirac.cnrs-orleans.fr/ScientificPython/ScientificPythonManual/Scientific.Physics.PhysicalQuantities-module.html)
- [SciMath](http://scimath.readthedocs.org/en/latest/units/intro.html)
- [sympy.physics.units](http://docs.sympy.org/dev/modules/physics/units.html)
- [udunitspy](https://github.com/blazetopher/udunitspy)
- [Units](https://bitbucket.org/adonohue/units/)
- [Unum](https://bitbucket.org/kiv/unum/)


[Python]: http://www.python.org/
[Python Standard Library]: https://docs.python.org/3/library/
[GitHub repository]: https://github.com/kdavies4/natu
[NIST]: http://www.nist.gov/
[BIPM]: http://www.bipm.org/
[pip]: https://pypi.python.org/pypi/pip
[Python]: http://www.python.org/
[pip]: https://pypi.python.org/pypi/pip
[degree Celsius (degC)]: http://en.wikipedia.org/wiki/Celsius
[decibel (dB)]: http://en.wikipedia.org/wiki/Decibel
[coherent relations]: http://en.wikipedia.org/wiki/Coherence_(units_of_measurement)
[statcoulomb]: http://en.wikipedia.org/wiki/Statcoulomb
[math]: https://docs.python.org/3/library/math.html
[numpy]: http://numpy.scipy.org/
[main website]: http://kdavies4.github.io/natu
[PyPI page]: http://pypi.python.org/pypi/natu
[natu.groups]: http://kdavies4.github.io/natu/natu.groups.html

#### References and footnotes

1. <a name="ref1"></a>
   K. Davies and C. Paredis,
   "[Natural Unit Representation in Modelica](http://www.ep.liu.se/ecp_article/index.en.aspx?issue=076;article=082),"
   in Modelica Conference (Munich, Germany), Modelica Assoc., Sep. 2012.
2. <a name="ref2"></a>
   Post by C. Bruns at
   http://stackoverflow.com/questions/2125076/unit-conversion-in-python
   (Feb. 5, 2010):

      > Units are NOT necessarily stored in terms of SI units internally.  This
      > is very important for me, because one important application area for us
      > is at the molecular scale.  Using SI units internally can lead to
      > exponent overflow in commonly used molecular force calculations.
3. <a name="ref3"></a>
   International Bureau of Weights and Measures (BIPM),
   "[The International System of Units (SI)](http://www.bipm.org/utils/common/pdf/si_brochure_8_en.pdf),"
   8th ed., 2006.
