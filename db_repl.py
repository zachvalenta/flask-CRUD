#!/usr/bin/env python

from random import randint

from app import Artist, Performance, PerformanceSchema

print("\n🔍 sample queries \n")
artist = Artist.query.get(randint(1, 2))
print(f"songs for artist {artist.artist_id} ({artist.name}): artist.songs \n")
print(f"{artist.songs}\n")

print("🔍 sample serializer \n")
performances = Performance.query.all()
performance_schema = PerformanceSchema(many=True)
perfs = performance_schema.dump(performances)
perf = perfs[randint(1, 30)]
print(f"song performed: perf['song']['name']\n")
print(f"{perf['song']['name']} \n")
print(f"concert of performance: perf['concert']['name']\n")
print(f"{perf['concert']['name']} \n")
