'''
OOP is a programming paradigm that organizes code using objects instead of just functions or procedures.
 It helps make code modular, reusable, and easier to maintain.

 ****Key Concepts of OOP****

Class – A blueprint for creating objects.
Example: class Car: defines how a Car should behave.

Object – An instance of a class.
Example: my_car = Car() creates an object my_car of type Car.

Attributes (Properties) – Data associated with a class or object.
Example: color, brand, speed of a Car.

Methods (Functions inside a class) – Actions the object can perform.
Example: start(), stop() methods in a Car class.

Encapsulation – Hiding internal details and controlling access using private variables.
Example: __balance in a BankAccount class is private.

Inheritance – A class can reuse properties and methods of another class.
Example: Student class inherits from Person class.

Polymorphism – Many forms: same method or operator behaves differently.
Example: + adds numbers or concatenates strings, method overriding in subclasses.

Abstraction – Hiding complex details and showing only what’s necessary.
Example: Abstract Shape class defines area() without implementation; subclasses provide details.


'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object
s1 = Student("Rashi", 20)
s1.display()