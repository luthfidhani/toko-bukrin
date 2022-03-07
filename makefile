ssh:
	docker-compose run --rm -p 8000:8000 up bash

up:
	docker-compose up

migrations:
	docker-compose run --rm up python manage.py makemigrations

migrate:
	docker-compose run --rm up python manage.py migrate

createsuperuser:
	docker-compose run --rm up python manage.py createsuperuser

test:
	docker-compose run --rm up python manage.py test

startapp:
	docker-compose run --rm up python manage.py startapp $(app)
