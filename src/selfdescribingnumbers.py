import sys

__author__ = 'Kirros'


def is_self_describing(num):
    for digit in range(0, len(num)):
        if int(num[digit]) != num.count(str(digit)):
            return False
    return True


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    i = test.strip()
    if is_self_describing(i):
        print("1")
    else:
        print("0")

test_cases.close()