def test_db_acts_like_dict(db):
    key = 'foo'
    for val in ('1', '2', '3'):
        db[key] = val
        assert db[key] == val
