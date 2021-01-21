from cities_library import _city_database

cdb = _city_database()
cdb.load_cities('worldcities.csv')
ret = cdb.city_coords
print(ret[1840001590])
