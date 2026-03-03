'''
raising own exception by using raise keyword

'''
age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("Age must be 18 or older to vote!")
else:
    print("You are eligible to vote.")