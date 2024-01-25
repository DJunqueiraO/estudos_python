weather = {'New York': 'snowing', 'Boston': 'cloudy', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}

print(sunny_weather)