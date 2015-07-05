import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    text = test.strip()
    length = len(text)
    i = 1
    result = -1
    while i <= length and result == -1:
        if length % i == 0:
            chunk_size = i
            chunk_count = length // i
            if text[:chunk_size] * chunk_count == text:
                result = chunk_size
        i += 1
    print(result)

test_cases.close()