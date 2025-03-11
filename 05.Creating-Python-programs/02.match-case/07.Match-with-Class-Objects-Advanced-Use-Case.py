class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print("Before Match Statement: p =", p.name, p.age)

match p:
    case Person(name="Alice", age=25):
        print("Alice is 25 years old.")  # This block executes
    case Person(name="Bob", age=30):
        print("Bob is 30 years old.")
    case _:
        print("Unknown person.")

print("After Match Statement: p =", p.name, p.age)

