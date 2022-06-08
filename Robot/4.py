import math


def main(n):
    f = 0.0

    if n == 0:
        f = f + 0.37
    elif n == 1:
        f = f + 0.06
    elif n >= 2:
        f = f + math.exp((main(n-2))**2 + 70*((main(n-1)**3)))
        f = f / 10

    return f


print(main(7))
