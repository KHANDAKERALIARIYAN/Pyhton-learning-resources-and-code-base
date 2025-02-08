# chapter 4 list and tuple

# list is a collection of items in a particular order
# example=[1,"Arif",3.14,"delhi"]
# print(example)

# friends = ['john', 'pat', 'gary', 'michael'] #unlike string list are mutable
# friends[0]='james'
# print(friends)
# print(friends[1])
# print(friends[1:4])
# friends.append("Harry") #append is used to add element at the end of the list
# print(friends)

# l1=[1,2,4,38,8,11]
# l1.sort() #sort is used to sort the list
# l1.reverse() #reverse is used to reverse the list
# l1.insert(2,3) #insert is used to insert the element at the given index
# l1.remove(38) #remove is used to remove the element from the list
# l1.pop(2) #pop is used to remove the element at the given index
# l1.append(11) #append is used to add the element at the end of the list

# print(l1)

# Tuple is a collection of items in a particular order but it is immutable
# a=(1,2,3,4,5)
# print(a)
# print(type(a))

# a=(1,3.14,"Arif","Delhi")
# print(a)
# a[0]=2
# print(a) #this will give an error because tuple is immutable

# a=(1,2,3,4,5)
# print(a[0])

# no=a.count(4)
# print(no) #this will give an error because count is not a function of tuple

# i=a.index(4)
# print(i) #this will give an error because index is not a function of tuple

# method from chatgpt
# tuples methods

# Tuples in Python have limited built-in methods since they are immutable (cannot be modified after creation). Here are some of the most commonly used tuple methods:

# 1. count()
# Returns the number of times a specified value appears in the tuple.

# t = (1, 2, 3, 2, 4, 2)
# print(t.count(2))  # Output: 3

# 2. index()
# Returns the first index of the specified value in the tuple.

# t = (10, 20, 30, 40, 50)
# print(t.index(30))  # Output: 2

# Other Useful Tuple Operations:
# Even though tuples don’t have many methods, you can still perform various operations:

# 3. Tuple Concatenation (+)
# Combines two tuples into a new one.

# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# t3 = t1 + t2
# print(t3)  # Output: (1, 2, 3, 4, 5, 6)

# 4. Tuple Repetition (*)
# Repeats a tuple multiple times.

# t = (1, 2, 3)
# print(t * 3)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 5. Tuple Slicing ([:])
# Extracts parts of a tuple.

# t = (10, 20, 30, 40, 50)
# print(t[1:4])  # Output: (20, 30, 40)

# 6. Tuple Unpacking
# Assigns tuple elements to variables.

# t = (100, 200, 300)
# a, b, c = t
# print(a, b, c)  # Output: 100 200 300
# Since tuples are immutable, methods like append(), remove(), or sort() (which work on lists) do not work on tuples.

# practice set 4

# 1.
# fruits=[]

# f1=int(input("Enter the name of the fr)uit: ")
# fruits.append(f1)
# f2=int(input("Enter the name of the fr)uit: ")
# fruits.append(f2)
# f3=int(input("Enter the name of the fr)uit: ")
# fruits.append(f3)
# f4=int(input("Enter the name of the fr)uit: ")
# fruits.append(f4)
# f5=int(input("Enter the name of the fr)uit: ")
# fruits.append(f5)
# f6=int(input("Enter the name of the fr)uit: ")
# fruits.append(f6)
# f7=int(input("Enter the name of the fr)uit: ")
# fruits.append(f7)

# print(fruits)

# 2.

# marks=[]

# f1=int(input("Enter the marks here: "))
# marks.append(f1)
# f2=int(input("Enter the marks here: "))
# marks.append(f2)
# f3=int(input("Enter the marks here: "))
# marks.append(f3)
# f4=int(input("Enter the marks here: "))
# marks.append(f4)
# f5=int(input("Enter the marks here: "))
# marks.append(f5)
# f6=int(input("Enter the marks here: "))
# marks.append(f6)

# marks.sort()
# print(marks)


# 3.
# a=(1,2,"harry")
# a[0]=45
# print(a) #this will give an error because

# 4.

# l=(1,2,3,4,5,6,7,8,9,10)
# print(sum(l))

# 5.
# a = (7, 0, 8, 0, 0, 9)
# b=a.count(0)
# print(b)