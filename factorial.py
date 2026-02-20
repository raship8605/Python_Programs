
'''
Factorial of a number means multiplying that number by all the smaller positive numbers till 1.
Factorial of n = n × (n-1) × (n-2) … × 1
Eg:  5! = 5 × 4 × 3 × 2 × 1 = 120
Special case:
0! = 1

 Time Complexity:
Loop → O(n)
Recursion → O(n)
'''
#simple method
num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*1
print(f"Factorial of {num} is {fact}")

#using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter number: "))
print("Factorial =", factorial(num))

#using builtin fun
import math
num = int(input("Enter number: "))
print("Factorial =", math.factorial(num))