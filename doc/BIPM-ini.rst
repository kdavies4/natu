BIPM units (BIPM.ini_)
======================

The table below lists the contents of the BIPM.ini_ file.  It implements the
definitions from [BIPM2006]_, including the `System International (SI) units`_
and some non-SI units.

The definitions depend on the following items:

- Classes: :class:`~natu.core.ScalarUnit`
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
S        ``25812.8074434/(R_K*cyc)``                            *True*     `siemens <http://en.wikipedia.org/wiki/Siemens_(unit)>`_ (aka mho)
mol      ``96485.3365*Wb*cyc*S/k_F``                            *True*     `mole <http://en.wikipedia.org/wiki/Mole_(unit)>`_
K        ``8.3144621*(Wb*cyc)**2*S/(s*mol*R)``                  *True*     `kelvin <http://en.wikipedia.org/wiki/Kelvin>`_
------ Units decoupled from the base constants ------
---------------------------------------------------------------------------------------
cd       ``ScalarUnit(1., 'J')``                                *True*     `candela <http://en.wikipedia.org/wiki/Candela>`_ (decoupled from the base constants by the `luminosity function <http://en.wikipedia.org/wiki/Luminosity_function>`_)
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
ohm      ``S**-1``                                              *True*     `ohm <http://en.wikipedia.org/wiki/Ohm>`_
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
*Hg*     ``13.5951*g*g_0/cc``                                              force per volume of `mercury <http://en.wikipedia.org/wiki/Mercury_(element)>`_ under `standard gravity`_ [#f1]_, [#f2]_
mmHg     ``mm*Hg``                                              *False*    `millimeter of mercury <http://en.wikipedia.org/wiki/Millimeter_of_mercury>`_
bar      ``100*kPa``                                            *True*     `bar <http://en.wikipedia.org/wiki/Bar_(unit)>`_
b        ``100*fm**2``                                          *False*    `barn <http://en.wikipedia.org/wiki/Barn_(unit)>`_
angstrom ``0.1*nm``                                             *False*    `angstrom <http://en.wikipedia.org/wiki/Angstrom>`_
nmi      ``1852*m``                                             *False*    `nautical mile <http://en.wikipedia.org/wiki/Nautical_mile>`_
kn       ``nmi/hr``                                             *False*    `knot <http://en.wikipedia.org/wiki/Knot_(unit)>`_
Np       ``(exp, log)``                                         *False*    `neper <http://en.wikipedia.org/wiki/Neper>`_ (in terms of amplitude ratio, not power ratio)
B        ``(lambda n: 10**n, log10)``                           *True*     bel (in terms of power ratio, not amplitude ratio)
dB       ``dB``                                                 *False*    `decibel <http://en.wikipedia.org/wiki/Decibel>`_ (explicitly included with prefix)
------ Non-SI units associated with CGS and CGS-Gaussian system of units (BIPM2006_, Table 9) ------
---------------------------------------------------------------------------------------
cm       ``cm``                                                 *False*    `centimetre <http://en.wikipedia.org/wiki/Centimetre>`_ [#f3]_
Gal      ``cm/s**2``                                            *True*     `gal <http://en.wikipedia.org/wiki/Gal_(unit)>`_ (unit of acceleration)
dyn      ``g*Gal``                                              *True*     `dyne <http://en.wikipedia.org/wiki/Dyne>`_ (unit of force)
erg      ``dyn*cm``                                             *True*     `erg <http://en.wikipedia.org/wiki/Erg>`_ (unit of energy)
Ba       ``dyn/cm**2``                                          *True*     `barye <http://en.wikipedia.org/wiki/Barye>`_ (aka barad, barrie, bary, baryd, baryed, or barie; unit of pressure) [#f2]_
P        ``Ba*s``                                               *True*     `poise <http://en.wikipedia.org/wiki/Poise>`_ (unit of dynamic viscosity)
St       ``cm**2/s``                                            *True*     `stokes <http://en.wikipedia.org/wiki/Stokes_(unit)>`_ (aka stoke; unit of kinematic viscosity)
sb       ``cd/cm**2``                                           *True*     `stilb <http://en.wikipedia.org/wiki/Stilb_(unit)>`_ (unit of luminance)
ph       ``sb*sr``                                              *True*     `phot <http://en.wikipedia.org/wiki/Phot>`_ (unit of illuminance)
abA      ``daA``                                                *True*     `abampere <https://en.wikipedia.org/wiki/Abampere>`_ (aka decaampere or Biot (Bi)) [#f2]_
Mx       ``erg/(abA*cyc)``                                      *True*     `maxwell <http://en.wikipedia.org/wiki/Maxwell_(unit)>`_ (unit of magnetic flux)
Gs       ``Mx/cm**2``                                           *True*     `gauss <http://en.wikipedia.org/wiki/Gauss_(unit)>`_ (unit of magnetic flux density)
pole     ``4*pi*Mx``                                            *False*    unit pole [#f2]_
Oe       ``dyn/pole``                                           *True*     `oersted <http://en.wikipedia.org/wiki/Oersted>`_ (unit of the auxiliary magnetic field)
======== ====================================================== ========== ============

Since angle is explicit, some definitions are different than in [BIPM2006]_ and
[NIST2014]_:

- m ≈ 10973732 cyc *R_inf*\ :superscript:`-1` (i.e.,
  *R_inf* ≈ 10973732 cyc m\ :superscript:`-1`) [#f4]_
- S ≈ 25813 *R_K*\ :superscript:`-1` cyc\ :superscript:`-1` (i.e.,
  *R_K* ≈ 25813 ohm cyc\ :superscript:`-1`) [#f4]_
- Hz = cyc s\ :superscript:`-1` [#f5]_
- V = Wb Hz (i.e., Wb = V s cyc\ :superscript:`-1`) [#f5]_
- H = ohm s = V s A\ :superscript:`-1`
  (H ≠ Wb A\ :superscript:`-1`)

Note that frequency can be expressed in Hz or rad s\ :superscript:`-1` but not
s\ :superscript:`-1`.  Torque can be expressed in N m rad\ :superscript:`-1` or
J rad\ :superscript:`-1` but not N m or J.  Also note that the `steradian
(sr)`_, a unit of `solid angle`_, has dimension A\ :superscript:`2`.

deg, arcmin, and arcsec are used as the symbols for the degree_, arcminute_, and
arcsecond_ since the symbols in Table 6 of [BIPM2006]_ are not valid Python
names.  hr is used as the symbol for the hour_ (instead of h per [BIPM2006]_)
since *h* is used for the `Planck constant`_.  nmi is used as the symbol for
nautical mile (instead of M per [BIPM2006]_) since M is used for the `unit
molar`_.   Gs is used as the symbol for
the gauss mile (instead of G per [BIPM2006]_) since G is used as the
`gravitational constant`_.

In general, prefixes are not included because they are added upon access.
However, [BIPM2006]_ (and BIPM.ini_) includes two units with explicit prefixes:
kg and dB.


.. _BIPM.ini: https://github.com/kdavies4/natu/blob/master/natu/config/BIPM.ini
.. _System International (SI) units: http://en.wikipedia.org/wiki/International_System_of_Units
.. _steradian (sr): http://en.wikipedia.org/wiki/Steradian
.. _henry (H): http://en.wikipedia.org/wiki/Henry_(unit)
.. _solid angle: http://en.wikipedia.org/wiki/Solid_angle
.. _Planck constant: http://en.wikipedia.org/wiki/Planck_constant
.. _unit molar: http://en.wikipedia.org/wiki/Molar_concentration#Units

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
.. [#f3] not included in Table 9, but explicitly provided since this is a CGS base unit
.. [#f4] Traditionally, angle is dropped [NIST2014]_.
.. [#f5] Angle is dropped in [BIPM2006]_.
