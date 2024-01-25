from duck import *

class Person():
    def catch(self, duck: Duck):
        duck.walk()
        duck.talk()
        print("You are catched")