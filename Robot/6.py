def zero(items, left, right):
    if items[0] == 'IDRIS':
        return left
    if items[0] == 'RUBY':
        return right


def four(items, left, middle, right):
    if items[4] == 2007:
        return left
    if items[4] == 2000:
        return middle
    if items[4] == 1988:
        return right


def three(items, left, middle, right):
    if items[3] == 2000:
        return left
    if items[3] == 2014:
        return middle
    if items[3] == 1969:
        return right


def two(items, left, middle, right):
    if items[2] == 'YACC':
        return left
    if items[2] == 'HLSL':
        return middle
    if items[2] == 'LATTE':
        return right


def one(items, left, middle, right):
    if items[1] == 'MTML':
        return left
    if items[1] == 'NCL':
        return middle
    if items[1] == 'GAMS':
        return right


def main(items):
    return three(
        items,
        zero(
            items,
            four(items, 0, two(items, 1, 2, 3), two(items, 4, 5, 6)),
            7
        ),
        two(items, 8, one(items, 9, 10, 11), 12),
        13
    )



print(main(['IDRIS', 'GAMS', 'HLSL', 1969, 1988]))