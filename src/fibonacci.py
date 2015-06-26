import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

fibonacci = [0, 1]


def elongate_fibonacci(new_size):
    global fibonacci
    while len(fibonacci) < new_size:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])


def f(n):
    global fibonacci
    while n >= len(fibonacci):
        elongate_fibonacci(n + 2)
    return fibonacci[n]


for test in test_cases:
    print(f(int(test)))

test_cases.close()