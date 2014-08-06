#!/bin/bash
# Compare the \*-ini.rst files in the documenation to the corresponding \*.ini
# source files.
#
# This requires Meld (http://meldmerge.org/).

(cd doc
for f in *-ini.rst; do
    meld ../natu/config/${f:0:${#f}-8}.ini $f
done
)
