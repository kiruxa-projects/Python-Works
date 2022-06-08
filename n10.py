import json
import re


def main(table):
    buffTable = table
    transTable = []

    newTable = []

    for i in range(0, len(buffTable)):
        if (buffTable[i] not in newTable):
            newTable.append(buffTable[i])

    dest = len(newTable)
    dI = 0
    for i in range(0, dest):
        buff = []
        allNone = True
        for j in range(0, len(newTable[i])):
            if (newTable[i][j] is not None):
                allNone = False

                regex = r"[а-яА-Я]*\s[а-яА-Я]*"

                if ("[at]" in newTable[i][j]):
                    buff.append(newTable[i][j].split("[at]")[0])
                elif (re.findall(regex, newTable[i][j])):
                    buff.append(newTable[i][j].split(" ")[1])
                elif (re.findall(r"\d{5,}", newTable[i][j])):
                    b = newTable[i][j]
                    buff.append(b[0] + b[1] + b[2] + "-" + b[3] + b[4] +
                                b[5] + "-" + b[6] + b[7] + b[8] + b[9])
                else:
                    buff.append(newTable[i][j])
        if (not allNone):
            transTable.append([])
            transTable[i - dI] = buff
        else:
            dI += 1

    return transTable


print(json.dumps(main([['fudanz63[at]gmail.com', '7024388020', None, 'Макар Фудянц'],
                       ['nosanko11[at]rambler.ru', '9242619573', None, 'Кирилл Носанко'],
                       ['nukelev30[at]gmail.com', '6521623239', None, 'Эмиль Нукелев'],
                       ['nukelev30[at]gmail.com', '6521623239', None, 'Эмиль Нукелев'],
                       ['nukelev30[at]gmail.com', '6521623239', None, 'Эмиль Нукелев'],
                       ['sezulman72[at]yahoo.com', '5363890143', None, 'Самир Шезулман']]
                      ), ensure_ascii=False))
