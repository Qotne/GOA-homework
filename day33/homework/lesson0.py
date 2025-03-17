# 1. Format a String
name = input("Name: ")
age = input("Age: ")
print("Hello, {}! You are {} years old.".format(name, age))

# 2. Join a List of Strings
print(" ".join(["Python", "is", "fun"]))

# 3. Split a String
print(input("Sentence: ").split())

# 4. Replace Substrings
s = input("Sentence: ")
print(s.replace(input("Replace: "), input("With: ")))

# 5. Convert to Lowercase
print(input("Text: ").lower())

# 6. Convert to Uppercase
print(input("Text: ").upper())
