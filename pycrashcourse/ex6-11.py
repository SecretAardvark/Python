cities = {
    'portland' : {'state': 'oregon', 'population': 640000,
    'fact':  "Portland was named by the flip of a coin",},

    'NYC' : {'state': 'new york', 'population' : 8700000, 
    'fact': 'New York City has 5 burroughs'},

    'Santa Barbara': {'state': 'california', 'population': 92000, 
    'fact': 'Santa Barbara sucks' },
}

for city, facts in cities.items(): 
    print(city)
    print(facts)