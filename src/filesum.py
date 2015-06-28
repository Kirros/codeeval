import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')
file_sum = 0

for test in test_cases:
    file_sum += int(test)

print(file_sum)

test_cases.close()