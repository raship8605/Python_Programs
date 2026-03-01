'''
Exchange values of two variables.

Example:
a = 5, b = 10 → after swap → a = 10, b = 5

'''
#using third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = a
a = b
b = temp
print("After swap:")
print("a =", a)
print("b =", b)

#without third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After swap:")
print("a =", a)
print("b =", b)

#pythonic way (EAsy)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swap:")
print("a =", a)
print("b =", b)