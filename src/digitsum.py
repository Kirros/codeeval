import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print(sum(map(int, list(test.strip()))))

test_cases.close()