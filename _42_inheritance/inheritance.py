from animals.all import *

rabbit: Animal = Rabbit()
hawk: Animal = Hawk()
fish: Animal = Fish()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
hawk.fly()
fish.swim()