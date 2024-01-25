from typing import Callable

friends = [("Rachel", 19), 
           ("Monica", 18), 
           ("Phoebe", 17), 
           ("Joey", 16), 
           ("Chandler", 21), 
           ("Ross", 20)]

age = lambda friend: friend[1] >= 18

drinking_buddies = list(filter(age, friends))

print(', '.join(map(lambda buddy: str(buddy), drinking_buddies)))

