import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')
visible = '0123456789'
hidden = 'abcdefghij'

for test in test_cases:
    result = ''
    for ch in test.strip():
        if ch in visible:
            result += ch
        elif ch in hidden:
            result += str(hidden.index(ch))
    if result == '':
        print('NONE')
    else:
        print(result)

test_cases.close()