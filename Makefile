run: db
	python school21_case/manage.py runserver

launch: db migrate
	python school21_case/manage.py runserver

db:
	docker compose -f docker-compose.dev.yaml up -d --build

db_down:
	docker compose -f docker-compose.dev.yaml down

migrate:
	python school21_case/manage.py makemigrations
	python school21_case/manage.py migrate

backup:
	mkdir -p backup
	python school21_case/manage.py archive

