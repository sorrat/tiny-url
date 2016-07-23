from urllib.parse import urlunsplit

from bottle import request, redirect, abort

from tiny_url.lib import Db, PersistentSequence, get_url_alias


def view_url_alias():
    url = request.query.url
    cache = Db()
    alias_generator = PersistentSequence(cache, 'current-id').next

    url_alias = get_url_alias(url, cache, alias_generator)

    return urlunsplit((
        request.urlparts.scheme,
        request.urlparts.netloc,
        url_alias, '', ''
    ))


def view_url_by_alias(url_alias):
    cache = Db()
    try:
        url = cache[url_alias]
    except KeyError:
        abort(404, "There is not URL with alias %r" % url_alias)
    else:
        redirect(url)
