__author__ = 'Kirros'

for i in range(1, 13):
    print(" ".join(map(lambda x: str(x).rjust(3), list(range(i, 12*i + 1, i)))).strip())