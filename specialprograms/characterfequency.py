'''Character frequency – Count how many times each character appears.
'''
text = input("Enter a string: ")
char_freq = {}
for char in text:
    if char in char_freq:
        char_freq[char] += 1 
    else:
        char_freq[char] = 1  
for char, count in char_freq.items():
    print(f"'{char}': {count}")

'''
output:
     Enter a string: raashi
'r': 1
'a': 2
's': 1
'h': 1
'i': 1

'''