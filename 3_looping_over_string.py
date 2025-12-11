# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.

# Challenge:
# Count how many vowels are in the word.




word = input("Say any random word: ")

for char in word:
    print(char)


# initializing count variable
count = 0

# declaring a variable for index
i = 0


for i in range(len(word)):
    if (
        (word[i] == "a")
        or (word[i] == "e")
        or (word[i] == "i")
        or (word[i] == "o")
        or (word[i] == "u")
    ):
        count += 1

print("Number of vowels in the given string is: ", count)