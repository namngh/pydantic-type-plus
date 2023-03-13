import math


class UInt8(bytes):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        pass

    @classmethod
    def validate(cls, v):
        if not isinstance(v, int) and not isinstance(v, bytes):
            raise TypeError('must be int or bytes')

        if isinstance(v, bytes):
            if len(v) > 1:
                raise ValueError('convert out-of-bound')

        if isinstance(v, int):
            byte_length = math.ceil(v.bit_length() / 8.0)
            if byte_length > 1:
                raise ValueError('convert out-of-bound')

            v = v.to_bytes(1, 'little')

        return cls(v)

    def __add__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") + other)

    def __sub__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") - other)

    def __mul__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") * other)

    def __pow__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") ** other)

    def __truediv__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") / other)

    def __floordiv__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") // other)

    def __mod__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") % other)

    def __lshift__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") << other)

    def __rshift__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") >> other)

    def __and__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") & other)

    def __or__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") | other)

    def __xor__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return UInt8.validate(int.from_bytes(self, "little") ^ other)

    def __invert__(self):
        return UInt8.validate(~int.from_bytes(self, "little"))

    def __lt__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return int.from_bytes(self, "little") < other

    def __le__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return int.from_bytes(self, "little") <= other

    def __gt__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return int.from_bytes(self, "little") > other

    def __ge__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return int.from_bytes(self, "little") >= other

    def __eq__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return int.from_bytes(self, "little") == other

    def __ne__(self, other):
        if isinstance(other, UInt8) or isinstance(other, bytes):
            other = int.from_bytes(other, "little")

        return int.from_bytes(self, "little") != other

    def __repr__(self):
        return f'UInt8({int.from_bytes(self, "little")})'
