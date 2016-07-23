deps:
	pip3 install -r requirements.txt

test:
	py.test -s --pdb tests

dev:
	cd tiny_url; python3 app.py

prod:
	uwsgi config.ini
