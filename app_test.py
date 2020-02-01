import os

from app import Thing, app, db, search_things

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


def test_get_index():
    res = client.get("/")
    assert res.status_code == 200


def test_get_api():
    db.session.add(Thing(name="thing1", description="thing1 description"))
    db.session.add(Thing(name="thing2", description="thing2 description"))
    db.session.commit()
    res = client.get("/api")
    assert len(res.json["results"]) == 2
    assert res.json["results"][0]["name"] == "thing1"


def test_search():
    db.session.add(Thing(name="thing1", description="thing1 description"))
    db.session.add(Thing(name="thing2", description="thing2 description"))
    db.session.add(Thing(name="thing3", description="thing3 description"))
    db.session.commit()
    res = search_things(name="thing2")
    assert len(res) == 1
