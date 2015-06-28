import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    (a, b) = map(lambda x: x.split(","), test.strip().split(";"))
    result = []
    for num in a:
        if num in b:
            result.append(num)
    print(",".join(result))

test_cases.close()