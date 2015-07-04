import sys
import string

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')


def swap_case(c):
    if c in string.ascii_lowercase:
        return c.upper()
    elif c in string.ascii_uppercase:
        return c.lower()
    else:
        return c

for test in test_cases:
    print("".join(map(swap_case, test.strip())))

test_cases.close()