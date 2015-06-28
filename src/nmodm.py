import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    (n, m) = map(int, test.strip().split(","))
    i = n
    while i >= m:
        i -= m
    print(i)

test_cases.close()