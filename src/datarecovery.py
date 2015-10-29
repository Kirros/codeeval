import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    (data, hints) = test.strip().split(';')
    data = data.split(' ')
    hints = list(map(int, hints.split(' ')))
    result = []
    for order in range(len(data)):
        if order + 1 not in hints:
            result.append(data[-1])
            continue
        result.append(data[hints.index(order + 1)])
    print(' '.join(result))

test_cases.close()
