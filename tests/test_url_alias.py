from tiny_url.lib import get_url_alias


def test_get_url_alias(db):
    url = 'http://example.org/some-path'

    alias = '123'
    id_generator = lambda: alias

    assert get_url_alias(url, db, id_generator) == alias
    assert db[url] == alias
    assert db[alias] == url
