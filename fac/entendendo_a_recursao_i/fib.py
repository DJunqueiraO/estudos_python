def fib(n):
    def fib_recurs(n_):
        if n_ == 0 or n_ == 1:
            return n_
        return fib_recurs(n_ - 1) + fib_recurs(n_ - 2)
    return fib_recurs(n)

print(fib(0))  # 0
print(fib(1))  # 1
print(fib(5))  # 5
print(fib(10)) # 55
print(fib(12)) # 144
