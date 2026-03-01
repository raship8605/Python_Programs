'''
Reverse the digits of a number.

Example:
1234 → 4321
500 → 5

'''
#logic 
n = int(input("Enter number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reverse =", rev)

#string method

n = input("Enter number: ")
print("Reverse =", n[::-1])


#using for loop

n = int(input("Enter number: "))
rev = 0
for i in str(n):
    rev = rev * 10 + int(i)
print("Reverse =", rev)