# what is this?

Scaffold for Flask CRUD apps

# how to use?

* __dependencies__: `poetry install`
* __env var__: `ln -sf .env.dev .env`
* __Git hooks__: `make hooks`
* __scaffold db__: `make seed`
* __run__: `make flask`
* __everything else__: `make help`

```Makefile
======================================================================

🛠  UTILS

flask:      start built-in Flask dev server
home:       open home page
api:        hit API

📊 DATA

seed:       seed db
repl:       open bpython REPL w/ db obj loaded
lite:       connect to SQLite w/ litecli
vd:         connect to SQLite w/ visidata

🤖 CODE QUALITY

test:       run unit tests, view basic coverage report in terminal
cov:        view HTML coverage report in browser
lint:       lint using flake8
fmt:        autoformat using black
hooks:      set Git hooks w/ pre-commit

📦 DEPENDENCIES

env:        show environment info
deps:       list prod dependencies

======================================================================
```
