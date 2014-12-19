natu
====

**Natural units in Python**

**Warning:** This project is currently in a pre-release state.  It will be
officially released once the unit tests are complete.

[natu] is a free, open-source package to represent physical quantities.  There are
[many Python packages that deal with units and quantities](http://kdavies4.github.io/natu/seealso.html),
but [natu] is uniquely system-independent.  The units are derived from physical
constants with adjustable values and dimensions.  The value of a unit is
factored into a quantity so that the quantity is not "in" any particular unit.
This has the following advantages:

- **Flexible**: Different unit systems, including [natural units] (hence the
  name "natu"), can be represented by simply adjusting the physical constants.
- **Simple**: Unit conversion is inherent.  This results in quick computations
  and a small code base (< 1500 lines).  By default, dimensions and display
  units are tracked to catch errors and for string formatting, respectively.
  However, this can be turned off to reduce the computational overhead to nearly
  zero while still providing the core features.
- **Scalable**: The values of the base physical constants can scaled to prevent
  exponent overflow, regardless of the units used.
- **Intuitive**: Each unit is a fixed quantity which can be treated as a
  mathematical entity.  A variable quantity is expressed as the product of a
  number and a unit, as stated by [BIPM].
- **Representative**: The structure of the package reflects the way modern units
  are defined: standards organizations such as [NIST] assign values to universal
  physical constants so that the values of units can be determined by physical
  experiments instead of prototypes.

For example, you can do this:

    >>> from natu.units import degC, K
    >>> print(0*degC + 100*K)
    100.0 degC

Please
[see the tutorial](http://nbviewer.ipython.org/github/kdavies4/natu/blob/master/examples/tutorial.ipynb)
for more examples and [visit the main website][natu] for the full documentation.

#### Installation

The easiest way is to install [natu] is to use [pip]:

    > pip install natu

On Linux, it may be necessary to have root privileges:

    $ sudo pip install natu

#### License terms and development

[natu] is published under a [BSD-compatible license](LICENSE.txt).  Please
share any improvements you make, preferably as a pull request to the ``master``
branch of the [GitHub repository].  There are useful development scripts in the
[hooks folder](hooks).  If you find a bug, have a suggestion, or just want to
leave a comment, please
[open an issue](https://github.com/kdavies4/natu/issues/new).

[![Build Status](https://travis-ci.org/kdavies4/natu.svg?branch=travis)](https://travis-ci.org/kdavies4/natu)
![ ](doc/_static/hspace.png)
[![Code Health](https://landscape.io/github/kdavies4/natu/master/landscape.png)](https://landscape.io/github/kdavies4/natu)


[natu]: http://kdavies4.github.io/natu
[natural units]: http://en.wikipedia.org/wiki/Natural_units
[Python Standard Library]: https://docs.python.org/3/library/
[GitHub repository]: https://github.com/kdavies4/natu
[NIST]: http://www.nist.gov/
[BIPM]: http://www.bipm.org/
[pip]: https://pypi.python.org/pypi/pip
[pip]: https://pypi.python.org/pypi/pip
[degree Celsius (degC)]: http://en.wikipedia.org/wiki/Celsius
[decibel (dB)]: http://en.wikipedia.org/wiki/Decibel
[coherent relations]: http://en.wikipedia.org/wiki/Coherence_(units_of_measurement)
[statcoulomb]: http://en.wikipedia.org/wiki/Statcoulomb
[math]: https://docs.python.org/3/library/math.html
[numpy]: http://numpy.scipy.org/
[PyPI page]: http://pypi.python.org/pypi/natu
[natu.groups]: http://kdavies4.github.io/natu/natu.groups.html
