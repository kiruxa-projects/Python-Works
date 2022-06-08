import struct



SIGNATURE = bytes([0x4f, 0x4d, 0x42, 0xf4])
ORDER = '<'

#  uint8 - B
#  uint16 - H
#  uint32 - I
#  int16 - h
#  int32 - i
#  int64 - q
#  float - f

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
    A_pattern = 'hb{0}sB{1}s'  # without D = 13 + ..
    B_pattern = 'fq3s'  # array 1
    C_pattern = '{0}sQf4hdB2h'
    D_pattern = 'dBqBH7Ii'  # without F = 4 + ..
    # Re-calculation
    C_pattern = C_pattern.format(calcsize(D_pattern))
    A_pattern = A_pattern.format(calcsize(B_pattern) * 4, calcsize(C_pattern))

    # Getting the objects
    # begin A:
    A_pos = [begin + len(SIGNATURE),
             begin + len(SIGNATURE) + calcsize(A_pattern)]
    A = struct.unpack(ORDER + A_pattern, byte_str[A_pos[0]:A_pos[1]])
    A = create_dict('A', A)
    # A['A1'] = A['A1'].decode()  # byte-string fix

    # begin B:
    # B_pos = [A['A3'], A['A3']+calcsize(B_pattern)]
    B_arr = []
    for i in range(0, 4):
        B = struct.unpack(ORDER + B_pattern,
                          A['A3'][calcsize(B_pattern) *
                                  i:calcsize(B_pattern) * (i + 1)])
        B = [B[0], B[1], B[2].decode("utf-8")]
        B_arr.append(B)

    A['A3'] = [create_dict("B", B_arr[0]),
               create_dict("B", B_arr[1]),
               create_dict("B", B_arr[2]),
               create_dict("B", B_arr[3])]

    C1 = A['A5']
    C1 = C1[0:calcsize(D_pattern)]
    C1 = struct.unpack(ORDER + D_pattern, C1)

    D6 = []
    for i in C1[5:12]:
        D6.append(i)

    C1 = {'D1': C1[0],
          'D2': C1[1],
          'D3': C1[2],
          'D4': C1[3],
          'D5': C1[4],
          'D6': D6,
          'D7': C1[12], }

    A5 = struct.unpack(ORDER + C_pattern, A['A5'])

    A66 = []
    for i in A5[9:11]:
        A66.append(i)

    C44 = []
    for i in A5[3:7]:
        C44.append(i)

    A['A5'] = create_dict('C', [A5[0],
                                A5[1],
                                A5[2],
                                C44,
                                A5[7],
                                A5[8],
                                A66])
    A['A5']['C1'] = C1

    return A


def main(x):
    return f(x)
