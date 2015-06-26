import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    (x, n) = tuple(map(int,test.strip().split(",")))
    result = n
    while result < x:
        result += n
    print(result)

test_cases.close()