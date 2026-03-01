'''
A number is palindrome if it reads the same forward and backward.

Examples:
121 → Palindrome
1331 → Palindrome
123 → Not Palindrome

'''
#using logic 
n = int(input("Enter number: "))
temp = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#using string method 
n = input("Enter number: ")
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")