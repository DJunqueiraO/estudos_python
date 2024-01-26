import threading
import time
import datetime

def eat_breakfast():
    time.sleep(3)
    print('you eaten breakfast!', end=' ')
    print(datetime.datetime.now().strftime('%H:%M:%S'))


def drink_coffee_and_code():
    time.sleep(4)
    print('you drank coffee and coded!', end=' ')
    print(datetime.datetime.now().strftime('%H:%M:%S'))

def study():
    time.sleep(5)
    print('you studied!', end=' ')
    print(datetime.datetime.now().strftime('%H:%M:%S'))

# eat_breakfast()
# drink_coffee_and_code()
# study()

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee_and_code, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

print(threading.active_count())
print(threading.enumerate())

