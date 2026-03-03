'''
raising own exception by using raise keyword
raise allows you to manually throw an exception

Know common built-in exceptions:
ZeroDivisionError, ValueError, TypeError, IndexError, KeyError, FileNotFoundError
Prefer specific exceptions over a general Exception.
Always use finally for cleanup, like closing files or connections.
Be ready for nested try-except or handling multiple exceptions in one block.
'''
age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("Age must be 18 or older to vote!")
else:
    print("You are eligible to vote.")