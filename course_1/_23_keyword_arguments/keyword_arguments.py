def hello(first, middle, last, age = 0):
    print('Hello', first, middle, last)
    if age > 0:
        print(f'you are {age} years old.') 

hello(middle = 'Elves', first = 'Josicleison', last = 'Jackson')