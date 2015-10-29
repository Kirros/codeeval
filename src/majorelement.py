import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    numbers = test.strip().split(',')
    mode = max(set(numbers), key=numbers.count)
    if numbers.count(mode) > len(numbers) / 2:
        print(mode)
    else:
        print('None')

test_cases.close()