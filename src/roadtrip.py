import sys
import re

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    pattern = re.compile('\s*\S+,([0-9]+);')
    distances = sorted(map(int, pattern.findall(test.strip())))
    result = map(lambda args: str(args[0] - args[1]), zip(distances, [0] + distances[:-1]))
    print(','.join(result))

test_cases.close()