.PHONY: test

help:
	@echo
	@echo "======================================================================"
	@echo
	@echo "🛠  UTILS"
	@echo
	@echo "flask:      start built-in Flask dev server"
	@echo "seed:       seed db"
	@echo "home:       open home page"
	@echo "api:        hit API"
	@echo "repl:       open bpython REPL w/ db obj loaded"
	@echo "lite:       connect to SQLite w/ litecli"
	@echo
	@echo "📊 CODE QUALITY"
	@echo
	@echo "test:       run unit tests, view basic coverage report in terminal"
	@echo "cov:        view HTML coverage report in browser"
	@echo "lint:       lint using flake8"
	@echo "fmt:        autoformat using black"
	@echo
	@echo "📦 DEPENDENCIES"
	@echo
	@echo "env:        show environment info"
	@echo "deps:       list prod dependencies"
	@echo
	@echo "======================================================================"
	@echo

#
# 🛠 UTILS
#

flask:
	poetry run flask run

seed:
	rm local.db; poetry run python db_seed.py

api:
	poetry run http http://localhost:5000/api

home:
	open http://localhost:5000

repl:
	poetry run bpython -i db_repl.py

lite:
	poetry run litecli local.db

#
# 📊 CODE QUALITY
#

test:
	poetry run coverage run --source='app' -m pytest -v && poetry run coverage report -m

cov:
	poetry run coverage html; open htmlcov/index.html

lint:
	poetry run flake8 *.py

fmt:
	poetry run isort *.py; poetry run black *.py

#
# 📦 DEPENDENCIES
#

env:
	poetry env info

deps:
	poetry show --tree --no-dev
