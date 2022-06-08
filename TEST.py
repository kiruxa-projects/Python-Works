import struct

SIGNATURE = bytes([0x4c, 0x5a, 0x54, 0xcf])
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
    A_pattern = '{0}sihqdB'  # without D = 13 + ..
    B_pattern = 'f{0}s{1}sHIHHHqq'  # array 1
    C_pattern = '4Hf'
    D_pattern = 'fi'  # without F = 4 + ..
    E_pattern = '{0}sBIf'  # array 2
    F_pattern = 'qI4Q'  # array 3 = 11
    G_pattern = 'ih'  # array 3 = 11
    # Re-calculation
    E_pattern = E_pattern.format(calcsize(F_pattern))
    B_pattern = B_pattern.format(calcsize(C_pattern), calcsize(E_pattern))
    A_pattern = A_pattern.format(calcsize(B_pattern))

    # begin A:
    A_pos = [begin + len(SIGNATURE),
             begin + len(SIGNATURE) + calcsize(A_pattern)]
    A = struct.unpack(ORDER + A_pattern, byte_str[A_pos[0]:A_pos[1]])
    A = create_dict('A', A)

    B = list(struct.unpack(ORDER + B_pattern, A["A1"]))
    C = list(struct.unpack(ORDER + C_pattern, B[1]))
    D = C[0:5]
    for i in range(0, 4):
        C_pos = [C[i],
                 C[i] + calcsize(D_pattern)]
        D[i] = create_dict("D", list(struct.unpack(ORDER + D_pattern, byte_str[C_pos[0]:C_pos[1]])))
    del C[0:3]
    C[0] = D
    B[1] = create_dict("C", C)

    E = list(struct.unpack(ORDER + E_pattern, B[2]))

    F = list(struct.unpack(ORDER + F_pattern, E[0]))

    Buff = F[2:]
    del F[3:]
    F[2] = Buff

    E[0] = create_dict("F", F)

    E[2] = create_dict("G", list(struct.unpack(ORDER + G_pattern, byte_str[E[2]:E[2] + calcsize(G_pattern)])))

    B[2] = create_dict("E", E)

    buff = list(struct.unpack(ORDER + str(B[3]) + "b", byte_str[B[4]:B[4] + calcsize(str(B[3]) + "b")]))
    B[3] = buff
    del B[4]
    buff = list(struct.unpack(ORDER + str(B[5]) + "b", byte_str[B[6]:B[6] + calcsize(str(B[5]) + "b")]))
    B[5] = buff
    del B[6]
    A["A1"] = create_dict("B", B)

    return A


def main(x):
    return f(x)


print(main(b'LZT\xcf\xee\x8a%\xbf|\x00\x84\x00\x8c\x00\x94\x00\x0b\xf4\x9b>1\xd6\x14\xa8'
           b'\x86\xe8>\xb3\xb4@\x0b\xe3/\xf2v\x93\x0c\x00\x0b@b&9\x80a\x85\xc4\xb2'
           b'\x06B\xabDL\x0cPd7\x94\x00-z(\xaf\xef\x80\x9c\x00\x00\x00a\x9a\xe0'
           b'\xbd\x05\x00\xa2\x00\x00\x00\xd0]\x02\x00\xa7\x00\xce\x99\xfa\xb4\x99$ '
           b'\x817(\x9f\xfcH\x05\x1f\xfc\x9f\xe1\xa1\xc4\x82\x1e\xafP\xf9\xee\r'
           b'\x14\x8d\xfd8\xcc\x8c(\xeft\xd6?e\xc68\xe5\xbeP\x86\xb4T\xff\x0e\x95='
           b'^\xd3\xeb\xd6U\x97f?E\xcdP\xd2<\x89%\xbe\xd4\x8a\xbd\xf2\xba\xd7Q\xff'
           b'\xad\x8a\xa0N\xba\xea\xa2\xd4d'))
