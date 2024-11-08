run: db
	python3 school21_case/manage.py runserver

launch: db migrate
	python3 school21_case/manage.py runserver

backup:
	mkdir -p backup
	python3 school21_case/manage.py archive

db:
	docker compose -f docker-compose.dev.yaml up -d --build

db_down:
	docker compose -f docker-compose.dev.yaml down

migrate:
	python3 school21_case/manage.py makemigrations
	python3 school21_case/manage.py migrate

