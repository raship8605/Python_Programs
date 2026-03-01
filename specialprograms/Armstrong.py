'''
A number is Armstrong if the sum of the cube (or power of digits) equals the number.
Example:
153 → 1³ + 5³ + 3³ = 153 

'''
n = int(input("Enter number: "))
temp = n
sum = 0
while n > 0:
    digit = n % 10
    sum += digit ** 3
    n = n // 10
if temp == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")