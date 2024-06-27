def hello(first_name, last_name, age = 0):
    print('hello!', first_name, last_name)
    if age > 0:
        print(f'you are {age} years old.') 
    print('heve a nice day!')

MY_FIRST_NAME = "Josicleison"
MY_LAST_NAME = "Elves"

hello(MY_FIRST_NAME, MY_LAST_NAME, 21)
hello(MY_LAST_NAME, MY_FIRST_NAME)