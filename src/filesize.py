import os
import sys

__author__ = 'Kirros'

print(str(os.stat(sys.argv[1]).st_size))