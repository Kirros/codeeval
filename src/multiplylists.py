import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    mixed = test.strip().split(',')
    numbers = []
    words = []
    for mix in mixed:
        try:
            int(mix)
            numbers.append(mix)
        except ValueError:
            words.append(mix)
    result = '|'.join((','.join(words), ','.join(numbers)))
    if result.startswith('|') or result.endswith('|'):
        result = result.replace('|', '')
    print(result)

test_cases.close()