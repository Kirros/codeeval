import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    sequence = list(map(int, test.strip().split(' ')))
    current_num = sequence[0]
    count = 0
    compressed = []
    for n in sequence:
        if current_num == n:
            count += 1
        else:
            compressed.append(count)
            compressed.append(current_num)
            current_num = n
            count = 1
    compressed.append(count)
    compressed.append(current_num)
    print(' '.join(map(str, compressed)))

test_cases.close()