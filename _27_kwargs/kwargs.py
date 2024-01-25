
def hello(**names):
    print("hello ", end='')
    for item in names.items():
        print(item[1], end=' ')

hello(title='Mr', first='Josicleison', middle='Elves', last='Jackson')