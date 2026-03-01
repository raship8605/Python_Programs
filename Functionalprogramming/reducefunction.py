'''
reduce() combines all elements of an iterable into one single value using a function.
Used for sum, product, max, min, concatenation

syntax:  from functools import reduce
         reduce(function, iterable)

 Function must take 2 arguments
Returns a single value

Example:  from functools import reduce
          nums = [1,2,3,4]
          total = reduce(lambda a, b: a + b, nums)
          print(total)

'''

#reduce() to find sum of all elements in a list
from functools import reduce
li=[10,2,3,4,5,6,4]
sum=reduce(lambda a, b :a+b,li)
print(sum)

#educe() to find product of list elements
from functools import reduce
li=[10,3,4,6,7,5,3,6,2]
product=reduce(lambda a,b:a*b,li)
print(product)

#reduce() to find maximum number in a list
from functools import reduce
li = [10,3,4,6,7,5,3,6,2]
maxelement = reduce(lambda a, b: a if a > b else b, li)
print(maxelement)

#reduce() to concatenate list of strings.
from functools import reduce
name = ["rashi", "ramnarayan", "pardeshi"]
concat = reduce(lambda a, b: a + b, name)
print(concat)

#reduce() to find factorial of a number.
from functools import reduce
n = 5
factorial = reduce(lambda a, b: a * b, range(1, n+1))
print(factorial)
