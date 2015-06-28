import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    last_one = ''
    result = []
    for n in test.strip().split(","):
        if last_one == n:
            continue
        result.append(n)
        last_one = n
    print(",".join(result))

test_cases.close()