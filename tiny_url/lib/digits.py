import string


class Digits:
    DIGITS = string.digits + string.ascii_lowercase
    DIGIT_INDEXES = {digit: index for index, digit in enumerate(DIGITS)}
    FIRST = DIGITS[0]

    @classmethod
    def sum(cls, digit, by):
        buf, i = divmod(cls.DIGIT_INDEXES[digit] + by, len(cls.DIGITS))
        return buf, cls.DIGITS[i]

    @classmethod
    def get(cls, i):
        return cls.DIGITS[i]
