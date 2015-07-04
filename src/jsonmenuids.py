import sys
import json

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    j = json.loads(test.strip())
    result = 0
    for item in j.get('menu').get('items'):
        if item is None:
            continue
        if 'label' in item.keys():
            result += item.get('id')
    print(result)

test_cases.close()