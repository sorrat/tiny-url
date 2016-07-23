import sys

from .digits import Digits


def increment_sequence(string, maxlen=-1):
    if string is None:
        return Digits.FIRST

    result = []
    buf = 1
    letters = list(string)

    while letters:
        buf, incremented = Digits.sum(letters.pop(), buf)
        result.append(incremented)

        if buf == 0:
            result.extend(reversed(letters))
            break

    if buf > 0:
        result.append(Digits.get(buf))

    result = ''.join(reversed(result))

    if 0 < maxlen < len(result):
        result = Digits.FIRST
    return result
