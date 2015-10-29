import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip().split(' ')
    binary = ''
    for i in range(0, len(test), 2):
        if test[i] == '0':
            binary += test[i + 1]
        elif test[i] == '00':
            binary += '1' * len(test[i + 1])
    print(int(binary, 2))

test_cases.close()
