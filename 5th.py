# chapter 5 

# set and dictionary

# dictionary is a collection of key value pairs

# marks={
#     "harry": 90,
#     "rohan": 56,
#     "skillf": 78,
#     "shubham": 45
# }
# print(marks)
# print(type(marks))
# print(marks["harry"]) 

#  dictionaries methods

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"shubham": 55,"rohan": 57})
# print(marks)
# print(marks.get("harry")) # it will not give error if key is not present
# print(marks["harry"]) # it will give error if key is not present

# print(marks.get("harry")) # prints none
# print(marks["harry"]) # return error

# method from chatgpt

# Python dictionaries come with many useful built-in methods. Here are some of the most commonly used ones:

# 1. keys()
# Returns a view of all keys in the dictionary.

# d = {
# "name": "Alice",
# "age": 25,
# "city": "New York"
# }
# print(d.keys())  # Output: dict_keys(['name', 'age', 'city'])

# 2. values()
# Returns a view of all values in the dictionary.

# print(d.values())  # Output: dict_values(['Alice', 25, 'New York'])

# 3. items()
# Returns key-value pairs as tuples in a view object.

# print(d.items())  
# Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# 4. get()
# Retrieves the value for a given key; returns None if the key doesn’t exist (instead of an error).

# print(d.get("name"))  # Output: Alice
# print(d.get("gender", "Not Found"))  # Output: Not Found

# 5. update()
# Merges another dictionary or key-value pairs into the current dictionary.

# d.update({"age": 26, "gender": "Female"})
# print(d)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'gender': 'Female'}

# 6. pop()
# Removes a key and returns its value.

# age = d.pop("age")
# print(age)  
# Output: 26
# print(d)  
# Output: {'name': 'Alice', 'city': 'New York', 'gender': 'Female'}

# 7. popitem()
# Removes and returns the last inserted key-value pair (useful in Python 3.7+).

# last_item = d.popitem()
# print(last_item)  # Output: ('gender', 'Female')
# print(d)  # Output: {'name': 'Alice', 'city': 'New York'}

# 8. clear()
# Removes all items from the dictionary.

# d.clear()
# print(d)  # Output: {}

# 9. setdefault()
# Returns the value of a key; if the key does not exist, it adds it with a default value.

# d = {"name": "Alice", "city": "New York"}
# d.setdefault("age", 25)
# print(d)  # Output: {'name': 'Alice', 'city': 'New York', 'age': 25}

# 10. copy()
# Returns a shallow copy of the dictionary.

# d2 = d.copy()
# print(d2)  # Output: {'name': 'Alice', 'city': 'New York', 'age': 25}

# set

# set is a collection of non repetitive elements
# s1={}
# print(type(s1)) # it will give dictionary

# s1={1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9}
# print(s1) # it will remove the repetitive elements
# print(type(s1)) # it will give set

# s={1,2,3,4,5,6,7,8,9}

# s.add(12)
# print(s,type(s))

# Python sets come with several useful built-in methods. Here are some of the most commonly used ones:

# 1. add()
# Adds an element to the set.

# s = {1, 2, 3}
# s.add(4)
# print(s)  # Output: {1, 2, 3, 4}

# 2. remove()
# Removes an element from the set (raises an error if the element is not found).

# s.remove(2)
# print(s)  # Output: {1, 3, 4}

# 3. discard()
# Removes an element from the set (does not raise an error if the element is not found).

# s.discard(10)  # No error, even though 10 is not in the set
# print(s)

# 4. pop()
# Removes and returns a random element from the set.

# item = s.pop()
# print(item)  # Output: Random element from the set
# print(s)  # Output: Remaining elements in the set

# 5. clear()
# Removes all elements from the set.

# s.clear()
# print(s)  # Output: set()

# 6. union() (| Operator)
# Returns a new set containing elements from both sets.

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1.union(s2))  # Output: {1, 2, 3, 4, 5}
# print(s1 | s2)  # Output: {1, 2, 3, 4, 5} (Using | operator)

# 7. intersection() (& Operator)
# Returns a new set containing common elements of both sets.

# print(s1.intersection(s2))  # Output: {3}
# print(s1 & s2)  # Output: {3} (Using & operator)

# 8. difference() (- Operator)
# Returns elements present in the first set but not in the second set.

# print(s1.difference(s2))  # Output: {1, 2}
# print(s1 - s2)  # Output: {1, 2} (Using - operator)

# 9. symmetric_difference() (^ Operator)
# Returns elements that are in one of the sets, but not both.

# print(s1.symmetric_difference(s2))  # Output: {1, 2, 4, 5}
# print(s1 ^ s2)  # Output: {1, 2, 4, 5} (Using ^ operator)

# 10. issubset()
# Checks if one set is a subset of another.

# s1 = {1, 2}
# s2 = {1, 2, 3, 4}
# print(s1.issubset(s2))  # Output: True

# 11. issuperset()
# Checks if one set is a superset of another.

# print(s2.issuperset(s1))  # Output: True

# 12. isdisjoint()
# Returns True if two sets have no common elements.

# s3 = {7, 8, 9}
# print(s1.isdisjoint(s3))  # Output: True

# 13. copy()
# Returns a shallow copy of the set.

# s_copy = s1.copy()
# print(s_copy)  # Output: {1, 2}


# s={1,2,3,4,5,6,7,8,9}
# print(len(s))

# practice set 5

# 1.

# dictionary={
#     "madad": "help",
#     "age":"before",
#     "kew":"why",
#     "shiph":"only",
#     "kursi":"chair"
# }

# word=input("Enter the word: ")
# print(dictionary[word])

# 2.

# s=set()

# n=input("Enter the number: ")
# s.add(int(n))
# n=input("Enter the number: ")
# s.add(int(n))
# n=input("Enter the number: ")
# s.add(int(n))
# n=input("Enter the number: ")
# s.add(int(n))
# n=input("Enter the number: ")
# s.add(int(n))
# n=input("Enter the number: ")
# s.add(int(n))
# n=input("Enter the number: ")
# s.add(int(n))
# n=input("Enter the number: ")
# s.add(int(n))

# print(s)

# 3.

# s=set()
# s.add(20)
# s.add("20")
# print(s)

# 4. 

# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 
# print(len(s)) # Output: 2

# 5.
# s={}
# print(type(s)) # it will give dictionary

# 6.

# d={}

# name=input("Enter the name: ")
# language=input("Enter the language: ")
# d.update({name:language})

# name=input("Enter the name: ")
# language=input("Enter the language: ")
# d.update({name:language})

# print(d)

