import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')


def turn(current, next):
    if current == next:
        return '|'
    if current < next:
        return '\\'
    else:
        return '/'

first_line = True
current_track = 0
for test in test_cases:
    if 'C' in test:
        next_track = test.index('C')
        if first_line:
            print(test.replace('C', '|'))
            first_line = False
        else:
            print(test.replace('C', turn(current_track, next_track)))
    else:
        next_track = test.index('_')
        if first_line:
            print(test.replace('_', '|'))
            first_line = False
        else:
            print(test.replace('_', turn(current_track, next_track)))
    current_track = next_track

test_cases.close()