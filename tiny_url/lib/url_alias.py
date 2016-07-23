def get_url_alias(url, cache, alias_generator):
    if url in cache:
        return cache[url]

    url_alias = alias_generator()
    cache[url] = url_alias
    cache[url_alias] = url

    return url_alias
