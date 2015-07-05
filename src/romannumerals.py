import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')
numerals = [['I', 'V'], ['X', 'L'], ['C', 'D'], ['M', '']]

for test in test_cases:
    n = int(test)
    roman = ''
    for i in range(1, 5):
        result = ''
        digit = n % 10
        top = numerals[i - 1][1]
        one = numerals[i - 1][0]
        if digit > 5:
            top = numerals[i][0]
            result = numerals[i - 1][1]
            digit -= 5
        if digit < 4:
            result += one * digit
        elif digit == 4:
            result = one + top
        else:
            result = top
        roman = result + roman
        n //= 10
    print(roman)

test_cases.close()