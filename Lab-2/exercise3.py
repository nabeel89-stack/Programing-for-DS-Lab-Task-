text = input("Enter a word or sentence: ")

chars = 0
vowels = 0
spaces = 0
for ch in text:
    chars += 1
    if ch.lower() in "aeiou":
        vowels += 1
    if ch == " ":
        spaces += 1

print("Characters:", chars)
print("Vowels:", vowels)
print("Spaces:", spaces)
