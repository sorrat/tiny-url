from tiny_url.lib import Digits, PersistentSequence


def test_persistent_sequence(db):
    x = '4444'
    s = PersistentSequence(db, 'counter-key')

    assert s.value is None
    assert s.next(func=lambda *args: x) == x
    assert s.value == x

