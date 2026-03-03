with open("example.txt", "r") as f:
    content = f.read()

# Number of characters
num_chars = len(content)

# Number of words
num_words = len(content.split())

# Number of lines
num_lines = content.count('\n') + 1  # +1 for last line

print("Characters:", num_chars)
print("Words:", num_words)
print("Lines:", num_lines)