import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


for test in test_cases:
    digits = map(lambda x: str(words.index(x)), test.strip().split(";"))
    print("".join(digits))

test_cases.close()