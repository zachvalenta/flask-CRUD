import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask, render_template, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

"""
CONF
"""

# db - load env, construct path
load_dotenv(find_dotenv())
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, os.getenv("DATABASE"))
db_uri = "sqlite:///" + db_path

# app - init, config
app = Flask(__name__, template_folder=basedir)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

# db - init
db = SQLAlchemy(app)
ma = Marshmallow(app)

"""
MODEL & SCHEMA
"""


class Thing(db.Model):
    thing_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.Text)

    def __repr__(self):
        return f"id {self.thing_id} name {self.name} desc {self.description}"


class ThingSchema(ma.ModelSchema):
    class Meta:
        model = Thing


"""
ROUTES
"""


@app.route("/")
def index():
    results = Thing.query.paginate(page=1)
    pages = [x for x in results.iter_pages()]
    return render_template("index.html", results=results, pages=pages)


@app.route("/page/<int:page>")
def get_page(page):
    results = Thing.query.paginate(page=page)
    pages = [x for x in results.iter_pages()]
    return render_template("index.html", results=results, pages=pages)


@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    results = Thing.query.filter_by(name=query).paginate(page=1)
    pages = [x for x in results.iter_pages()]
    return render_template("index.html", results=results, pages=pages, query=query)


@app.route("/page/<int:page>/<string:query>")
def get_search_page(page, query):
    results = Thing.query.filter_by(name=query).paginate(page=page)
    pages = [x for x in results.iter_pages()]
    return render_template("index.html", results=results, pages=pages, query=query)


"""
API
"""


@app.route("/api/all")
def api_all():
    things = Thing.query.all()
    thing_schema = ThingSchema(many=True)
    serialized = thing_schema.dump(things)
    return {"results": serialized}


@app.route("/api/search")
def api_search():
    query = request.args.get("name")
    things = Thing.query.filter_by(name=query).all()
    thing_schema = ThingSchema(many=True)
    serialized = thing_schema.dump(things)
    return {"results": serialized}
