import time

from tiny_url.lib import increment_sequence


def test_increment_sequence():
    fixtures = (
        ('0', '1'),
        ('9', 'a'),
        ('ab', 'ac'),
        ('cz', 'd0'),
        ('7z', '80'),
        ('345sdf3', '345sdf4'),
    )
    for val, expected_next_val in fixtures:
        assert increment_sequence(val) == expected_next_val


def test_counter_is_cyclical():
    fixtures = (
        ('z', '0', 1),
        ('z', '10', 2),
        ('zzzz', '0', 4),
        ('zzzz', '10000', 5),
    )
    for val, next_val, maxlen in fixtures:
        assert increment_sequence(val, maxlen) == next_val


def test_counter_generates_unique_values():
    first = increment_sequence(None)
    current = increment_sequence(first)
    uniques = set([first, current])
    i = len(uniques)
    t = time.time()

    while current != first:
        current = increment_sequence(current, 2)
        uniques.add(current)
        i += 1

        if i % 10000 == 0 and time.time() - t > 5:
            raise Exception("Timeout!")

    assert len(uniques) == i - 1

