from typing import Callable

cities_in_F = {'New York': 32, 
               'Boston': 75, 
               'Los Angeles': 100, 
               'Chicago': 50}

cities_in_C = {key: (value - 32) * (5/9) for (key, value) in cities_in_F.items()}

format_dictionary_numers: Callable[[dict], dict] = \
    lambda dictionary: {key: round(value, 2) for (key, value) in dictionary.items()}

print(f'Cities in F: {format_dictionary_numers(cities_in_F)}')
print(f'Cities in C: {format_dictionary_numers(cities_in_C)}')