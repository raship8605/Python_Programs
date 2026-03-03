numbers = [10, 25, 5, 80, 50]
largest = max(numbers) #largest
smallest = min(numbers) #smallest
print("Largest element:", largest)
print("Smallest element:", smallest)


#using loop

largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)