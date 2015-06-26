import math

__author__ = 'Kirros'

MAX = 1000


def is_prime(n):
    if n < 2:
        return False
    for f in range(2, int(math.sqrt(n)) + 1):
        if n % f == 0:
            return False
    return True

currentNumber = 2
primeCount = 0
primeSum = 0

while primeCount < MAX:
    if is_prime(currentNumber):
        primeCount += 1
        primeSum += currentNumber
    currentNumber += 1

print(primeSum)