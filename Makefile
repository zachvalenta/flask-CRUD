.PHONY: test

help:
	@echo
	@echo "======================================================================"
	@echo
	@echo "🛠  UTILS"
	@echo
	@echo "flask:      start built-in Flask dev server"
	@echo "home:       open home page"
	@echo "up:         open upload page"
	@echo "api:        get performance by id"
	@echo "todo:       view all todos"
	@echo
	@echo "📊 DATA"
	@echo
	@echo "seed:       seed db"
	@echo "repl:       open bpython REPL w/ db obj loaded"
	@echo "lite:       connect to SQLite w/ litecli"
	@echo "vd:         connect to SQLite w/ visidata"
	@echo
	@echo "🤖 CODE QUALITY"
	@echo
	@echo "test:       run unit tests, view basic coverage report in terminal"
	@echo "cov:        view HTML coverage report in browser"
	@echo "lint:       lint using flake8"
	@echo "fmt:        autoformat using black"
	@echo "hooks:      set Git hooks w/ pre-commit"
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

home:
	open http://localhost:5000

up:
	open http://localhost:5000/upload

api:
	poetry run http http://localhost:5000/api/performances/7

todo:
	rg -i -B 3 -A 3 todo *.py

#
# 📊 DATA
#

seed:
	rm local.db; poetry run python db_seed.py

repl:
	poetry run bpython -i db_repl.py

lite:
	poetry run litecli local.db

vd:
	poetry run vd local.db

#
# 🤖 CODE QUALITY
#

test:
	poetry run coverage run --source='app' -m pytest -v && poetry run coverage report -m

cov:
	poetry run coverage html; open htmlcov/index.html

lint:
	poetry run flake8 *.py

fmt:
	poetry run isort *.py; poetry run black *.py

hooks:
	poetry run pre-commit install -t pre-commit; poetry run pre-commit install -t pre-push

#
# 📦 DEPENDENCIES
#

env:
	poetry env info

deps:
	poetry show --tree --no-dev
