try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found! Please check the filename.")
finally:
    print("File handling attempt finished.")