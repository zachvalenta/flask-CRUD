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
get:        hit index endpoint

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
