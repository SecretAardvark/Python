def city_country(city, country):
    location = city + " " + country
    return location

place = {"Santiago" : "Chile", "New York":"New York", "mexico city": "mexico"}

for key, value in place:
    map = city_country(key, value)
    print(map)