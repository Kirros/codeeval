import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    (S, t) = test.strip().split(",")
    print(S.rfind(t))

test_cases.close()