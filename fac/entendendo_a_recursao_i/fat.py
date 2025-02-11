def fat(n):
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos")
    if n == 0 or n == 1:
        return 1
    def fat_recursor(n):
        if n == 1:
            return 1
        return n * fat_recursor(n - 1)

    return fat_recursor(n)

print(fat(5))
