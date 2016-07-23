import os

from lsm import LSM

from tiny_url import settings
from tiny_url.lib import memoize


@memoize
class Db:
    def __init__(self):
        self.path = settings.DB_PATH
        self.db = LSM(self.path)

    def __getitem__(self, key):
        return self.db[key]

    def __setitem__(self, key, item):
        self.db[key] = item

    def __contains__(self, key):
        return key in self.db

    def reset(self):
        self.db.close()
        os.remove(self.path)
        self.db = LSM(self.path)
