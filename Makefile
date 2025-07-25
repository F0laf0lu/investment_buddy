# Makefile for investment buddy backend
PYTHON=python
PIP=pip

setup:
	$(PIP) install -r requirements.txt

migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

runserver:
	$(PYTHON) manage.py runserver

resetdb:
	mysql -u root -p < db_init.sql