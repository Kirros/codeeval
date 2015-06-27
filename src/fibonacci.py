import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

fibonacci = [0, 1]


def elongate_fibonacci(max_index):
    global fibonacci
    while len(fibonacci) < max_index + 1:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])


def f(n):
    global fibonacci
    while n > len(fibonacci) - 1:
        elongate_fibonacci(n)
    return fibonacci[n]


for test in test_cases:
    print(f(int(test)))

test_cases.close()