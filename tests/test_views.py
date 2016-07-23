import pytest

from tiny_url.views import view_url_alias, view_url_by_alias


def test_view_url_alias(db, monkeypatch):
    from bottle import request

    server_host = 'localhost:12345'

    monkeypatch.setitem(request.environ, 'HTTP_HOST', server_host)
    monkeypatch.setitem(request.environ, 'QUERY_STRING', 'url=example.com')

    assert view_url_alias() == 'http://%s/0' % server_host


def test_view_url_by_alias(db):
    url = 'example.com'
    alias = '42'

    with pytest.raises(Exception) as resp:
        view_url_by_alias(url)
        assert resp.status_code == 404

    db[url] = alias

    with pytest.raises(Exception) as resp:
        view_url_by_alias(url)
        assert resp.status_code == 302
        assert resp.url == url
