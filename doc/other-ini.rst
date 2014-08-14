:orphan:

Other units and constants (other.ini_)
======================================

The table below lists the contents of the other.ini_ file.  It establishes some
units besides the SI_ and non-SI units from [BIPM2006]_.

The definitions below depend on the following items:

- Mathematical constants: *pi*
- Base physical constants: *c*
- SI_ and non-SI units from [BIPM2006]_
- Other units and constants: cyc and *g_0*

=========== ============================================================ ========== =============
Symbol      Expression                                                   Prefixable Name & notes
=========== ============================================================ ========== =============
------ Time ------
-------------------------------------------------------------------------------------------------
y           ``365.25*d``                                                 *False*    `Julian year <http://en.wikipedia.org/wiki/Julian_year_(astronomy)>`_
------ Length ------
-------------------------------------------------------------------------------------------------
ly          ``c*y``                                                      *True*     `light year <http://en.wikipedia.org/wiki/Light_year>`_
au          ``149597870700*m``                                           *False*    `astronomical unit <http://en.wikipedia.org/wiki/Astronomical_unit>`_
pc          ``au*648e3/pi``                                              *False*    `parsec <http://en.wikipedia.org/wiki/Parsec>`_
inch        ``2.54*cm``                                                  *False*    `inch <http://en.wikipedia.org/wiki/Inch>`_
ft          ``12*inch``                                                  *False*    `foot <http://en.wikipedia.org/wiki/Foot_(unit)>`_
yd          ``3*ft``                                                     *False*    `yard <http://en.wikipedia.org/wiki/Yard_(unit)>`_
mi          ``1760*yd``                                                  *False*    `mile <http://en.wikipedia.org/wiki/Mile>`_
pica        ``inch/6``                                                   *False*    `pica <http://en.wikipedia.org/wiki/Pica_(typography)>`_
point       ``pica/12``                                                  *False*    `point <http://en.wikipedia.org/wiki/Point_(typography)>`_
------ Mass ------
-------------------------------------------------------------------------------------------------
u           ``g/(N_A*mol)``                                              *True*     `unified atomic mass unit <https://en.wikipedia.org/wiki/Atomic_mass_unit>`_ (aka dalton (Da))
oz          ``28.349523125*g``                                           *False*    `avoirdupois ounce <http://en.wikipedia.org/wiki/Ounce#International_avoirdupois_ounce>`_
lb          ``16*oz``                                                    *False*    `pound <http://en.wikipedia.org/wiki/Pound_(mass)>`_
ton         ``2e3*lb``                                                   *False*    `short ton <http://en.wikipedia.org/wiki/Short_ton>`_
------ Force ------
-------------------------------------------------------------------------------------------------
lbf         ``lb*g_0``                                                   *False*    `pound force <http://en.wikipedia.org/wiki/Pound_force>`_
kip         ``1000*lbf``                                                 *False*    `kip <http://en.wikipedia.org/wiki/Kip_(unit)>`_
------ Pressure ------
-------------------------------------------------------------------------------------------------
atm         ``101325*Pa``                                                *False*    `atmosphere <http://en.wikipedia.org/wiki/Atmosphere_(unit)>`_
Pag         ``(lambda n: n*Pa + atm, lambda p: (p - atm)/Pa)``           *True*     pascal, gauge
psi         ``lbf/inch**2``                                              *False*    `pounds per square inch <http://en.wikipedia.org/wiki/Pounds_per_square_inch>`_
psig        ``(lambda n: n*psi + atm, lambda p: (p - atm)/psi)``         *False*    pounds per square inch, gauge
Torr        ``atm/760``                                                  *False*    `torr <http://en.wikipedia.org/wiki/Torr>`_
------ Energy ------
-------------------------------------------------------------------------------------------------
BTU         ``1055.05585262*J``                                          *True*     `British thermal unit <http://en.wikipedia.org/wiki/British_thermal_unit>`_, based on International Steam Table calorie [IT1956]_
cal         ``4.184*J``                                                  *True*     `small calorie <http://en.wikipedia.org/wiki/Small_calorie>`_ (thermochemical)
Cal         ``kcal``                                                     *True*     large calorie (aka food calorie)
Wh          ``W*hr``                                                     *True*     `watt hour <http://en.wikipedia.org/wiki/Watt_hour>`_
eV          ``e*V``                                                      *True*     `electron volt <http://en.wikipedia.org/wiki/Electron_volt>`_
------ Power ------
-------------------------------------------------------------------------------------------------
hp          ``550*ft*lbf/s``                                             *False*    `mechanical horsepower <http://en.wikipedia.org/wiki/Horsepower#Mechanical_horsepower>`_
------ Area ------
-------------------------------------------------------------------------------------------------
ac          ``mi**2/640``                                               *False*    `acre <http://en.wikipedia.org/wiki/Acre>`_
------ Volume ------
-------------------------------------------------------------------------------------------------
gallon      ``231*inch**3``                                              *False*    `US gallon <http://en.wikipedia.org/wiki/US_gallon>`_
qt          ``gallon/4``                                                 *False*    `US quart <http://en.wikipedia.org/wiki/US_quart#United_States_liquid_quart>`_
pt          ``qt/2``                                                     *False*    `US pint <http://en.wikipedia.org/wiki/US_pint>`_
cup         ``pt/2``                                                     *False*    `US cup <http://en.wikipedia.org/wiki/Cup_(unit)#United_States_customary_cup>`_
fluid_oz    ``cup/8``                                                    *False*    `US fluid ounce <http://en.wikipedia.org/wiki/US_fluid_ounce>`_
bbl         ``42*gallon``                                                *False*    `oil barrel <http://en.wikipedia.org/wiki/Oil_barrel#Oil_barrel>`_
------ Angle ------
-------------------------------------------------------------------------------------------------
grad        ``cyc/400``                                                  *False*    `gradian <http://en.wikipedia.org/wiki/Gradian>`_
sign        ``rad/6``                                                    *False*
sextant     ``cyc/6``                                                    *False*
quadrant    ``cyc/4``                                                    *False*
------ Solid angle ------
-------------------------------------------------------------------------------------------------
sp          ``4*pi*sr``                                                  *False*    `spat <http://en.wikipedia.org/wiki/Spat_(unit)>`_
------ Velocity ------
-------------------------------------------------------------------------------------------------
mph         ``mi/hr``                                                    *False*    `miles per hour <http://en.wikipedia.org/wiki/Miles_per_hour>`_
kph         ``km/hr``                                                    *False*    `kilometres per hour <http://en.wikipedia.org/wiki/Kilometers_per_hour>`_
------ Frequency/Angular velocity ------
-------------------------------------------------------------------------------------------------
rpm         ``cyc/min``                                                  *False*    `revolution per minute <http://en.wikipedia.org/wiki/Revolutions_per_minute>`_
------ Temperature ------
-------------------------------------------------------------------------------------------------
degR        ``K*5/9``                                                    *False*    `degree Rankine <http://en.wikipedia.org/wiki/Rankine_scale>`_
degF        ``(lambda n: (n + 459.67)*degR, lambda T: T/degR - 459.67)`` *False*    `degree Fahrenheit <http://en.wikipedia.org/wiki/Fahrenheit>`_
------ Dimensionless ------
-------------------------------------------------------------------------------------------------
pct         ``0.01``                                                     *False*    `percent <http://en.wikipedia.org/wiki/Percent>`_ (%)
ppm         ``1e-6``                                                     *False*    `parts per million <http://en.wikipedia.org/wiki/Parts_per_million>`_
ppb         ``1e-9``                                                     *False*    `parts per billion <http://en.wikipedia.org/wiki/Parts_per_billion>`_
ppt         ``1e-12``                                                    *False*    `parts per trillion <http://en.wikipedia.org/wiki/Parts_per_trillion>`_
ppq         ``1e-15``                                                    *False*    `parts per quadrillion <http://en.wikipedia.org/wiki/Parts_per_quadrillion>`_
------ `CGS units`_ (general) ------
-------------------------------------------------------------------------------------------------
cm          ``cm``                                                       *False*    `centimetre <http://en.wikipedia.org/wiki/Centimetre>`_
gal         ``cm/s**2``                                                  *True*     `gal <http://en.wikipedia.org/wiki/Gal_(unit)>`_ (unit of acceleration)
dyn         ``g*gal``                                                    *True*     `dyne <http://en.wikipedia.org/wiki/Dyne>`_ (unit of force)
erg         ``dyn*cm``                                                   *True*     `erg <http://en.wikipedia.org/wiki/Erg>`_ (unit of energy)
Ba          ``dyn/cm**2``                                                *True*     `barye <http://en.wikipedia.org/wiki/Barye>`_ (aka barad, barrie, bary, baryd, baryed, or barie; unit of pressure)
P           ``Ba*s``                                                     *True*     `poise <http://en.wikipedia.org/wiki/Poise>`_ (unit of dynamic viscosity)
St          ``cm**2/s``                                                  *True*     `stokes <http://en.wikipedia.org/wiki/Stokes_(unit)>`_ (aka stoke; unit of kinematic viscosity)
------ CGS units (EMU_) ------
-------------------------------------------------------------------------------------------------
abA         ``daA``                                                      *True*     `abampere <https://en.wikipedia.org/wiki/Abampere>`_ (aka decaampere or Biot (Bi))
abC         ``abA*s``                                                    *True*     `abcoloumb <https://en.wikipedia.org/wiki/Abcoulomb>`_
abV         ``erg/abC``                                                  *True*     `abvolt <https://en.wikipedia.org/wiki/Abvolt>`_
Mx          ``erg/(abA*cyc)``                                            *True*     `maxwell <http://en.wikipedia.org/wiki/Maxwell_(unit)>`_ (unit of magnetic flux)
Gs          ``Mx/cm**2``                                                 *True*     `gauss <http://en.wikipedia.org/wiki/Gauss_(unit)>`_ (unit of magnetic flux density)
pole        ``4*pi*Mx``                                                  *False*    unit pole
Oe          ``dyn/pole``                                                 *True*     `oersted <http://en.wikipedia.org/wiki/Oersted>`_ (unit of the auxiliary magnetic field)
abF         ``abC/abV``                                                  *True*     `abfarad <https://en.wikipedia.org/wiki/Abfarad#CGS_units>`_
abohm       ``s/abF``                                                    *True*     `abohm <https://en.wikipedia.org/wiki/Abohm>`_
abH         ``abohm*s``                                                  *True*     `abhenry <http://en.wikipedia.org/wiki/Abhenry>`_
------ CGS units (ESU_ and Gaussian_) ------
-------------------------------------------------------------------------------------------------
statC       ``sqrt(g*cc)/s``                                             *True*     `statcoulomb <https://en.wikipedia.org/wiki/Statcoulomb>`_ (aka franklin (Fr) or electrostatic unit (esu) of charge)
statA       ``statC/s``                                                  *True*     statampere
statV       ``erg/statC``                                                *True*     `statvolt <https://en.wikipedia.org/wiki/Statvolt>`_
statWb      ``statV/Hz``                                                 *True*     statweber
statT       ``statWb/cm**2``                                             *True*     stattesla
------ Constants related to `Ampere's force law`_ ------
-------------------------------------------------------------------------------------------------
*k_A*       ``dyn/abA**2``                                                          Ampere constant (aka magnetic force constant)
*k_C*       ``k_A*c**2``                                                            `Coulomb constant <https://en.wikipedia.org/wiki/Coulomb_constant>`_ (aka electric force constant or electrostatic constant)
*epsilon_0* ``1/(k_C*(4*pi if rational else 1))``                                   `electric constant <http://en.wikipedia.org/wiki/Vacuum_permittivity>`_ (aka vacuum permittivity or permittivity of free space)
*mu_0*      ``1/(epsilon_0*sr*c**2)``                                               `magnetic constant <http://en.wikipedia.org/wiki/Vacuum_permeability>`_ (aka vacuum permeability or permeability of free space)
*Z_0*       ``2*k_A*c/rad``                                                         `characteristic impedance of vacuum <http://en.wikipedia.org/wiki/Impedance_of_free_space>`_
*alpha*     ``k_A*c/R_K``                                                           `fine structure constant <http://en.wikipedia.org/wiki/Fine_structure_constant>`_
*a_0*       ``alpha/(2*R_inf)``                                                     `Bohr radius <https://en.wikipedia.org/wiki/Bohr_radius>`_ (aka Hartree length)
*lambda_e*  ``alpha*a_0/sr``                                                        electron `Compton wavelength <https://en.wikipedia.org/wiki/Compton_wavelength>`_
*kappa*     ``lambda_e*c/2``                                                        quantum of circulation
*m_e*       ``Phi_0/kappa``                                                         `electron rest mass per elementary charge <http://en.wikipedia.org/wiki/Electron_mass>`_
*r_e*       ``k_A/m_e``                                                             `classical electron radius per elementary charge <http://en.wikipedia.org/wiki/Classical_electron_radius>`_ (aka Lorentz radius or Thomson scattering length)
*mu_B*      ``kappa*e*sp/2``                                                        `Bohr magnetron <https://en.wikipedia.org/wiki/Bohr_magneton>`_
*M_e*       ``m_e*e``                                                               mass of an electron (aka Hartree mass)
*t_H*       ``a_0*sqrt(M_e/Ha)``                                                    Hartree time
*l_n*       ``h*rad/(M_e*c)``                                                       natural unit of length
*t_n*       ``l_n/c``                                                               natural unit of time
------ Misc. units and constants ------
-------------------------------------------------------------------------------------------------
AT          ``A*cyc``                                                    *False*    `ampere-turn <http://en.wikipedia.org/wiki/Ampere-turn>`_
D           ``cdyn/atm``                                                 *True*     `darcy <http://en.wikipedia.org/wiki/Darcy_(unit)>`_
M           ``mol/L``                                                    *True*     `molar <http://en.wikipedia.org/wiki/Molar_concentration#Units>`_
=========== ============================================================ ========== =============

