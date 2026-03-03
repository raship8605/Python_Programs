numbers = [10, 20, 20, 30, 10, 40]
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print("List after removing duplicates:", unique_list)