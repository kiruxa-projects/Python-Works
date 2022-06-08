def main(digit):
    A = digit & 0b111
    digit = digit >> 3
    B = digit & 0b1111111
    digit = digit >> 7
    C = digit & 0b11111111111111
    digit = digit >> 14
    D = digit & 0b111
    digit = digit >> 3
    E = digit & 0b1
    digit = digit >> 1
    F = digit & 0b111
    digit = digit >> 3
    G = digit & 0b1

    d = (((A << 29) |
          (B << 22) | (D << 19) | (G << 18) |
          (F << 15) | (C << 1) | (E << 0)))
    return d
