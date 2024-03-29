export NAMESPACE=auditinater

# default set up to run with docker compose managed services:
export DATABASE_URL?=postgresql://service:service@localhost:5432/service
export REDIS_URL?=redis://localhost/
export DEBUG_ENABLED?=1
export DISABLE_ECS_LOG_FORMAT?=1

.DEFAULT_GOAL := all

.PHONY: all collect run run_beat run_worker migrate remove release reinstall test up ps down

all:
	echo "Please choose a make target to run."

pip-compile:
	python -m pip install pip-tools

requirements.txt: pip-compile
	pip-compile requirements.in

install: pip-compile requirements.txt
	pip install --upgrade pip
	pip install -r requirements.txt

test_install:
	pip install -r requirements-test.txt

clean:
	rm -rf dist/ build/
	find . -iname '*.pyc' -exec rm {} \; -print

collect:
	python manage.py collectstatic --noinput

runserver: collect
	python manage.py runserver

run: runserver

runbeat:
	celery -A webapp beat -l DEBUG

runworker:
	celery -A webapp worker -l DEBUG

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

up:
	docker-compose --project-name ${NAMESPACE} up --remove-orphans

ps:
	docker-compose --project-name ${NAMESPACE} ps

down:
	docker-compose --project-name ${NAMESPACE} logs -t
	docker-compose --project-name ${NAMESPACE} down --remove-orphans

lint:
	flake8 --ignore=E501 auditinater

test: lint
	pytest -s --ds=auditinater.settings --cov=auditinater
