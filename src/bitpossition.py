import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    (n, p1, p2) = tuple(map(int, test.strip().split(",")))
    print(str(((n & 2**(p1-1)) == 0) == ((n & 2**(p2-1)) == 0)).lower())

test_cases.close()