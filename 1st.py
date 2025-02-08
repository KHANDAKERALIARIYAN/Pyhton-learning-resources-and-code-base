# chapter 1

# print("Hello World")

# Module

# import pyjokes
# print("Printing Jokes : ")
# joke=pyjokes.get_joke()
# print(joke)

# we can use pyhton as calculator - we need to open the power shell and then we need to write python
# REPL-Read Evaluate Print Loop

# comment

# single line comment

"""
this 
is
multiline
comment
"""

# practice set

# 1.
# print("""Twinkle Twinkle, Little Star
# How I wonder what you are
# Up above the world so high
# Like a diamond in the sky
# Twinkle Twinkle Little Star
# How I wonder what you are!
# Twinkle Twinkle, Little Star
# How I wonder what you are
# Up above the world so high
# Like a diamond in the sky
# Twinkle Twinkle Little Star
# How I wonder what you are!
# """)

# 2.
# using repl

# >>> 5*1
# 5
# >>> 5*2
# 10
# >>> 5*3
# 15
# >>> 5*4
# 20
# >>> 5*5
# 25
# >>> 5*6
# 30
# >>> 5*7
# 35
# >>> 5*8
# 40
# >>> 5*9
# 45
# >>> 5*10
# 50

# 3.

# import pyttsx3
# engine=pyttsx3.init()
# engine.say("Ariyan")
# engine.runAndWait()

# 4.

# import os

# def list_directory_contents(directory):
#     try:
#         # Get the list of all files and directories in the specified directory
#         contents = os.listdir(directory)
        
#         print(f"Contents of the directory '{directory}':")
#         for item in contents:
#             print(item)
#     except FileNotFoundError:
#         print(f"Error: The directory '{directory}' does not exist.")
#     except PermissionError:
#         print(f"Error: Permission denied to access the directory '{directory}'.")

# # Example usage
# directory_path = input("Enter the path of the directory: ")
# list_directory_contents(directory_path)
