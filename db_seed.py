#!/usr/bin/env python

from app import Thing, db

print("\n 🌱 seeding db... \n")

db.drop_all()
db.create_all()

things = [
    Thing(name="thing1", description="thing 1 desc"),
    Thing(name="thing2", description="thing 2 desc"),
]

db.session.bulk_save_objects(things)
db.session.commit()

print("\n 🌿 done \n")
print(f"things {Thing.query.all()} \n")
