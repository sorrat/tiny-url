Description
===========
URL shortener.

Installation
------------
You will need ``Python 3.5``.

Clone repository or download tarball and extract it, and cd to the directory.

| ``make deps`` - install dependencies.
| ``make test`` - run tests.
| ``make dev`` - start-up development server.
| ``make prod`` - start-up production server.
|

The server will be available at ``localhost:8020``.


Usage
-----
::

  Request:
    GET localhost:8020/alias?url=https://www.google.ru/search?q=%D0%B4%D0%BB%D1%8F+%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B5%D0%B3%D0%BE+%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F&ie=utf-8&oe=utf-8&client=firefox-b&gfe_rd=cr&ei=WsOMV-bhFs7ANMfskMAN
  Response:
    DATA localhost:8020/1234

::

  Request
    GET localhost:8020/1234
  Response
    LOCATION https://www.google.ru/search?q=%D0%B4%D0%BB%D1%8F+%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B5%D0%B3%D0%BE+%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F&ie=utf-8&oe=utf-8&client=firefox-b&gfe_rd=cr&ei=WsOMV-bhFs7ANMfskMAN
