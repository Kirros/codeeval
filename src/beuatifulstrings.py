import string
import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    letters = test.lower()
    counts = []
    result = 0
    for letter in list(string.ascii_lowercase):
        counts.append(letters.count(letter))
    counts.sort()
    for i in range(1, 27):
        result += i * counts[i - 1]
    print(result)

test_cases.close()