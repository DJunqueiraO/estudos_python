class Person:
  def __init__(
    self, 
    name: str, 
    age: int, 
    isGay: bool, 
    isMale: bool
  ):
    self.name = name
    self.age = age
    self.isGay = isGay
    self.isMale = isMale
    self.description = (
      f"There once was a {"man" if self.isMale else "woman"} named {self.name}, \n" +
      f"{"He" if self.isMale else "She"} was {self.age} years old. \n" +
      f"{"He" if self.isMale else "She"} is {"gay" if self.isGay else "straight"}, "
    )

josicleison = Person("Josicleison", 21, True, True)
josicleide = Person("Josicleide", 23, False, False)

print(josicleison.description)
print(josicleide.description)
