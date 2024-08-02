from person import Person

person = Person(
  input("Enter your name: "), 
  int(input("Enter your age: ")), 
  input("Are you gay? (y/n): ").lower() == "y",
  input("Are you male? (y/n): ").lower() == "y"
)
print("Hello, " + person.name)
print(person.description)