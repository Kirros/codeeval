import math
import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    (pos1, pos2) = test.split(") (")
    (x1, y1) = pos1[1:].split(", ")
    (x2, y2) = pos2[:-2].split(", ")
    dist = math.sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)
    print(int(dist))

test_cases.close()