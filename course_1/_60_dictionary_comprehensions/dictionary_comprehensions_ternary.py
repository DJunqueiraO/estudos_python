
cities_in_F = {'New York': 32, 
               'Boston': 75, 
               'Los Angeles': 100, 
               'Chicago': 50}

desc_cities = {key: ('WARM' if value >= 40 else 'COLD') for (key, value) in cities_in_F.items()}

print(desc_cities)
