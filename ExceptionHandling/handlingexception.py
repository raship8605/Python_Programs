'''
What is Exception Handling?

Exception: An error that occurs during program execution (e.g., dividing by zero, file not found).
Exception Handling: Catching errors so the program doesn’t crash.
Done using try, except blocks in Python.

syntax:
    try:
       #CODE that may raise exception 
       #problematic statements 
    except ZeroDivisionError: 
       #handling statments
    except ValueError:
        #multiple handling statements for multiple exception
'''
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except Exception as e:
    print("An error occurred:", e)


'''
Exception catches any type of exception
as e stores the exception object for printing


'''