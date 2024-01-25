def divisor(x: float):
    def dividend(y: float):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))