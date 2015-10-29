import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    lower = 0
    upper = 0
    for char in test:
        if char.isupper():
            upper += 1
        else:
            lower += 1
    print("lowercase: %.2f uppercase: %.2f" % (lower / len(test) * 100, upper / len(test) * 100))

test_cases.close()
