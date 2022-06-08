import re


def main(example):

    exr = r'\s*declare\s*q\(([^)]*)\)\s*:=\s*\[([^\]]*)\]'

    d = {}
    matches = re.findall(exr, example)

    for match in matches:
        s = []
        for j in match[1].split(','):
            j = j.strip().strip("'")
            s.append(j)
        key = match[0]
        d[key] = s
        
    return d