# Input string
text = input("Enter a string: ").lower()
vowels = 0
consonants = 0
vowel_letters = "aeiou"
for char in text:
    if char.isalpha():  # Consider only letters
        if char in vowel_letters:
            vowels += 1
        else:
            consonants += 1
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")