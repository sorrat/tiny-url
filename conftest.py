import os

import pytest


@pytest.fixture
def db(monkeypatch):
    from tiny_url import settings
    from tiny_url.lib import Db

    test_db_path = os.path.join(settings.ROOT_DIR, 'tests/tiny_url.ldb')
    monkeypatch.setattr('tiny_url.settings.DB_PATH', test_db_path)

    db = Db()
    db.reset()
    return db
