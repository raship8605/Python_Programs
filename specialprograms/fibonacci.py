'''
Fibonacci series is a sequence where:
   0, 1, 1, 2, 3, 5, 8, 13, 21 ...
Each number = sum of previous two numbers.

'''
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b