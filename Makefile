run: db
	python school21_case/manage.py runserver

launch: install db migrate
	python school21_case/manage.py runserver

backup:
	mkdir -p backup
	python school21_case/manage.py archive


install:
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

db:
	docker compose -f docker-compose.dev.yaml up -d --build

db_down:
	docker compose -f docker-compose.dev.yaml down

migrate:
	python school21_case/manage.py makemigrations
	python school21_case/manage.py migrate

