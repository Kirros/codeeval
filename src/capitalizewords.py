import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print(" ".join(map(lambda x: x[0].upper() + x[1:], test.strip().split(" "))))

test_cases.close()