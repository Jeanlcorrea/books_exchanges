.DEFAULT_GOAL := default_target

PROJECT_NAME := books_exchanges
PYTHON_VERSION := 3.12.3
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)
DATABASE_PASS := postgres

pycodestyle:
	echo "Running pycodestyle"
	pycodestyle

flake8:
	echo "Running flake8"
	flake8

code-convention: pycodestyle flake8

# Postgres Local
run-postgres:
	docker start books_exchanges-postgres 3>/dev/null || docker run --name books_exchanges-postgres -p 5432:5432 -e POSTGRES_PASSWORD='$(DATABASE_PASS)' -d postgres:12-alpine

containers-up: run-postgres

containers-down:
	docker stop $$(docker ps -aq)

containers-reset: containers-down containers-up
