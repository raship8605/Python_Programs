my_dict = {"name": "Rashi", "age": 20}
try:
    print(my_dict["address"])
except KeyError:
    print("Error: Key does not exist!")
finally:
    print("Dictionary access attempted.\n")