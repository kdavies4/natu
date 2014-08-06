BIPM units (BIPM.ini_)
======================

The table below lists the contents of the BIPM.ini_ file.  It implements the
definitions from [BIPM2006]_, including the `System International (SI) units`_
and some non-SI units.

The definitions depend on the following items:

- Classes: :class:`~natu.types.ScalarUnit`
- Functions: :func:`math.exp`, :func:`math.log`, and :func:`math.log10`
- Mathematical constants: *pi*
- Base physical constants: *R_inf*, *c*, *k_J*, *R_K*, *k_F*, and *R*
- Units: cyc

======== ====================================================== ========== ============
Symbol   Expression                                             Prefixable Name & notes
======== ====================================================== ========== ============
------ Mathematical relations ------
---------------------------------------------------------------------------------------
rad      ``cyc/(2*pi)``                                         *True*     `radian <http://en.wikipedia.org/wiki/Rad_(unit)>`_
------ Empirical relations ------
---------------------------------------------------------------------------------------
m        ``10973731.568539*cyc/R_inf``                          *True*     `metre <http://en.wikipedia.org/wiki/Metre>`_
s        ``299792458*m/c``                                      *True*     `second <http://en.wikipedia.org/wiki/Second>`_
Wb       ``483597.870e9/k_J``                                   *True*     `weber <http://en.wikipedia.org/wiki/Weber_(unit)>`_
S        ``25812.807557/(R_K*cyc)``                             *True*     `siemens <http://en.wikipedia.org/wiki/Siemens_(unit)>`_ (aka mho)
mol      ``96485.3365*Wb*cyc*S/k_F``                            *True*     `mole <http://en.wikipedia.org/wiki/Mole_(unit)>`_
K        ``8.3144621*(Wb*cyc)**2*S/(s*mol*R)``                  *True*     `kelvin <http://en.wikipedia.org/wiki/Kelvin>`_
------ Units considered independent of the base constants ------
---------------------------------------------------------------------------------------
cd       ``ScalarUnit(1., 'J')``                                *True*     `candela <http://en.wikipedia.org/wiki/Candela>`_ (independent of the base constants due to the `luminosity function <http://en.wikipedia.org/wiki/Luminosity_function>`_)
------ Remaining SI base units (BIPM2006_, Table 1) and intermediate units ------
---------------------------------------------------------------------------------------
Hz       ``cyc/s``                                              *True*     `hertz <http://en.wikipedia.org/wiki/Hertz>`_
V        ``Wb*Hz``                                              *True*     `volt <http://en.wikipedia.org/wiki/Volt>`_
A        ``V*S``                                                *True*     `ampere <http://en.wikipedia.org/wiki/Ampere>`_
C        ``A*s``                                                *True*     `coulomb <http://en.wikipedia.org/wiki/Coulomb>`_
J        ``V*C``                                                *True*     `joule <http://en.wikipedia.org/wiki/Joule>`_
Gy       ``m**2/s**2``                                          *True*     `gray <http://en.wikipedia.org/wiki/Gray_unit>`_
kg       ``J/Gy``                                               *False*    `kilogram <http://en.wikipedia.org/wiki/Kilogram>`_
g        ``kg/1000``                                            *True*     `gram <http://en.wikipedia.org/wiki/Gram>`_ (included for prefixes other than k)
------ Remaining coherent derived SI units (BIPM2006_, Table 3) ------
---------------------------------------------------------------------------------------
sr       ``rad**2``                                             *True*     `steradian <http://en.wikipedia.org/wiki/Steradian>`_
lm       ``cd*sr``                                              *True*     `lumen <http://en.wikipedia.org/wiki/Lumen_(unit)>`_
W        ``J/s``                                                *True*     `watt <http://en.wikipedia.org/wiki/Watt>`_
N        ``J/m``                                                *True*     `newton <http://en.wikipedia.org/wiki/Newton_unit>`_
Pa       ``N/m**2``                                             *True*     `pascal <http://en.wikipedia.org/wiki/Pascal_(unit)>`_
T        ``Wb/m**2``                                            *True*     `tesla <http://en.wikipedia.org/wiki/Tesla_(unit)>`_
lx       ``lm/m**2``                                            *True*     `lux <http://en.wikipedia.org/wiki/Lux>`_
F        ``s*S``                                                *True*     `farad <http://en.wikipedia.org/wiki/Farad>`_
ohm      ``1/S``                                                *True*     `ohm <http://en.wikipedia.org/wiki/Ohm>`_
H        ``s/S``                                                *True*     `henry <http://en.wikipedia.org/wiki/Henry_(unit)>`_
kat      ``mol/s``                                              *True*     `katal <http://en.wikipedia.org/wiki/Katal>`_
Sv       ``Gy``                                                 *True*     `sievert <http://en.wikipedia.org/wiki/Sievert>`_
Bq       ``s**-1``                                              *True*     `becquerel <http://en.wikipedia.org/wiki/Becquerel>`_
degC     ``(lambda n: (n + 273.15)*K, lambda T: T/K - 273.15)`` *True*     `degree Celsius <http://en.wikipedia.org/wiki/Celsius>`_
------ Non-SI units accepted for use with SI (BIPM2006_, Table 6) ------
---------------------------------------------------------------------------------------
min      ``60*s``                                               *False*    `minute <http://en.wikipedia.org/wiki/Minute>`_
hr       ``60*min``                                             *False*    `hour <http://en.wikipedia.org/wiki/Hour>`_
d        ``24*hr``                                              *False*    `day <http://en.wikipedia.org/wiki/Day>`_
deg      ``cyc/360``                                            *False*    `degree <http://en.wikipedia.org/wiki/Degree_(angle)>`_
arcmin   ``deg/60``                                             *False*    `arcminute <http://en.wikipedia.org/wiki/Arcminute>`_
arcsec   ``arcmin/60``                                          *False*    `arcsecond <http://en.wikipedia.org/wiki/Arcsecond>`_
ha       ``hm**2``                                              *False*    `hectare <http://en.wikipedia.org/wiki/Hectare>`_
L        ``dm**3``                                              *True*     `liter <http://en.wikipedia.org/wiki/Liter>`_
t        ``Mg``                                                 *False*    `tonne <http://en.wikipedia.org/wiki/Tonne>`_
------ Other non-SI units (BIPM2006_, Table 8) ------
---------------------------------------------------------------------------------------
*g_0*    ``9.80665*m/s**2``                                                `standard gravity <http://en.wikipedia.org/wiki/Standard_gravity>`_ [#f1]_, [#f2]_
cc       ``cm**3``                                              *False*    `cubic centimeter <http://en.wikipedia.org/wiki/Cubic_centimeter>`_ [#f1]_
*Hg*     ``13.5951*g*g_0/cc``                                              force per volume of mercury under standard gravity [#f1]_, [#f2]_
mmHg     ``mm*Hg``                                              *False*    `millimeter of mercury <http://en.wikipedia.org/wiki/Millimeter_of_mercury>`_
bar      ``100*kPa``                                            *True*     `bar <http://en.wikipedia.org/wiki/Bar_(unit)>`_
b        ``100*fm**2``                                          *False*    `barn <http://en.wikipedia.org/wiki/Barn_(unit)>`_
angstrom ``0.1*nm``                                             *False*    `angstrom <http://en.wikipedia.org/wiki/Angstrom>`_
M        ``1852*m``                                             *False*    `nautical mile <http://en.wikipedia.org/wiki/Nautical_mile>`_
kn       ``M/hr``                                               *False*    `knot <http://en.wikipedia.org/wiki/Knot_(unit)>`_
Np       ``(exp, log)``                                         *False*    `neper <http://en.wikipedia.org/wiki/Neper>`_ (defined in terms of amplitude ratio, not power)
B        ``(lambda n: 10**n, log10)``                           *True*     bel (defined in terms of power ratio, not amplitude)
dB       ``dB``                                                 *False*    `decibel <http://en.wikipedia.org/wiki/Decibel>`_ (explicitly included with prefix)
======== ====================================================== ========== ============

Since angle is explicit, some definitions are different than in [BIPM2006]_ and
[NIST2014]_:

- m ≈ 10973732 cyc *R_inf*\ :superscript:`-1` (i.e.,
  *R_inf* ≈ 10973732 cyc m\ :superscript:`-1`) [#f3]_
- S ≈ 25813 *R_K*\ :superscript:`-1` cyc\ :superscript:`-1` (i.e.,
  *R_K* ≈ 25813 ohm cyc\ :superscript:`-1`) [#f3]_
- Hz = cyc s\ :superscript:`-1` [#f4]_
- V = Wb Hz (i.e., Wb = V s cyc\ :superscript:`-1`) [#f4]_
- H = s S\ :superscript:`-1` (i.e., H = ohm s = V s A\ :superscript:`-1`;
  H ≠ Wb A\ :superscript:`-1`)

Note that frequency can be expressed in Hz or rad s\ :superscript:`-1` but not
s\ :superscript:`-1`.  Torque can be expressed in N m rad\ :superscript:`-1` or
J rad\ :superscript:`-1` but not N m or J.  Also note that the `steradian
(sr)`_, a unit of `solid angle`_, has dimension A\ :superscript:`2`.

deg, arcmin, and arcsec are used as the symbols for the degree_, arcminute_, and
arcsecond_ since the symbols in Table 6 of [BIPM2006]_ are not valid Python
names.  hr is used as the symbol for the hour_ since *h* is used for the `Planck
constant`_.

In general, prefixes are not included because they are added as needed upon
import.  However, [BIPM2006]_ (and BIPM.ini_) includes two units with explicit
prefixes: kg and dB.


.. _BIPM.ini: https://github.com/kdavies4/natu/blob/master/natu/config/BIPM.ini
.. _System International (SI) units: http://en.wikipedia.org/wiki/International_System_of_Units
.. _steradian (sr): http://en.wikipedia.org/wiki/Steradian
.. _henry (H): http://en.wikipedia.org/wiki/Henry_(unit)
.. _solid angle: http://en.wikipedia.org/wiki/Solid_angle
.. _Planck constant: http://en.wikipedia.org/wiki/Planck_constant

.. rubric:: References

.. [BIPM2006] International Bureau of Weights and Measures (BIPM),
              "`The International System of Units (SI)
              <http://www.bipm.org/utils/common/pdf/si_brochure_8_en.pdf>`_,"
              8th ed., 2006.
.. [NIST2014] National Institute of Science and Technology, "Fundamental
              Physical Constants: Complete Listing,"
              http://physics.nist.gov/constants, accessed 2014.

.. rubric:: Footnotes

.. [#f1] a constant (not a unit), but useful here
.. [#f2] not defined in [BIPM2006]_, but useful here
.. [#f3] Traditionally, angle is dropped [NIST2014]_.
.. [#f4] Angle is dropped in [BIPM2006]_.
