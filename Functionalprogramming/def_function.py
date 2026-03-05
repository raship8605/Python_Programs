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