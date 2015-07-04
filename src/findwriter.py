import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')


for test in test_cases:
    code = test.strip().split("|")[1].strip().split(" ")
    print("".join(map(lambda x: test[int(x) - 1], code)))

test_cases.close()