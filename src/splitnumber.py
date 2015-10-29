import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')


def decode(numbers, pattern):
    return int(''.join(map(lambda x: numbers[ord(x) - ord('a')], pattern)))

for test in test_cases:
    (numbers, pattern) = test.strip().split(' ')
    adding = False
    if '+' in pattern:
        adding = True
        (first, second) = pattern.split('+')
    else:
        (first, second) = pattern.split('-')
    first = decode(numbers, first)
    second = decode(numbers, second)
    if adding:
        print(str(first + second))
    else:
        print(str(first - second))


test_cases.close()