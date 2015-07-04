import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    n = int(test)
    if n % 2 == 0:
        print("1")
    else:
        print("0")

test_cases.close()