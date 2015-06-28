import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    n = int(test)
    m = sum(map(lambda x: int(x)**len(test), list(test)))
    print(n == m)

test_cases.close()