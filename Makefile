COMPOSE_FILE_DEV = docker-compose.dev.yaml
COMPOSE_FILE_PROD = docker-compose.yaml
APP = app
DATABASE_NAME = csirt_postgres_db 


dev: 
	docker compose -f $(COMPOSE_FILE_DEV) up --build
build:
	docker compose build
up:
	docker compose up
restart: build up
shell:
	docker compose exec app python manage.py shell
shellplus:
	docker compose exec app python manage.py shell_plus
down:
	docker compose down
migrate:
	docker compose run app python manage.py migrate
migrations:
	docker compose run app python manage.py makemigrations
migrationsmerge:
	docker compose run app python manage.py makemigrations --merge
test:
	docker compose run app python manage.py test $(APP)
db:
	docker compose exec db psql --username=$(USERNAME) --dbname=$(DBNAME)
superuser:
	docker compose run app python manage.py createsuperuser
startapp:
	docker compose exec app python manage.py startapp $(APP)
flush:
	docker compose exec app python manage.py flush --no-input
lint-apply:
	@echo "applying lint changes ..."
	docker-compose exec app flake8 --ignore=D401,W503 --exclude migrations .