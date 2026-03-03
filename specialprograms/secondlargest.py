numbers = [10, 25, 5, 80, 50]
unique_numbers = list(set(numbers))  # Remove duplicates
unique_numbers.sort()  # Sort ascending
second_largest = unique_numbers[-2]  # Second last element
print("Second largest element:", second_largest)

#without sort

first = second = float('-inf')
for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second largest element:", second)