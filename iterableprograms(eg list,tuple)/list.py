#1- Write a program to access the third element from the given list. Input: [10, 20, 30, 40, 50]

li=[10, 20, 30, 40, 50]
print(li[2])

#2 Write a program to access the last element from the given list using negative indexing. Input: ['apple', 'banana', 'cherry', 'date']

fruits= ['apple', 'banana', 'cherry', 'date']
print(fruits[-1])

#3 Write a program to change the second element to 100 in the given list. Input: [5, 10, 15, 20, 25]

li= [5, 10, 15, 20, 25]
li[1]=100
print(li)

#4 Write a program to access the first element using negative indexing. Input: [7, 14, 21, 28, 35]

li=[7, 14, 21, 28, 35]
print(li[-5])

#5 Write a program to access the second last element from the given list. Input: [1, 2, 3, 4, 5, 6]

li=[1, 2, 3, 4, 5, 6]
print(li[-2])

#6 Write a program to extract the first three elements from the given list. Input: [100, 200, 300, 400, 500, 600]

ele=[100, 200, 300, 400, 500, 600]
print(ele[0:3])

#7 Write a program to extract all elements except the first two from the given list. Input: [2, 4, 6, 8, 10, 12]

li=[2, 4, 6, 8, 10, 12]
print(li[2::])

#8 Write a program to extract every alternate element from the given list. Input: [5, 10, 15, 20, 25, 30, 35]

li=[5, 10, 15, 20, 25, 30, 35]
print(li[::2])

#9 Write a program to reverse the given list using slicing. Input: [1, 3, 5, 7, 9]

li=[1, 3, 5, 7, 9]
print(li[::-1])

#10 Write a program to extract elements from index 2 to 5 from the given list. Input: [11, 22, 33, 44, 55, 66, 77]

li= [11, 22, 33, 44, 55, 66, 77]
print(li[2:6])

#nested sclicing
#11 Write a program to access the second element from the first nested list. Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

li=[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
print(li[0][0][1])

#12 Write a program to extract the last element from the last nested list. Input: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

li=[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
print(li[2][2])

#13 Write a program to extract the second and third lists from a given nested list. Input: [[10, 20], [30, 40], [50, 60], [70, 80]]

li= [[10, 20], [30, 40], [50, 60], [70, 80]]
print(li[1:3])

#14 Write a program to extract the second element from all nested lists. Input: [[1, 9], [2, 8], [3, 7], [4, 6]] :

nested_list = [[1, 9], [2, 8], [3, 7], [4, 6]]
second_elements = []
for i in nested_list:
    second_elements.append(i[1])
print(second_elements)

#15 Write a program to reverse all sublists in a nested list. Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

li=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
reversed_list=[]
for i in li:
  reversed_list.append(i[::-1])
print(reversed_list)

#list adding methods
#append
#1- Write a program to append the number 100 to the given list. Input: [10, 20, 30, 40]

numbers=[10,20,30,40]
numbers.append(100)
print(numbers)

#2 Write a program to append a string "Hello" to the given list. Input: ['apple', 'banana', 'cherry']

fruits= ['apple', 'banana', 'cherry']
fruits.append("Hello")
print(fruits)

#3 Write a program to append a list [5, 6, 7] as a single element in the given list. Input: [1, 2, 3, 4]

li=[1, 2, 3, 4]
li.append([5,6,7])
print(li)

#extend() Function Questions
#4- Write a program to extend the given list by adding another list [50, 60, 70]. Input: [10, 20, 30, 40]

li=[10, 20, 30, 40]
li.extend([50,60,70])
print(li)

#Write a program to extend a list of numbers [7, 8, 9] with another list [10, 11, 12]. Input: [7, 8, 9]

li=[7,8,9]
li.extend([10,11,12])
print(li)

#6 Write a program to extend a list of strings ["cat", "dog"] with another list ["lion", "tiger"].

li=["lion", "tiger"]
l=["cat", "dog"]
li.extend(l)
print(li)

#pop() Function Questions
#7 Write a program to remove the last element from the given list using the pop function. Input: [10, 20, 30, 40]

li=[10,20,30,40]
li.pop()
print(li)

#8 Write a program to remove the third element from the given list using the pop function. Input: [1, 2, 3, 4, 5]

li=[1,2,3,4,5]
li.pop(2)
print(li)

#9 Write a program to remove the first element from the given list using the pop function. Input: [100, 200, 300, 400]

li= [100, 200, 300, 400]
li.pop(0)
print(li)

#remove() Function Questions
#10 Write a program to remove the element 20 from the given list. Input: [10, 20, 30, 40, 50]

li=[10,20,30,40,50]
li.remove(20)
print(li)

#11 Write a program to remove the first occurrence of "apple" from the given list.
#Input: ["banana", "apple", "cherry", "apple"]

fruits=["banana", "apple", "cherry", "apple"]
fruits.remove("apple")
print(fruits)

#12 Write a program to remove the number 5 from the given list if it exists. Input: [1, 2, 3, 4, 5, 6]

li= [1, 2, 3, 4, 5, 6]
li.remove(5)
print(li)

#index() Function Questions
#13 Write a program to find the index of the element 50 in the given list. Input: [10, 20, 30, 40, 50, 60]

li= [10, 20, 30, 40, 50, 60]
print(li.index(50))

#14 Write a program to find the index of "cherry" in the given list. Input: ["apple", "banana", "cherry", "date"]

fruits=["banana", "apple", "cherry", "apple"]
print(fruits.index("cherry"))

#15 Write a program to find the index of the number 100 in the given list. If not found, print "Not found". Input: [10, 20, 30, 40]

li=[10, 20, 30, 40]
# print(li.index(100))

#not found error

#count() Function Questions
#16 Write a program to count the occurrences of 5 in the given list. Input: [1, 5, 2, 5, 3, 5, 4]

li=[1, 5, 2, 5, 3, 5, 4]
print(li.count(5))

#17 Write a program to count how many times "apple" appears in the given list.
#input: ["apple", "banana", "apple", "cherry", "apple"]

li=["apple", "banana", "apple", "cherry", "apple"]
print(li.count("apple"))

#18 Write a program to count the occurrences of 100 in the given list. Input: [10, 20, 30, 40, 50]

li=[10,20,30,40,50]
print(li.count(100))

#min() and max() Function Questions
#19 Write a program to find the minimum value in the given list. Input: [45, 12, 78, 34, 23]

li=[45, 12, 78, 34, 23]
print(min(li))

#20 Write a program to find the maximum value in the given list. Input: [99, 55, 73, 21, 64]

li=[99, 55, 73, 21, 64]
print(max(li))