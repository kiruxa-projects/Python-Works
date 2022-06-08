map = {"i": 0, 2014: {"i": 3, "PLSQL": {
    "i": 2, 2010: {"i": 1, 1964: 0, 1965: 1}, 2008: 2}, "POD": 3, "POD": 3},
       2005: {"i": 4, "ABNF": 5,
              "UNO": {"i": 3, "PLSQL": {
                  "i": 1, 1964: 6, 1965: 7},
                      "POD": {"i": 2, 2010: 8, 2008: 9}}}, 1967: 11}


def main(arr):
    current = map[arr[0]]
    while (type(current) != int):
        current = current[arr[current["i"]]]
    return current

