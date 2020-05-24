# what is this?

Scaffold for Flask CRUD apps; similar to [another project](https://github.com/zachvalenta/flask-skeleton) I have but with pagination and search.

# todo

Moving models and schemas to separate modules should be simple as:

```python
db = SQLAlchemy(app)
ma = Marshmallow(app)
from models import Artist
from schemas import ArtistSchema
```

and updating the `flake8` config to ignore `E402` along with the tests and helper scripts to import models/schemas from their own modules instead of `app.py`.

The problem I encountered was that the tests failed *only on the Git hook*.

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
