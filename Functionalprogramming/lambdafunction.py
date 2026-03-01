
'''
A lambda function is a small anonymous function written in one line.

 It has no name
 Used for short, simple operations
 Often used with map(), filter(), reduce(), sorted()

 syntax:  ambda arguments : expression
 Exaample: square = lambda x: x*x
           print(square(5))
'''

#addition
add=lambda n1,n2:(n1+n2)
print(add(10,20))

#square
square=lambda num:num**2
print(square(5))

#cube
cube=lambda num:num**3
print(cube(2))

#even or odd
even_odd=lambda num: "even" if num%2==0 else "odd"
print(even_odd(7))

#maximum of two numbers
num = lambda num1, num2: "num1 is larger" if num1 > num2 else "num2 is larger"
print(num(5, 8))

#minimum of three numbers
minimum = lambda a, b, c: a if a < b and a < c else b if b < c else c
print(minimum(5, 2, 8))

#2
minimum = lambda a, b, c: min(a, b, c)
print(minimum(5, 2, 8))

#number is positive, negative, or zero
number = lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(number(0))

#find the length of a string
name=lambda str:len(str)
print(name("rashi"))

#reverse a string
reverse = lambda text: text[::-1]
print(reverse("Rashi"))

#whether a string is palindrome
palindrome=lambda text:"palindrome" if text==text[::-1] else "Not palindrome"
print(palindrome("abcabc"))
