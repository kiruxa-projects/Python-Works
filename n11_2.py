import struct

SIGNATURE = bytes([0x77, 0x53, 0x42, 0x5a])
ORDER = '<'

#  uint8 - B
#  uint16 - H
#  uint32 - I
#  int16 - h
#  int32 - i
#  int64 - q
#  float - f

# Вариант 11

def get_array_pattern(size, type_s):
    pattern = ORDER + (type_s) * size
    return pattern


def calcsize(pattern):
    return struct.calcsize(ORDER + pattern)


def create_dict(name: str, structure: tuple) -> dict:
    dictionary = dict()
    for i in range(len(structure)):
        dictionary.update({name + str(i + 1): structure[i]})
    return dictionary


def f(byte_str: bytes) -> dict:
    begin = byte_str.find(SIGNATURE)
    assert begin >= 0

    # Patterns
    A_pattern = '4sBHI%dsH'  # without D = 13 + ..
    B_pattern = 'IIh'  # array 1
    C_pattern = 'II'
    D_pattern = 'I%ds'  # without F = 4 + ..
    E_pattern = 'iHHI'  # array 2
    F_pattern = 'BIHI'  # array 3 = 11
    # Re-calculation
    D_pattern = D_pattern % calcsize(F_pattern)
    A_pattern = A_pattern % calcsize(D_pattern)

    # Getting the objects
    # begin A:
    A_pos = [begin + len(SIGNATURE),
             begin + len(SIGNATURE) + calcsize(A_pattern)]
    A = struct.unpack(ORDER + A_pattern, byte_str[A_pos[0]:A_pos[1]])
    A = create_dict('A', A)
    A['A1'] = A['A1'].decode()  # byte-string fix

    # begin B:
    B_pos = [A['A3'], A['A3'] + calcsize(B_pattern)]
    B = struct.unpack(ORDER + B_pattern, byte_str[B_pos[0]:B_pos[1]])

    # begin C
    C_arr_size = B[0]
    elem_size = calcsize(C_pattern)

    Cs = list()
    for i in range(C_arr_size):
        arr_pos = (B[1] + elem_size * i, B[1] + elem_size * (i + 1))
        C = struct.unpack(ORDER + C_pattern,
                          byte_str[arr_pos[0]:arr_pos[1]])
        Cs.append(create_dict('C', C))
    # end C

    B = create_dict('B', [Cs, B[2]])
    # end B

    # begin D
    D = struct.unpack(ORDER + D_pattern, A['A5'])

    # begin E
    E_pos = [D[0], D[0] + calcsize(E_pattern)]
    E = struct.unpack(ORDER + E_pattern, byte_str[E_pos[0]:E_pos[1]])

    int_arr_size = E[1]
    elem_size = 8

    int_arr_pos = (E[2], E[2] + elem_size * int_arr_size)
    int_arr = struct.unpack(ORDER + 'q' * int_arr_size,
                            byte_str[int_arr_pos[0]:int_arr_pos[1]])
    E = create_dict('E', (E[0], list(int_arr), E[3]))
    # end E

    # begin F
    F = struct.unpack(ORDER + F_pattern, D[1])

    int_arr_size = F[2]
    elem_size = 4

    int_arr_pos = (F[3], F[3] + elem_size * int_arr_size)
    int_arr = struct.unpack(ORDER + 'l' * int_arr_size,
                            byte_str[int_arr_pos[0]:int_arr_pos[1]])

    F = create_dict('F', [F[0], F[1], list(int_arr)])
    # end F

    D = create_dict('D', [E, F])
    # end D

    A['A3'] = B
    A['A5'] = D
    # end A

    return A


def main(x):
    return f(x)
