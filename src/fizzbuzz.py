__author__ = 'Kirros'
import sys


def fizz_buzz(x, y, i):
    if i % x == 0:
        if i % y == 0:
            return "FB"
        return "F"
    elif i % y == 0:
        return "B"
    else:
        return str(i)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        continue
    test = (tuple(map(int, test.split(" "))))
    print(" ".join(map(lambda x: fizz_buzz(test[0], test[1], x), range(1, test[2] + 1))))

test_cases.close()



