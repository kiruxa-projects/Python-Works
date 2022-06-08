from enum import Enum
from struct import unpack_from, calcsize
from typing import Any, Callable


class Primitive(Enum):
    uint64 = 'Q'
    int64 = 'q'
    uint32 = 'I'
    int32 = 'i'
    uint16 = 'H'
    int16 = 'h'
    uint8 = 'B'
    int8 = 'b'
    float = 'f'
    double = 'd'
    char = 'c'


class BinaryReader:
    def __init__(self, source: str, offset: int = 0):
        self.offset = offset
        self.source = source

    def read(self, pattern: Primitive):
        data = unpack_from(pattern.value, self.source, self.offset)
        self.offset += calcsize(pattern.value)
        return data[0]


def read_array(
        reader: BinaryReader,
        size: int,
        address: int,
        read: Callable[[BinaryReader], Any],
        structure_size: int = 1,
        to_sum: bool = False
):
    if to_sum:
        reader.offset += size * structure_size
    reader = BinaryReader(source=reader.source, offset=address)
    values = []
    while address + (size * structure_size) > reader.offset:
        values.append(read(reader))
    return values


def read_g(reader: BinaryReader):
    return dict(
        G1=reader.read(Primitive.uint16),
        G2=reader.read(Primitive.uint64),
        G3=reader.read(Primitive.uint8)
    )


def read_f(reader: BinaryReader):
    return dict(
        F1=read_array(
                reader,
                reader.read(Primitive.uint16),
                reader.read(Primitive.uint16),
                lambda reader: reader.read(Primitive.uint8),
                structure_size=1
            ),
        F2=reader.read(Primitive.int8),
        F3=reader.read(Primitive.int64),
        F4=read_array(
            reader,
            8,
            reader.offset,
            lambda reader: reader.read(Primitive.int32),
            structure_size=4,
            to_sum=True
        ),
        F5=reader.read(Primitive.int32)
    )


def read_e(reader: BinaryReader):
    return dict(
        E1=reader.read(Primitive.uint16),
        E2=reader.read(Primitive.uint32)
    )


def read_d(reader: BinaryReader):
    return dict(
        D1=reader.read(Primitive.double),
        D2=[read_e(BinaryReader(reader.source,
                                offset=i))
            for i in
            read_array(
                reader,
                reader.read(Primitive.uint16),
                reader.read(Primitive.uint32),
                lambda reader: reader.read(Primitive.uint16),
                structure_size=2
            )
            ],
        D3=read_f(reader),
        D4=read_array(
                reader,
                reader.read(Primitive.uint16),
                reader.read(Primitive.uint32),
                lambda reader: reader.read(Primitive.int16),
                structure_size=2
            ),
        D5=read_array(
                reader,
                2,
                reader.offset,
                lambda reader: reader.read(Primitive.uint64),
                structure_size=8,
                to_sum=True
            ),
        D6=reader.read(Primitive.float)
    )


def read_c(reader: BinaryReader):
    return dict(
        C1=reader.read(Primitive.uint32),
        C2=read_d(reader),
        C3=reader.read(Primitive.uint32),
        C4=reader.read(Primitive.double),
        C5=reader.read(Primitive.uint64)
    )


def read_b(reader: BinaryReader):
    return dict(
        B1=reader.read(Primitive.int8),
        B2=reader.read(Primitive.float),
        B3=reader.read(Primitive.int8),
    )


def read_a(reader: BinaryReader):
    return dict(
        A1=reader.read(Primitive.uint16),
        A2=reader.read(Primitive.uint32),
        A3=read_b(BinaryReader(reader.source,
                               offset=reader.read(Primitive.uint32))),
        A4=reader.read(Primitive.float),
        A5=reader.read(Primitive.float),
        A6=reader.read(Primitive.int8),
        A7=read_c(BinaryReader(reader.source,
                               offset=reader.read(Primitive.uint16))),
        A8=read_g(BinaryReader(reader.source,
                               offset=reader.read(Primitive.uint16)))
    )


def main(source):
    return read_a(BinaryReader(source, offset=4))
