import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask, render_template
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
    # TODO: redirect / to /page/1
    results = Thing.query.paginate(page=1)
    return render_template("index.html", results=results)


@app.route("/page/<int:page_num>")
def get_page(page_num):
    results = Thing.query.paginate(page=page_num)
    return render_template("index.html", results=results)


@app.route("/api")
def api():
    results = get_things()
    return {"results": results}


def get_things():
    things = Thing.query.all()
    thing_schema = ThingSchema(many=True)
    return thing_schema.dump(things)
