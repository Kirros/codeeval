import math

__author__ = 'Kirros'

MAX = 1000
MAX_SQRT = int(math.sqrt(MAX))


def is_prime(n):
    if n < 2:
        return False
    for f in range(2, MAX_SQRT):
        if n % f == 0:
            return False
    return True


def is_palindrome(n):
    string = str(n)
    return string == string[::-1]


for i in reversed(range(1, MAX)):
    if is_prime(i) and is_palindrome(i):
        print(i)
        break
