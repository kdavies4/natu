#!/usr/bin/python
"""Contains *PREFIXES*, a dictionary of SI prefixes
"""
# [BIPM2006]: International Bureau of Weights and Measures (BIPM), "The
#             International System of Units (SI)," 8th ed., 2006.

# [BIPM2006, Table 5]
PREFIXES = dict(Y=1e24,   # yotta
                Z=1e21,   # zetta
                E=1e18,   # exa
                P=1e15,   # peta
                T=1e12,   # tera
                G=1e9,    # giga
                M=1e6,    # mega
                k=1e3,    # kilo
                h=100,    # hecto
                da=10,    # deca
                d=0.1,    # deci
                c=0.01,   # centi
                m=1e-3,   # milli
                u=1e-6,   # micro
                n=1e-9,   # nano
                p=1e-12,  # pico
                f=1e-15,  # femto
                a=1e-18,  # atto
                z=1e-21,  # zepto
                y=1e-24)  # yocto
