from math import exp


def main(y):
    n = len(y)
    total = 0
    y.insert(0, 0)
    for i in range(1, n + 1):
        temp = ((y[n+1-i])**3) / 39
        total += ((exp(temp))**6) / 36

    return 71*total



print(main([0.97, -0.51, 0.1, -0.48, -0.69, 0.26, -0.1]))
