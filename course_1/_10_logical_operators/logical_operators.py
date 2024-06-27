temperature = float(input("What is the temperature outside? "))

temperatureIsLesserThan0 = temperature < 0
temperatureIsGreaterThan30 = temperature > 30

if not(temperatureIsLesserThan0) and not(temperatureIsGreaterThan30):
    print("The temperature is good today.")
    print("Go outside.")
elif temperatureIsLesserThan0 or temperatureIsGreaterThan30:
    print(f"The temperature is {"hot" if temperatureIsGreaterThan30 else "cold"} today.")
    print("Stay inside.")
