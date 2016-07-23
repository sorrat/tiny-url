from tiny_url.lib import Digits


def test_digits():
    assert Digits.FIRST == '0'
    assert Digits.get(0) == Digits.FIRST
    assert Digits.get(35) == 'z'

    assert Digits.sum('3', 1) == (0, '4')
    assert Digits.sum('9', 1) == (0, 'a')
    assert Digits.sum('a', 2) == (0, 'c')
    assert Digits.sum('z', 1) == (1, '0')
    assert Digits.sum('0', 36) == (1, '0')
