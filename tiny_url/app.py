from bottle import Bottle, HTTPResponse, run

import settings  # injects root dir
from tiny_url.views import view_url_by_alias, view_url_alias


app = Bottle()

app.route('/<url_alias>', 'GET', view_url_by_alias)
app.route('/alias', 'GET', view_url_alias)


@app.error(404)
def error_404(error):
    return HTTPResponse(error.body, 404)


if __name__ == '__main__':
    run(app, host='localhost', port=8020, reloader=True, debug=True)
