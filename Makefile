SHELL := /bin/bash
include .env

OK      := "\033[32;1m [Ok]\033[0m"

help:
	@printf 'Available commands\n\n'
	@IFS=$$'\n' ; \
		help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//'`); \
		for help_line in $${help_lines[@]}; do \
			IFS=$$'#' ; \
			help_split=($$help_line) ; \
			help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
			help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
			printf "%-30s %s\n" $$help_command $$help_info ; \
		done

start: ##Start local container
	docker-compose up -d

down: ##Down local container
	docker-compose down

restart: ##Restart local container
	docker-compose down
	docker-compose up -d

rebuild: ##Rebuild local container
	docker-compose build

schema: ##Create custom schemas on db
	docker exec -it accounting_db_container psql -U ${DB_USER} -d ${DB_NAME} -c 'CREATE SCHEMA IF NOT EXISTS ${USER_APP_DB_SCHEMA} AUTHORIZATION ${DB_USER}'
	docker exec -it accounting_db_container psql -U ${DB_USER} -d ${DB_NAME} -c 'CREATE SCHEMA IF NOT EXISTS ${TRANSACTIONS_APP_DB_SCHEMA} AUTHORIZATION ${DB_USER}'

restart-force: ##Force rebuild and restart local container without cache, remove docker volume, remove migrations folder
	make down
	##rm -rf src/user_app/migrations
	docker volume rm accounting_postgres-dev-db-data --force
	docker-compose build --no-cache
	make start
	sleep 5
	make schema

restart-force-init: ##Same "make restart-force" and flask db init, migrate, upgrade
	make restart-force
	##make u_flask_db_init
	make u_flask_db_migrate
	make u_flask_db_upgrade


t_migrate: ##docker-compose run --rm transactions_app_service sh -c "python manage.py migrate"
	docker-compose run --rm transactions_app_service sh -c "python manage.py migrate"

t_makemigrations: ##docker-compose run --rm transactions_app_service sh -c "python manage.py makemigrations"
	docker-compose run --rm transactions_app_service sh -c "python manage.py makemigrations"

t_test: ##docker-compose run --rm transactions_app_service sh -c "python manage.py test"
	docker-compose run --rm transactions_app_service sh -c "python manage.py test"

t_exec: ##docker exec -it transactions_app_service sh
	docker exec -it transactions_app_service sh

u_exec: ##docker exec -it user_app_container sh
	docker exec -it user_app_container sh

u_flask_db_init: ##docker-compose run --rm user_app_service sh -c "flask db init"
	docker-compose run --rm user_app_service sh -c "flask db init"

u_flask_db_migrate: ##docker-compose run --rm user_app_service sh -c "flask db migrate"
	docker-compose run --rm user_app_service sh -c "flask db migrate"

u_flask_db_upgrade: ##docker-compose run --rm user_app_service sh -c "flask db upgrade"
	docker-compose run --rm user_app_service sh -c "flask db upgrade"

u_pip_freeze: ##docker-compose run --rm user_app_service sh -c "python -m pip freeze"
	docker-compose run --rm user_app_service sh -c "python -m pip freeze"

u_pip_install ARGUMENT: ##docker-compose run --rm user_app_service sh -c "python -m pip install {ARGUMENT}"
	docker-compose run --rm user_app_service sh -c "pip install flask-migrate && python -m pip freeze"

my_test:
	ifeq (toto, $(filter toto,$(MAKECMDGOALS)))
		@echo 'toto is defined'
	else
		@echo 'no toto around'
	endif
		@echo run command $(if $(filter toto,$(MAKECMDGOALS)),--verbose,--normally)

