import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    numbers = map(float, test.strip().split(" "))
    print(" ".join(map(lambda x: "%(number).3f" % {"number": x}, sorted(numbers))))

test_cases.close()