import sys

__author__ = 'Kirros'

test_cases = open(sys.argv[1], 'r')

DIMENSION = 256

board = []
for i in range(0, DIMENSION):
    board.append([0] * DIMENSION)


def set_row(i, x):
    board[i] = [x] * DIMENSION


def set_col(j, x):
    for line in board:
        line[j] = x


def query_row(i):
    return sum(board[i])


def query_col(j):
    result = 0
    for line in board:
        result += line[j]
    return result


for test in test_cases:
    if test.startswith("Set"):
        (i, x) = map(int, test[7:].split(" "))
        if test[3:6] == "Col":
            set_col(i, x)
        if test[3:6] == "Row":
            set_row(i, x)
    if test.startswith("Query"):
        i = int(test[9:])
        if test[5:8] == "Col":
            print(query_col(i))
        if test[5:8] == "Row":
            print(query_row(i))

test_cases.close()