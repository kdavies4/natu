Base constants (base-\*.ini)
============================

The tables below list the physical constants which are defined in the
:file:`base-*.ini` files.  All other constants and units are derived from these
[#f1]_, and they can be charged to establish various unit systems.

The derived electromagnetic constants also depend on the *rational* setting.  If
*rational* is *True*, the constants are rationalized
(``epsilon_0 = 1/(4*pi*k_C)``) ala Lorentz-Heaviside_; otherwise,
``epsilon_0 = 1/k_C`` like the `Gaussian units`_.

The definitions depend on the following items:

- Classes: :class:`~natu.core.Quantity`
- Mathematical constants: *pi*

The default is the `SI unit system`_ (base-SI.ini_), with the following
definitions:

========== =============================================================== ============
Symbol     Expression                                                      Name & notes
========== =============================================================== ============
------ Base physical constants ------
---------------------------------------------------------------------------------------
*R_inf*    ``Quantity(10973731.568539*2*pi, 'A/L', 'cyc/m')``              `Rydberg constant <http://en.wikipedia.org/wiki/Rydberg_constant>`_
*c*        ``Quantity(299792458, 'L/T', 'm/s')``                           `speed of light <http://en.wikipedia.org/wiki/Speed_of_light>`_ (aka Planck, Stoney, or natural unit of velocity)
*k_J*      ``Quantity(483597.870e9*2*pi, 'A*I*T2/(L2*M)', '1/Wb')``        `Josephson constant <http://en.wikipedia.org/wiki/Josephson_constant>`_
*R_K*      ``Quantity(25812.8074434/(2*pi), 'L2*M/(A*I2*T3)', 'ohm/cyc')`` `von Klitzing constant <http://en.wikipedia.org/wiki/Von_Klitzing_constant>`_
*k_F*      ``Quantity(96485.3365, 'I*T/N', 'C/mol')``                      `Faraday constant <http://en.wikipedia.org/wiki/Faraday_constant>`_
*R*        ``Quantity(8.3144621, 'L2*M/(N*T2*Theta)', 'J/(mol*K)')``       `gas constant <http://en.wikipedia.org/wiki/Gas_constant>`_
*k_Aprime* ``Quantity(2*pi, 'A', 'rad')*R_K/c``                            modified Ampere constant (``k_A*cyc/alpha``)
------ Settings ------
---------------------------------------------------------------------------------------
*rational* *True*                                                          *True* if the unit system is rationalized
========== =============================================================== ============

The second argument of the :class:`~natu.core.Quantity` constructor is
comprised of SI_ dimensions (current (I), length (L), mass (M), amount (N),
time (T), temperature (Theta)) and an additional dimension to track angle (A).
The value of *k_Aprime* for SI_ and most of the other unit systems is chosen so
that the radian_ (rad) has a value of one as defined by [BIPM2006]_.\ [#f2]_
However, this is not possible in the `Planck unit system`_, so the `Josephson
constant`_ is (arbitrarily) given a value of one instead.\ [#f3]_

For the ESU_ and Gaussian_ unit systems (base-ESU.ini_):

========== ===================================================================== ============
Symbol     Expression                                                            Name & notes
========== ===================================================================== ============
------ Base physical constants ------
---------------------------------------------------------------------------------------------
*R_inf*    ``Quantity(109737.31568539*2*pi, 'A/L', 'cyc/cm')``                   `Rydberg constant <http://en.wikipedia.org/wiki/Rydberg_constant>`_
*c*        ``Quantity(29979245800, 'L/T', 'cm/s')``                              `speed of light <http://en.wikipedia.org/wiki/Speed_of_light>`_ (aka Planck, Stoney, or natural unit of velocity)
*k_J*      ``Quantity(4835978.70*2*pi, 'A*T/(L(3/2)*M(1/2))', 's/(statT*cm3)')`` `Josephson constant <http://en.wikipedia.org/wiki/Josephson_constant>`_
*R_K*      ``Quantity(25812.8074434e9/(2*pi), 'L/(A*T)', 'cm/(s*cyc)')``         `von Klitzing constant <http://en.wikipedia.org/wiki/Von_Klitzing_constant>`_
*k_F*      ``Quantity(9648.53365, 'M(1/2)*L(1/2)/N', 'g(1/2)*cm(1/2)/mol')``     `Faraday constant <http://en.wikipedia.org/wiki/Faraday_constant>`_
*R*        ``Quantity(8.3144621e7, 'L2*M/(N*T2*Theta)', 'erg/(mol*K)')``         `gas constant <http://en.wikipedia.org/wiki/Gas_constant>`_
*k_Aprime* ``Quantity(2*pi, 'A', 'cyc')*R_K/c``                                  modified Ampere constant (``k_A*cyc/alpha``)
------ Settings ------
---------------------------------------------------------------------------------------------
*rational* *False*                                                               *True* if the unit system is rationalized
========== ===================================================================== ============

The same values are used for both of these unit systems.  The difference is in
how `Maxwell's equations`_ are expressed, not in the definition of the constants
and units.  The `Lorentz-Heaviside unit system`_ can be established with the
same constants but with *rational* = *True*.

For the `electromagnetic unit (EMU) system`_ (base-EMU.ini_):

========== =============================================================== ============
Symbol     Expression                                                      Name & notes
========== =============================================================== ============
------ Base physical constants ------
---------------------------------------------------------------------------------------
*R_inf*    ``Quantity(109737.31568539*2*pi, 'A/L', 'cyc/cm')``             `Rydberg constant <http://en.wikipedia.org/wiki/Rydberg_constant>`_
*c*        ``Quantity(29979245800, 'L/T', 'cm/s')``                        `speed of light <http://en.wikipedia.org/wiki/Speed_of_light>`_ (aka Planck, Stoney, or natural unit of velocity)
*k_J*      ``Quantity(4835978.70*2*pi, 'A*T/(L(3/2)*M(1/2))', '1/Mx')``    `Josephson constant <http://en.wikipedia.org/wiki/Josephson_constant>`_
*R_K*      ``Quantity(25812.8074434e9/(2*pi), 'L/(A*T)', 'cm/(s*cyc)')``   `von Klitzing constant <http://en.wikipedia.org/wiki/Von_Klitzing_constant>`_
*k_F*      ``Quantity(9648.53365, 'L(1/2)*M(1/2)/N', 'abC*s/(cm*mol)')*c`` `Faraday constant <http://en.wikipedia.org/wiki/Faraday_constant>`_
*R*        ``Quantity(8.3144621e7, 'L2*M/(N*T2*Theta)', 'erg/(mol*K)')``   `gas constant <http://en.wikipedia.org/wiki/Gas_constant>`_
*k_Aprime* ``Quantity(2*pi, 'A', 'cyc')*R_K/c``                            modified Ampere constant (``k_A*cyc/alpha``)
------ Settings ------
---------------------------------------------------------------------------------------
*rational* *False*                                                         *True* if the unit system is rationalized
========== =============================================================== ============

The next two unit systems are fully `natural
<http://en.wikipedia.org/wiki/Natural_units>`_, so all of the quantities are
dimensionless.  In the definitions, floating point numbers are used instead of
the :class:`~natu.core.Quantity` class.

For the `Hartree unit system`_ (base-Hartree.ini_):

========== ================================= ============
Symbol     Expression                        Name & notes
========== ================================= ============
------ Base physical constants ------
---------------------------------------------------------
*R_inf*    ``299792458e-7*pi/25812.8074434`` `Rydberg constant <http://en.wikipedia.org/wiki/Rydberg_constant>`_
*c*        ``1/(2*R_inf)``                   `speed of light <http://en.wikipedia.org/wiki/Speed_of_light>`_ (aka Planck, Stoney, or natural unit of velocity)
*k_J*      ``2``                             `Josephson constant <http://en.wikipedia.org/wiki/Josephson_constant>`_
*R_K*      ``2``                             `von Klitzing constant <http://en.wikipedia.org/wiki/Von_Klitzing_constant>`_
*k_F*      ``1``                             `Faraday constant <http://en.wikipedia.org/wiki/Faraday_constant>`_
*R*        ``k_F``                           `gas constant <http://en.wikipedia.org/wiki/Gas_constant>`_
*k_Aprime* ``2*pi*R_K/c``                    modified Ampere constant (``k_A*cyc/alpha``)
------ Settings ------
---------------------------------------------------------
*rational* *False*                           *True* if the unit system is rationalized
========== ================================= ============

For the `Planck unit system`_ (base-Planck.ini_):

========== ======================================================================================================= ============
Symbol     Expression                                                                                              Name & notes
========== ======================================================================================================= ============
------ Base physical constants ------
-------------------------------------------------------------------------------------------------------------------------------
G          ``1``                                                                                                   `gravitational constant <https://en.wikipedia.org/wiki/Gravitational_constant>`_
*c*        ``1``                                                                                                   `speed of light <http://en.wikipedia.org/wiki/Speed_of_light>`_ (aka Planck, Stoney, or natural unit of velocity)
*k_J*      ``1``                                                                                                   `Josephson constant <http://en.wikipedia.org/wiki/Josephson_constant>`_
*R_K*      ``sqrt(25812.8074434/(2*299792458*1e-7))/(pi*k_J)``                                                     `von Klitzing constant <http://en.wikipedia.org/wiki/Von_Klitzing_constant>`_
*k_F*      ``1``                                                                                                   `Faraday constant <http://en.wikipedia.org/wiki/Faraday_constant>`_
*R*        ``k_F*k_J*R_K*sqrt(pi)``                                                                                `gas constant <http://en.wikipedia.org/wiki/Gas_constant>`_
*k_Aprime* ``2*(pi*k_J*R_K)**2/c``                                                                                 modified Ampere constant (``k_A*cyc/alpha``)
------ Empirical ------
-------------------------------------------------------------------------------------------------------------------------------
*R_inf*    ``10973731.568539*k_J*c**2*sqrt(k_Aprime*6.67384e-11/(G*R_K*25812.8074434*299792458**3))/483597.870e9`` `Rydberg constant <http://en.wikipedia.org/wiki/Rydberg_constant>`_
------ Derived ------
-------------------------------------------------------------------------------------------------------------------------------
*l_P*      ``sqrt(k_Aprime*G/2)/(c*k_J*R_K*pi)``                                                                   `Planck length <https://en.wikipedia.org/wiki/Planck_length>`_
*M_P*      ``l_P*c**2/G``                                                                                          `Planck mass <https://en.wikipedia.org/wiki/Planck_mass>`_
*t_P*      ``l_P/c``                                                                                               `Planck time <https://en.wikipedia.org/wiki/Planck_time>`_
*E_P*      ``M_P*c**2``                                                                                            `Planck energy <http://en.wikipedia.org/wiki/Planck_energy>`_
*T_P*      ``E_P*k_F*k_J*R_K*sqrt(pi)/R``                                                                          `Planck temperature <https://en.wikipedia.org/wiki/Planck_temperature>`_
------ Settings ------
-------------------------------------------------------------------------------------------------------------------------------
*rational* *True*                                                                                                  *True* if the unit system is rationalized
========== ======================================================================================================= ============

Note that the `gravitational constant`_ is included as a base constant.  The
`Rydberg constant`_ is no longer a base constant but is empirically related to
the base constants.


.. _SI: http://en.wikipedia.org/wiki/International_System_of_Units
.. _SI unit system: http://en.wikipedia.org/wiki/International_System_of_Units
.. _Lorentz-Heaviside: http://en.wikipedia.org/wiki/Lorentz%E2%80%93Heaviside_units
.. _Lorentz-Heaviside unit system: http://en.wikipedia.org/wiki/Lorentz%E2%80%93Heaviside_units
.. _Gaussian: http://en.wikipedia.org/wiki/Gaussian_units
.. _Gaussian units: http://en.wikipedia.org/wiki/Gaussian_units
.. _CGS: http://en.wikipedia.org/wiki/Centimetre%E2%80%93gram%E2%80%93second_system_of_units
.. _ESU: http://en.wikipedia.org/wiki/Centimetre%E2%80%93gram%E2%80%93second_system_of_units#Electrostatic_units_.28EMU.29
.. _electromagnetic unit (EMU) system: http://en.wikipedia.org/wiki/Centimetre%E2%80%93gram%E2%80%93second_system_of_units#Electromagnetic_units_.28EMU.29
.. _Hartree unit system: http://en.wikipedia.org/wiki/Atomic_units
.. _Planck unit system: http://en.wikipedia.org/wiki/Planck_units
.. _Maxwell's equations: http://en.wikipedia.org/wiki/Maxwell's_equations
.. _radian: http://en.wikipedia.org/wiki/Radian
.. _hertz: http://en.wikipedia.org/wiki/Hertz

.. _base-SI.ini: https://github.com/kdavies4/natu/blob/master/natu/config/base-SI.ini
.. _base-ESU.ini: https://github.com/kdavies4/natu/blob/master/natu/config/base-ESU.ini
.. _base-EMU.ini: https://github.com/kdavies4/natu/blob/master/natu/config/base-EMU.ini
.. _base-Hartree.ini: https://github.com/kdavies4/natu/blob/master/natu/config/base-Hartree.ini
.. _base-Planck.ini: https://github.com/kdavies4/natu/blob/master/natu/config/base-Planck.ini

.. rubric:: References

.. [BIPM2006] International Bureau of Weights and Measures (BIPM),
              "`The International System of Units (SI)
              <http://www.bipm.org/utils/common/pdf/si_brochure_8_en.pdf>`_,"
              8th ed., 2006.

.. rubric:: Footnotes

.. [#f1] ... except for the `candela (cd)
   <https://en.wikipedia.org/wiki/Candela>`_, which is not directly related due
   to the `luminosity function
   <https://en.wikipedia.org/wiki/Luminosity_function>`_.
.. [#f2] However, note that there is a contradiction in the `SI unit system`_.
   Since rad = 1, it should follow that a cycle or revolution is 2\*\ *pi*, yet
   [BIPM2006]_ defines the hertz_ (generally accepted as cycles per second) as
   1/s.
.. [#f3] When considering angle as a dimension, the `Planck unit system`_ only
   places a constraint on the product of the `Josephson constant`_ and the `von
   Klitzing constant`_, not on either constant individually.
