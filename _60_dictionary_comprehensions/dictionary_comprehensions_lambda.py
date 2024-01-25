from typing import Callable

cities_in_F = {'New York': 32, 
               'Boston': 75, 
               'Los Angeles': 100, 
               'Chicago': 50}

check_temp: Callable[[int], str] = lambda temp: 'WARM' if temp >= 40 else 'COLD'

desc_cities = {key: check_temp(value) for (key, value) in cities_in_F.items()}

print(desc_cities)
