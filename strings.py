# Define a sample string
s = "Hello, Python! Welcome to string manipulation."

print("=== String Operations ===\n")

# 1. Length of the string
print("1. Length of the string:", len(s))

# 2. Convert to uppercase
print("2. Uppercase:", s.upper())

# 3. Convert to lowercase
print("3. Lowercase:", s.lower())

# 4. Swap case
print("4. Swapcase:", s.swapcase())

# 5. Capitalize the first letter
print("5. Capitalize:", s.capitalize())

# 6. Title case (capitalize first letter of each word)
print("6. Title Case:", s.title())

# 7. Count occurrences of a substring
print("7. Count of 'o':", s.count('o'))

# 8. Find the first occurrence of a substring
print("8. Index of 'Python':", s.find('Python'))

# 9. Check if the string starts with a substring
print("9. Starts with 'Hello':", s.startswith("Hello"))

# 10. Check if the string ends with a substring
print("10. Ends with 'manipulation.':", s.endswith("manipulation."))

# 11. Replace a substring
print("11. Replace 'Python' with 'World':", s.replace('Python', 'World'))

# 12. Split the string into a list of words
print("12. Split into words:", s.split())

# 13. Join a list of strings into one
words = ["Join", "these", "words"]
print("13. Join words with '-':", '-'.join(words))

# 14. Strip whitespace from the ends
s_with_spaces = "   Trim spaces   "
print("14. Strip spaces:", s_with_spaces.strip())

# 15. Strip characters from the left
print("15. Left strip spaces:", s_with_spaces.lstrip())

# 16. Strip characters from the right
print("16. Right strip spaces:", s_with_spaces.rstrip())

# 17. Check if all characters are alphanumeric
print("17. Is alphanumeric:", s.isalnum())

# 18. Check if all characters are alphabetic
print("18. Is alphabetic:", s.isalpha())

# 19. Check if all characters are digits
num = "12345"
print("19. Is numeric:", num.isdigit())

# 20. Check if all characters are lowercase
print("20. Is lowercase:", s.islower())

# 21. Check if all characters are uppercase
print("21. Is uppercase:", s.isupper())

# 22. Check if the string is a title
print("22. Is title:", s.istitle())

# 23. Check if the string is printable
print("23. Is printable:", s.isprintable())

# 24. Check if the string contains only whitespace
only_space = "   "
print("24. Contains only whitespace:", only_space.isspace())

# 25. Center align the string
print("25. Center aligned:", s.center(50, '*'))

# 26. Left align the string
print("26. Left aligned:", s.ljust(50, '-'))

# 27. Right align the string
print("27. Right aligned:", s.rjust(50, '-'))

