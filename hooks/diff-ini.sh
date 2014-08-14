#!/bin/bash
# Compare the \*-ini.rst files in the documenation to the corresponding \*.ini
# source files.
#
# If an argument is given, it is taken as the base filename to compare (without
# .ini or -ini.rst).  If no argument is given, then all of the files are
# compared.
#
# This requires Meld (http://meldmerge.org/).

if [[ $1 == '' ]]; then
    (cd doc
    for f in *-ini.rst; do
        meld ../natu/config/${f:0:${#f}-8}.ini $f
    done
    )
else
    meld natu/config/$1.ini doc/$1-ini.rst
fi
