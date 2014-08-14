#!/usr/bin/python
"""Set up the natu package.

See README.md for instructions.
"""

# pylint: disable=C0103

import re

from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'natu', '__init__.py')) as f:
    hit = re.search('__version__ *= *["'"'"'](.*)["'"'"']', f.read())
    try:
        version = hit.group(1)
    except AttributeError:
        version = None

with open(path.join(here, 'doc/long-description.txt')) as f:
    long_description = f.read()

setup(name='natu',
      version=version if version else '0',
      description="Natural units in Python",
      long_description=long_description,
      author='Kevin Davies',
      author_email='kdavies4@gmail.com',
      license='BSD-compatible (see LICENSE.txt)',
      keywords='quantity quantities unit conversion natural SI CGS Planck Hartree',
      url='http://kdavies4.github.io/natu/',
      download_url=('https://github.com/kdavies4/natu/archive/v%s.zip'
                    % version if version else ''),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Intended Audience :: Education',
          'Topic :: Scientific/Engineering',
          'Topic :: Software Development :: Quality Assurance',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Microsoft :: Windows',
      ],
      provides=['natu'],
      packages=['natu', 'natu.config', 'natu.groups'],
      package_data={'natu.config': ['*.ini']},
      platforms='any',
      zip_safe=False, # because ini files must be accessed
      test_suite = 'tests.test_suite',
     )
