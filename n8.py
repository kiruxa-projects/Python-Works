import re


def main(str):
    parsed = re.findall(r'(equ\s*\#(\-*\d*)\s*to\s*\'([^\']*))', str)
    result = {}
    for i in parsed:
        result[i[2]] = int(i[1])

    return result
