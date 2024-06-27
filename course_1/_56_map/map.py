from typing import Callable

store: list[tuple[str, float]] = [
    ("ship", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00)
]

to_: Callable[[float], Callable[[tuple[str, float]], tuple[str, float]]] = lambda price: lambda data: (data[0], data[1] * price)
to_euro: Callable[[tuple[str, float]], tuple[str, float]] = to_(0.19)
to_dollar: Callable[[tuple[str, float]], tuple[str, float]] = to_(0.20)
to_dinheiro_de_verdade: Callable[[tuple[str, float]], tuple[str, float]] = to_(0.0000051)

store_euros = list(map(to_euro, store))
store_dollar = list(map(to_dollar, store))
store_bitcoin = list(map(to_dinheiro_de_verdade, store))

print(', '. join(map(lambda a: f"{a}", store_euros)))
print(', '. join(map(lambda a: f"{a}", store_dollar)))
print(', '. join(map(lambda a: f"{a}", store_bitcoin)))
    
