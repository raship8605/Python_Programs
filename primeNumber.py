#A prime number is a number greater than 1 that has only 2 factors → 1 and itself.
#Example: 2, 3, 5, 7, 11

n = int(input("Enter number: "))
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")