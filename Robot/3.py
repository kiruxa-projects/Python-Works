import math


def main(m, x, n, a, b):
    f = 0.0

    for c in range(1, m+1):
        f = f + ((88*x + x**3 + (c**2)/65)**4 - ((math.exp((c**3)/39))**6)/36)

    for c in range(1, b+1):
        for i in range(1, a+1):
            for j in range(1, n+1):
                f = f - (2**((1 - 43*i**2)**3) + (48*c + 92*j**2)**6 + 62)

    return f


print(main(3, 0.91, 2, 2, 7))
