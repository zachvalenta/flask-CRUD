#!/usr/bin/env python

from random import randint

from app import Artist, Concert, Performance, Song, db

print("\n 🌱 seeding db... \n")

db.drop_all()
db.create_all()

artists = [Artist(name="Massive Attack"), Artist(name="Nas")]
for a in artists:
    db.session.add(a)
db.session.commit()

massive_attack = Artist.query.get(1)
nas = Artist.query.get(2)

songs = [
    Song(name="One Love", artist=massive_attack),
    Song(name="One Love", artist=nas),
    Song(name="Protection", artist=massive_attack),
    Song(name="Black Bond", artist=nas),
    Song(name="The World is Yours", artist=nas),
    Song(name="Bye Baby", artist=nas),
]
for s in songs:
    db.session.add(s)
db.session.commit()

for _ in range(0, 200):
    performance = Performance(
        rating=randint(5, 10), song_id=randint(1, 6), concert_id=randint(1, 3)
    )
    db.session.add(performance)
db.session.commit()

concerts = [
    Concert(name="Glastonbury"),
    Concert(name="Jazz Fest"),
    Concert(name="Big Day Out"),
]
db.session.bulk_save_objects(concerts)
db.session.commit()

print("\n 🌿 done \n")
