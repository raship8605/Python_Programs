try:
    with open("data.txt", "r") as f:
        content = f.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("File operation finished.\n")