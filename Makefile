run: db
	.venv/bin/python school21_case/manage.py runserver

launch: install db migrate
	.venv/bin/python school21_case/manage.py runserver

backup:
	mkdir -p backup
	.venv/bin/python school21_case/manage.py archive

install:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

db:
	docker compose -f docker-compose.dev.yaml up -d --build

db_down:
	docker compose -f docker-compose.dev.yaml down

migrate:
	.venv/bin/python school21_case/manage.py makemigrations
	.venv/bin/python school21_case/manage.py migrate

