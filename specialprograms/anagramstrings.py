'''
An anagram means two strings have the same letters in the 
same quantity but possibly in a different order.

eg 
"listen" and "silent" → anagrams 
"hello" and "world" → not anagrams 


'''
str1 = input("Enter first string: ").lower().replace(" ", "")
str2 = input("Enter second string: ").lower().replace(" ", "")
if sorted(str1) == sorted(str2):
    print(f'"{str1}" and "{str2}" are Anagrams')
else:
    print(f'"{str1}" and "{str2}" are not Anagrams')