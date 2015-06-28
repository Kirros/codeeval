import sys

__author__ = 'Kirros'


def happy_step(num):
    return sum(map(lambda x: int(x)**2, list(str(num))))


def is_happy(num):
    i = num
    results = []
    while i not in results:
        results.append(i)
        i = happy_step(i)
    if results[-1] == 1:
        return True
    else:
        return False


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    n = int(test)
    if is_happy(n):
        print("1")
    else:
        print("0")

test_cases.close()