Derived constants and units (derived.ini_)
==========================================

The table below lists the contents of the derived.ini_ file.  It contains
constants and units that are derived from the base physical constants.

The definitions depend on the following items:

- Mathematical constants: *pi*
- Base constants: *R_inf*, *c*, *k_J*, *R_K*, *k_F*, *R*, and *k_Aprime*

============ =========================== ========== ============
Symbol       Expression                  Prefixable Name & notes
============ =========================== ========== ============
------ Derived physical constants and intermediate units ------
----------------------------------------------------------------
*Phi_0*      ``1/k_J``                              `magnetic flux quantum <http://en.wikipedia.org/wiki/Magnetic_flux_quantum>`_
*G_0*        ``2/R_K``                              `conductance quantum <http://en.wikipedia.org/wiki/Conductance_quantum>`_
*e*          ``Phi_0*G_0``                          `elementary charge <http://en.wikipedia.org/wiki/Elementary_charge>`_ (aka Hartree unit of charge)
*h*          ``2*e*Phi_0``                          `Planck constant <http://en.wikipedia.org/wiki/Planck_constant>`_
*N_A*        ``k_F/e``                              `Avogadro constant <http://en.wikipedia.org/wiki/Avogadro_constant>`_
*k_B*        ``R/N_A``                              `Boltzmann constant <http://en.wikipedia.org/wiki/Boltzmann_constant>`_
cyc          ``k_Aprime*c/R_K``          *False*    cycle (aka circle, revolution, `turn <http://en.wikipedia.org/wiki/Turn_(geometry)>`_) (a unit---not a constant---but useful below)
*c_1*        ``2*pi*h*c**2/cyc**3``                 `first radiation constant <http://physics.nist.gov/cgi-bin/cuu/Value?c11strc>`_
*c_2*        ``h*c/k_B``                            `second radiation constant <http://physics.nist.gov/cgi-bin/cuu/Value?c22ndrc|search_for=second+radiation>`_
*c_3_f*      ``2.821439372122079*c/c_2``            `Wien frequency displacement constant <http://en.wikipedia.org/wiki/Wien's_displacement_law>`_ (the number is *x*, where exp(*x*)*(3 - *x*) = 3)
*c_3_lambda* ``c_2/4.965114231744276``              `Wien wavelength displacement constant <http://en.wikipedia.org/wiki/Wien's_displacement_law>`_ (the number is *x*, where exp(*x*)*(5 - *x*) = 5)
*sigma*      ``c_1/15*(pi/c_2)**4``                 `Stefan-Boltzmann constant <http://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_constant>`_ (aka Stefan's constant)
*Ry*         ``h*c*R_inf``                          `Rydberg energy <http://en.wikipedia.org/wiki/Rydberg_constant#Value_of_the_Rydberg_constant_and_Rydberg_unit_of_energy>`_
*Ha*         ``2*Ry``                               `Hartree energy <http://en.wikipedia.org/wiki/Hartree>`_ (aka hartree)
*T_H*        ``Ha/k_B``                             Hartree temperature
============ =========================== ========== ============

Since angle is explicit, it appears in several of the constants:

- *Phi_0* ≈ 2.068×10\ :superscript:`-15` Wb [#f1]_
- *G_0* ≈ 7.748×10\ :superscript:`-5` S cyc [#f2]_
- *h* ≈ 6.626×10\ :superscript:`-34` J Hz\ :superscript:`-1` [#f1]_
- *c_1* ≈ 3.742×10\ :superscript:`-16` W m\ :superscript:`2` cyc\ :superscript:`-4` [#f2]_
- *c_2* ≈ 1.438×10\ :superscript:`-2` m K cyc\ :superscript:`-1` [#f2]_
- *c_3_f* ≈ 5.879×10\ :superscript:`10` Hz K\ :superscript:`-1` [#f1]_
- *c_3_lambda* ≈ 2.898×10\ :superscript:`-3` K m cyc\ :superscript:`-1` [#f2]_

The definition of the `Planck constant`_ implies that
*h*\*cyc ≈ 6.626×10\ :superscript:`-34` J (the traditional expression of
*h*) and *h*\*rad ≈ 1.05457×10\ :superscript:`-34` J (the traditional
expression of *ħ*).  Note that the cycle (cyc) is not an abbreviation for cycles
per second as it became in the `MKS system of units
<https://en.wikipedia.org/wiki/MKS_system_of_units>`_.  It is a unit of angle.


.. _derived.ini: https://github.com/kdavies4/natu/blob/master/natu/config/derived.ini
.. _Planck constant: http://en.wikipedia.org/wiki/Planck_constant

.. rubric:: References

.. [NIST2014] National Institute of Science and Technology, "Fundamental
              Physical Constants: Complete Listing,"
              http://physics.nist.gov/constants, accessed 2014.

.. rubric:: Footnotes

.. [#f1] See the `BIPM units <BIPM-ini.html>`_ regarding the weber (Wb) and the
   hertz (Hz).
.. [#f2] Traditionally, angle is dropped [NIST2014]_.
