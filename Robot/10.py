# НЕ ДОДЕЛАНО


# def transpose(table): #done
#     response = []
#     for i in range(len(table[0])):
#         response.append([])
#         for j in range(len(table)):
#             response[i].append(table[j][i])
#     return response


# def split_by_delimiter(table):
#     return [row for row in table if row[2] is not None]


# def delete_duplicate_columns(table): #done
#     for row in table:
#         del row[2]
#     return table


# def transformer(i, value):
#     if i == 0:
#         return 0 if value == "Нет" else "1"
#     if i == 1:
#         digit_str = value.replace('%', '')
#         digit = float(digit_str) / 100
#         return f'{digit:.2f}'
#     if i == 2:
#         name = value.split()
#         return f'{name[1]} {name[0]}'
#     if i == 2:
#         replaced = value \
#             .replace(' ', '') \
#             .replace('-', '') \
#             .replace('+', '')
#         return replaced[1:]
  


# def transform(table):
#     for i in range(len(table)):
#         for j in range(len(table[i])):
#             table[i][j] = transformer(i, table[i][j])
#     return table


# def main(table):
#     return transform(
#         transpose(
#             delete_duplicate_columns(table)
#         )
#     )
