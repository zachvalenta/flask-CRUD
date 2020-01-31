#!/usr/bin/env python

from app import Thing

print("\n ⤵️  sample queries \n\n")
print(f" 🔍 get all concerts: `Thing.query.all()` --> {Thing.query.all()} \n")
print(
    f" 🔍 get thing by id: `Thing.query.filter_by(thing_id=1).first()` --> "
    f"{Thing.query.filter_by(thing_id=1).first()} \n"
)
