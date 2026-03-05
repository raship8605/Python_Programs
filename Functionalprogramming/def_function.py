# 1- Write a function that calculates the area of a rectangle given its length and width.

def area(length,width):
  areaofrec=length*width
  return areaofrec
print(area(10,12))

# 2- Create a function that converts temperature from Celsius to Fahrenheit.

def temconverter(celsius):
  Fahrenheit = (celsius * 9/5) + 32
  return Fahrenheit
print(temconverter(45))

#3.Write a function to find the factorial of a number.bold text

def factorial(num):
  fact=1
  if num==1 or num==0:
    return 1
  else:
    return num*factorial(num-1)
print(factorial(5))

#4-Design a function to check if a given number is prime.

def checkprime(num):
    if num <= 1:
        print("Not prime!!")
    else:
        flag = 0
        for i in range(2, num):
            if num % i == 0:
                flag = 1
                break
        if flag == 0:
            print("Prime")
        else:
            print("Not prime!!")
print(checkprime(3))

#5-Create a function that reverses a given string

def reversestring(str):
  rev=""
  for i in str:
    rev=i+rev
  return rev
print(reversestring("rashi"))

#6-Write a function to compute the nth Fibonacci number

def Fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print(a, end=" ")
        a, b = b, a + b
print(Fibonacci(8))

#7-Create a function to find the largest element in a list.

def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
numbers = [10, 45, 23, 89, 12]
print("Largest element:", find_largest(numbers))

#8- Design a function to count the number of vowels in a string

def countvowels(string):
    count = 0
    for i in string:
        if i in "aeiouAEIOU":
            count += 1
    return count
print(countvowels("rashi"))

#9-Write a function to calculate the factorial of each number in a given list

def factorialofeachele(list):
  result=[]
  for num in list:
    fact=1
    for i in range(1,num+1):
      fact=fact*i
    result.append(fact)
  return result

print(factorialofeachele([2,3,4,5]))

#10- Create a function to check if a string is a palindrome

def palindrome(string):
  if string==string[::-1]:
    return f" Palindrome!!"
  else:
    return f"Not palindorme!!"
print(palindrome("rashi"))

#11: Write a function to find the sum of all elements in a list.

def sum(list):
  sum=0
  for i in list:
    sum=sum+i
  return sum

print(sum([1,2,3,4,5,5]))

#12: Create a function to sort a list of integers in ascending order

def sortlist(lst):
    return sorted(lst)
print(sortlist([5, 2, 9, 1, 3]))

#13: Design a function to calculate the area of a circle given its radius

def areaofcircle(radius):
  area=3.14*radius*radius
  return area
print(areaofcircle(4))