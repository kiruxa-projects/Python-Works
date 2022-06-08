def main(y):
    f = (y**3)/((y**3)/92 + 2*y)
    f = f + 88 * ((y**2 - 1)**4)
    f = f - 40*(17*(y**3)-y - 1)
    return f


print(main(0.19))
