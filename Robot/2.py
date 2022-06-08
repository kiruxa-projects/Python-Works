import math

def main(z):
    if z < -64:
        f = 14*z + 20 * z**6
    elif z >= -64 and z < -42:
        f = z**7 - z**2 - 81*((25-z**3)**4)
    elif z >= -42 and z < 18:
        f = z**3 + 85*((z)**4) + (math.tan(z - 55*(z**2)-z**3))/56
    elif z >= 18 and z < 118:
        f = 77*(z**7) + z**4
    elif z >= 118:
        f = z**3 - z - 1

    return f

print(main(146))