'''
filter() selects elements from an iterable based on a condition.
Keeps elements where condition is True

syntax: filter(function, iterable)
        function → returns True/False
        iterable → list, tuple, etc.
        Returns → filter object → convert to list.

Example:  nums = [1,2,3,4,5,6]
          even = list(filter(lambda x: x % 2 == 0, nums))
          print(even)
'''


#filter() to find all even numbers from a list.
li=[1,2,3,4,5,6,7,8,9]
even=filter(lambda num: num%2==0,li)
print(list(even))

#filter() to remove negative numbers from a list.
li=[2,3,-4,-3,3,-4,-6,-6]
removenegative=filter(lambda num:num>0,li)
print(list(removenegative))

#ilter() to find numbers greater than 50
numbers=[200,3,24,60,79,43,678,48,58]
greaternumber=filter(lambda num:num>50,numbers)
print(list(greaternumber))

#filter() to find palindrome words from a list
words = ["rashi", "abccba", "shiv", "123321"]
palindromeword = filter(lambda word: word == word[::-1], words)
print(list(palindromeword))

#filter() to find words starting with letter “A”
names = ["rashi","amar","aarohi","shiv","ram"]
anames=filter(lambda text: text.startswith("a"),names)
print(list(anames))