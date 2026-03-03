text = input("Enter a string: ")
unique_text = ""
for char in text:
    if char not in unique_text:
        unique_text += char
print("String after removing duplicates:", unique_text)