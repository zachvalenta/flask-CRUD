import os
from random import randint

from app import Artist, Concert, Performance, Song, app, db, search

"""
CONF
"""


client = app.test_client()
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "test.db")


"""
XUNIT FIXTURES
"""


def setup_module():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path


def teardown_module():
    os.remove(db_path)


def setup_function():
    db.create_all()


def teardown_function():
    db.drop_all()


"""
TESTS
"""


def test_search():
    db.session.add(Song(name="Slippery When Wet"))
    db.session.add(Artist(name="Commodores"))
    db.session.add(Concert(name="Glastonbury"))
    db.session.add(Performance(rating=randint(5, 10), song_id=1, concert_id=1))
    db.session.commit()
    res = search(query="Slippery When Wet", page=1, concert=1)
    assert res.items[0].song.name == "Slippery When Wet"


def test_get_perf_by_id():
    db.session.add(Song(name="Slippery When Wet"))
    db.session.add(Artist(name="Commodores"))
    db.session.add(Concert(name="Glastonbury"))
    db.session.add(Performance(rating=randint(5, 10), song_id=1, concert_id=1))
    res = client.get("/api/performances/1")
    assert res.json["perf_id"] == 1
