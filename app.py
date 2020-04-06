import os
import re
from pathlib import Path

from dotenv import find_dotenv, load_dotenv
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

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
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["UPLOAD_FOLDER"] = f"{basedir}/uploads"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

try:
    Path.cwd().joinpath("uploads").mkdir()
except FileExistsError:
    pass

# db - init
db = SQLAlchemy(app)
ma = Marshmallow(app)

"""
MODELS
"""


class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    songs = db.relationship("Song", backref="artist")

    def __repr__(self):
        return f"id {self.artist_id} name {self.name}"


class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.artist_id"))
    performances = db.relationship("Performance", backref="song")

    def __repr__(self):
        return f"id {self.song_id} name {self.name}"


class Performance(db.Model):
    perf_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey("song.song_id"))
    concert_id = db.Column(db.Integer, db.ForeignKey("concert.concert_id"))

    def __repr__(self):
        return f"id {self.perf_id} rating {self.rating}"


class Concert(db.Model):
    concert_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    performances = db.relationship("Performance", backref="concert")

    def __repr__(self):
        return f"id {self.concert_id} name {self.name}"


"""
SCHEMAS
"""


class ArtistSchema(ma.ModelSchema):
    class Meta:
        model = Artist


class SongSchema(ma.ModelSchema):
    class Meta:
        model = Song

    artist = ma.Nested(ArtistSchema)


class ConcertSchema(ma.ModelSchema):
    class Meta:
        model = Concert


class PerformanceSchema(ma.ModelSchema):
    class Meta:
        model = Performance

    song = ma.Nested(SongSchema)
    concert = ma.Nested(ConcertSchema)


"""
SEARCH
"""


def search(query, page, concert):
    return (
        db.session.query(Performance)
        .join(Song)
        .filter(Song.name == query)
        .join(Concert)
        .filter(Concert.concert_id == concert)
        .paginate(page=page)
    )


@app.route("/search/<int:concert>", methods=["POST"])
def do_search(concert):
    query = request.form["query"]
    results = search(query=query, page=1, concert=concert)
    if results.items:
        pages = [x for x in results.iter_pages()]
        performance_schema = PerformanceSchema(many=True)
        dump = performance_schema.dump(results.items)
        return render_template("perfs.html", results=dump, pages=pages, query=query)
    else:
        return render_template("404-search.html", concert=concert)


"""
TEMPLATES
"""


@app.route("/")
@app.route("/concert")
def get_concerts():
    results = Concert.query.all()
    concert_schema = ConcertSchema(many=True)
    dump = concert_schema.dump(results)
    return render_template("concert.html", results=dump)


@app.route("/concert/<int:concert>")
def get_perf_for_concert_first_page(concert):
    performances = Performance.query.filter_by(concert_id=concert).paginate(page=1)
    pages = [x for x in performances.iter_pages()]
    performance_schema = PerformanceSchema(many=True)
    dump = performance_schema.dump(performances.items)
    return render_template("perfs.html", results=dump, pages=pages)


@app.route("/concert/<int:concert>/<int:page>")
def get_perf_for_concert_page(concert, page):
    performances = Performance.query.filter_by(concert_id=concert).paginate(page=page)
    pages = [x for x in performances.iter_pages()]
    performance_schema = PerformanceSchema(many=True)
    dump = performance_schema.dump(performances.items)
    return render_template("perfs.html", results=dump, pages=pages)


@app.route("/concert/<int:concert>/<int:page>/<string:query>")
def get_perf_for_concert_page_query(concert, page, query):
    performances = search(concert=concert, page=page, query=query)
    pages = [x for x in performances.iter_pages()]
    performance_schema = PerformanceSchema(many=True)
    dump = performance_schema.dump(performances.items)
    return render_template("perfs.html", results=dump, pages=pages, query=query)


"""
API
"""


@app.route("/api/performances/<int:id>")
def get_performance_single(id):
    perf = Performance.query.get(id)
    performance_schema = PerformanceSchema()
    return performance_schema.dump(perf)


"""
FILE UPLOAD
"""


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "GET":
        return render_template("file-upload.html")
    if request.method == "POST":
        file = request.files["upload_file"]
        if file.filename == "":
            flash("no file selected", "error")
            return redirect(url_for("upload_file"))
        elif re.search("^[\w\-\_]*\.txt$", file.filename) is None:
            flash("only .txt files", "error")
            return redirect(url_for("upload_file"))
        else:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            flash("file successfully uploaded ✅")
            return redirect(url_for("upload_file"))


@app.route("/upload/<filename>")
def get_upload(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
