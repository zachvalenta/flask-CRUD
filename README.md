# what is this?

Scaffold for Flask CRUD apps

# how to use?

* __dependencies__: `poetry install`
* __env var__: `ln -sf .env.dev .env`
* __scaffold db__: `make seed`
* __run__: `make flask`
* __everything else__: `make help`

```Makefile
======================================================================

🛠  UTILS

flask:      start built-in Flask dev server
seed:       seed db
home:       open home page
api:        hit API
repl:       open bpython REPL w/ db obj loaded
lite:       connect to SQLite w/ litecli

📊 CODE QUALITY

test:       run unit tests, view basic coverage report in terminal
cov:        view HTML coverage report in browser
lint:       lint using flake8
fmt:        autoformat using black

📦 DEPENDENCIES

env:        show environment info
deps:       list prod dependencies

======================================================================
```
