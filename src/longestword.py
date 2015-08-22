import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    words = test.strip().split(' ')
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)

test_cases.close()