# Writing to a file

with open("example.txt", "w") as f:
    f.write("Hello, this is a test file.\nThis file has multiple lines.\nPython is fun!")

# Reading from a file

with open("example.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

#with automatically closes file