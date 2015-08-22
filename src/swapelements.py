import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')


def swap(l, pos):
    temp = l[pos[0]]
    l[pos[0]] = l[pos[1]]
    l[pos[1]] = temp
    return l

for test in test_cases:
    (numbers, swaps) = test.strip().split(':')
    numbers = numbers.strip().split(' ')
    swaps = swaps.strip().split(', ')
    swaps = map(lambda x: tuple(map(int, x.split('-'))), swaps)
    for s in swaps:
        numbers = swap(numbers, s)
    print(' '.join(numbers))

test_cases.close()