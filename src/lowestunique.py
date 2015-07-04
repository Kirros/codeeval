import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    numbers = list(map(int, test.strip().split(' ')))
    unique = list(filter(lambda x: numbers.count(x) == 1, numbers))
    if unique == []:
        print('0')
        continue
    lowest = sorted(unique)[0]
    print(numbers.index(lowest) + 1)

test_cases.close()