Since angle is explicit, it appears in several of the constants and units:

- *mu_0* ≈ 4 *pi* 10\ :superscript:`-7` H m\ :superscript:`-1` cyc\ :superscript:`-2`
  [#f1]_
- *Z_0* ≈ 376.730 ohm cyc\ :superscript:`-1` [#f1]_
- *kappa* ≈ 3.637×10\ :superscript:`-4` m\ :superscript:`2` s\ :superscript:`-1` cyc\ :superscript:`-1`
  [#f1]_
- rpm = cyc min\ :superscript:`-1`
- sp = 4 *pi* sr
- AT = A cyc
- Oe = 5 kA rad m\ :superscript:`-1`
  = 0.25 kA cyc *pi*\ :superscript:`-1` m\ :superscript:`-1`
  = 250 AT *pi*\ :superscript:`-1` m\ :superscript:`-1`
- Mx = erg abA\ :superscript:`-1` cyc\ :superscript:`-1` = 10\ :superscript:`-8` V Hz\ :superscript:`-1` [#f2]_
- Gs = Mx cm\ :superscript:`2` = 10\ :superscript:`-4` Wb m\ :superscript:`-2`
  = 10\ :superscript:`-4` V Hz\ :superscript:`-1` m\ :superscript:`-2` [#f2]_
- statWb = statV Hz\ :superscript:`-1` [#f2]_
- statT = statWb cm\ :superscript:`2`
  = statV Hz\ :superscript:`-1` cm\ :superscript:`2` [#f2]_

Note that torque can be expressed in lbf ft rad\ :superscript:`-1` but not
lbf ft.


.. _other.ini: https://github.com/kdavies4/natu/blob/master/natu/config/other.ini
.. _SI: http://en.wikipedia.org/wiki/International_System_of_Units
.. _CGS units: <http://en.wikipedia.org/wiki/Centimetre%E2%80%93gram%E2%80%93second_system_of_units
.. _EMU: <http://en.wikipedia.org/wiki/Centimetre%E2%80%93gram%E2%80%93second_system_of_units#Electromagnetic_units_.28EMU.29
.. _ESU: <http://en.wikipedia.org/wiki/Electrostatic_units
.. _Gaussian: http://en.wikipedia.org/wiki/Gaussian_units
.. _Ampere's force law: <http://en.wikipedia.org/wiki/Amp%C3%A8re's_force_law

.. rubric:: References

.. [BIPM2006] International Bureau of Weights and Measures (BIPM),
              "`The International System of Units (SI)
              <http://www.bipm.org/utils/common/pdf/si_brochure_8_en.pdf>`_,"
              8th ed., 2006.
.. [IT1956]   *Fifth International Conference on the Properties of Steam*,
              London, July 1956.
.. [NIST2014] National Institute of Science and Technology, "Fundamental
              Physical Constants: Complete Listing,"
              http://physics.nist.gov/constants, accessed 2014.

.. rubric:: Footnotes

.. [#f1] Traditionally, angle is dropped [NIST2014]_.
.. [#f2] ... where Hz has dimension of angle per time.
