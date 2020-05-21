def returnCities(*cities):  # * indicates an unknown amount of parameters given as tuples
    for city in cities:
        # for charCity in city:
        yield from city


citiesGen = returnCities('Madrid', 'Barcelona', 'Bilbao', 'Valencia')

print(next(citiesGen))
print(next(citiesGen))
