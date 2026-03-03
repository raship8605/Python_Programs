'''
A perfect number is a number that is equal to the sum of its proper divisors 
(all positive divisors excluding itself).

eg:
   6 → divisors are 1, 2, 3 → sum = 1 + 2 + 3 = 6 
   28 → divisors are 1, 2, 4, 7, 14 → sum = 28 
'''
num = int(input("Enter a number: "))
# Initialize sum
sum_of_divisors = 0
# Loop to find divisors
for i in range(1, num):
    if num % i == 0:  # if i divides num
        sum_of_divisors += i
# Check if sum of divisors equals the number
if sum_of_divisors == num:
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is not a Perfect Number")