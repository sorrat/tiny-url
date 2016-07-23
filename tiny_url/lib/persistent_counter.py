from tiny_url.lib import increment_sequence


class PersistentSequence:
    def __init__(self, cache, key):
        self.cache = cache
        self.key = key

    @property
    def value(self):
        try:
            return self.cache[self.key]
        except KeyError:
            return None

    def set(self, value):
        self.cache[self.key] = value

    def next(self, maxlen=4, func=increment_sequence):
        new_value = func(self.value, maxlen)
        self.set(new_value)
        return new_value
