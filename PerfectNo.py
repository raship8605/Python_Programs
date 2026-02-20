'''
A Perfect Number is a number equal to the sum of its proper divisors
(excluding the number itself).

Eg:
6 → 1 + 2 + 3 = 6

28 → 1 + 2 + 4 + 7 + 14 = 28
'''
num = int(input("Enter number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")