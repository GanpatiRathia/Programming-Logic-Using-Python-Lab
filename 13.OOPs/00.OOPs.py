# Object-Oriented Programming (OOP) in Python
"""
What is OOP?
Object-Oriented Programming is a programming paradigm that organizes code using objects and classes. 
It helps to structure programs so that properties and behaviors are bundled into individual objects.
"""
# Basic Concepts of OOP in Python:
"""
1. Class
A class is a blueprint for creating objects.

It defines the structure (variables) and behavior (methods) of an object.
"""
class Student:
    def __init__(self, name):
        self.name = name
"""
2. Object
An object is an instance of a class. It holds actual data.
"""
s1 = Student("Amit")
print(s1.name)  # Output: Amit
"""
3. Constructor (__init__ method)
Special method used to initialize objects.

Automatically called when an object is created.
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
"""
4. self keyword
Refers to the current object.

Used inside class methods to access instance variables.
"""
# Key OOP Features:
"""
1. Encapsulation
Hiding internal details of the object and only exposing necessary parts.

Done by using private/protected variables and public methods.
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def show_balance(self):
        return self.__balance
"""
2. Abstraction
Hiding complex implementation and showing only the necessary features.
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")
"""
3. Inheritance
Allows one class to inherit properties and methods from another.

Promotes code reuse.
"""
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()  # Output: Bark

"""
4. Polymorphism
One method behaves differently depending on the object calling it.

Same function name but different behavior.
"""

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

def animal_sound(animal):
    animal.sound()

animal_sound(Cat())  # Meow
animal_sound(Cow())  # Moo
"""
Why use OOP in Python?

Helps in organizing large programs.

Increases code reusability.

Makes maintenance easier.

Improves data security using encapsulation.
"""

"""
Summary Table:
Feature	           Description
Class	        Blueprint for creating objects
Object	        Instance of a class
Encapsulation	Hides data and methods
Abstraction	Shows only essential features
Inheritance	Reuses code from a parent class
Polymorphism	Many forms: same method, different output
"""
