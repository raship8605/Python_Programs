'''
Add all digits of a number.

Eg:
1234 → 1 + 2 + 3 + 4 = 10
'''
#using for loop
n = int(input("Enter number: "))
sum = 0
for i in n:
    sum=sum+i
print("Sum of digits =", sum)

#using while loop
n = int(input("Enter number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10
print("Sum of digits =", sum)