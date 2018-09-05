"""
Back compatibility noseclasses module. It will import the appropriate
set of tools
"""
from __future__ import division, absolute_import, print_function

import warnings

# 2018-04-04, numpy 1.15.0
warnings.warn("Importing from numpy.testing.noseclasses is deprecated, "
              "import from numpy.testing instead",
              DeprecationWarning)

from ._private.noseclasses import *
