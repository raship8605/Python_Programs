from collections import Counter

with open("example.txt", "r") as f:
    content = f.read().lower().replace('\n', ' ')

# Split words
words = content.split()

# Count frequency
freq = Counter(words)

# Find most common word
most_common_word, count = freq.most_common(1)[0]

print(f"The most frequent word is '{most_common_word}' appearing {count} times.")