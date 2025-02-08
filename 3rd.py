# chapter 3

# name="Ariyan"
# name1='Ariyan'
# name2="""Ariyan"""
# name3='''Ariyan'''
# string is immmutable
# nameShort=name[0:3] #start from 0 index to all the way to 3rd index but not include 3rd index
# print(nameShort)
# char1=name[0]
# print(char1)

# name="harry"
# print(name[0:3])
# print(name[-4:-1])
# print(name[1:4])
# print(name[:4])
# print(name[1:])

# slicing with skip value
# number1="0123456789"
# print(number1[1:7:2])

# string function
# name="Ariyan"
# print(len(name))
# print(name.endswith("y"))
# print(name.startswith("a"))
# print(name.capitalize())

# escape sequence \n \t \" \' \\
# a="Ariyan is a good boy \nHe wants to be a web developer";
# print(a)


# chapter 3 practice set

# 1.
# name=input("Enter your name: ")
# print("Good Afternoon "+name)
# print(f"Good Afternoon {name}")

# 2.

# letter = '''  
# Dear <|Name|>, 
#                 You are selected! 
#                 <|Date|'''

# print(letter.replace("<|Name|>", "Ariyan").replace("<|Date|", "12/12/2021"))

# 3.
# name="Ariyan is a  good boy"
# name2="Ariyan is a good boy"
# print(name.find("  "))
# print(name2.find("  "))

# 4.
# name="Ariyan is a  good boy"
# print(name.replace("  "," "))

# 5.
# letter = "Dear Harry,\n\t This python course is nice. \nThanks!" 
# print(letter)



# from chatgpt some method

# Here are some of the most commonly used string functions in Python:

# 1. len()
# Returns the length of the string.

# s = "Hello"
# print(len(s))  # Output: 5

# 2. lower()
# Converts the string to lowercase.

# s = "Hello"
# print(s.lower())  # Output: "hello"

# 3. upper()
# Converts the string to uppercase.

# s = "Hello"
# print(s.upper())  # Output: "HELLO"

# 4. strip()
# Removes leading and trailing spaces. just like the trim method in js

# s = "  Hello  "
# print(s.strip())  # Output: "Hello"

# 5. replace()
# Replaces a substring with another.

# s = "Hello World"
# print(s.replace("World", "Python"))  # Output: "Hello Python"

# 6. split()
# Splits the string into a list based on a delimiter.

# s = "apple,banana,orange"
# print(s.split(","))  # Output: ['apple', 'banana', 'orange']

# 7. join()
# Joins elements of a list into a string.

# words = ["Hello", "World"]
# print(" ".join(words))  # Output: "Hello World"

# 8. find()
# Returns the index of the first occurrence of a substring.

# s = "Hello World"
# print(s.find("World"))  # Output: 6

# 9. startswith() & endswith()
# Checks if a string starts or ends with a specific substring.

# s = "Hello World"
# print(s.startswith("Hello"))  # Output: True
# print(s.endswith("World"))    # Output: True

# 10. count()
# Counts occurrences of a substring.

# s = "banana"
# print(s.count("a"))  # Output: 3

# 11. capitalize()
# Capitalizes the first letter of the string.

# s = "hello world"
# print(s.capitalize())  # Output: "Hello world"

# 12. title()
# Converts the first letter of each word to uppercase.

# s = "hello world"
# print(s.title())  # Output: "Hello World"
