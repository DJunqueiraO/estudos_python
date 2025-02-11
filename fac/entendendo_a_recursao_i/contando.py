def conte(de, ate):
    if de > ate:
        return
    print(de)
    de += 1
    return conte(de, ate)

conte(0, 10)