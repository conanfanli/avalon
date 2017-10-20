.PHONY: restore-db
restore-db:
	psql -U postgres avalon -c 'drop schema public cascade; create schema public'
	python manage.py migrate

.PHONY: test
test:
	pip install -r requirements.txt
	python manage.py test

.PHONY: load-current
load-current:
	python manage.py loaddata current

.PHONY: dropschema
dropschema:
	psql avalon -c 'drop schema public cascade; create schema public'

.PHONY: dump-current
dump-current:
	python manage.py dumpdata --indent=2 core -o avalon/core/fixtures/current.json

.PHONY: dump-live-data
dump-live-data:
	DATABASE_URL=$(shell heroku config:get DATABASE_URL) python manage.py dumpdata --indent=2 core -o avalon/core/fixtures/current.json


.PHONY: start-dev
start-dev:
	honcho start -f Procfile.dev


.PHONY: prod-start
prod-start:
	heroku ps:scale web=1

.PHONY: prod-stop
prod-stop:
	heroku ps:scale web=0
