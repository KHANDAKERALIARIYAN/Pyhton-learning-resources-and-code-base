# chapter 6

# Conditional statements
# if, elif, else

# a=int(input("Enter your age: "))
# if(a>=18):
#     print("You can vote.")
# elif(a<0):
#     print("Invalid age.")
# elif(a==0):
#     print("You are a baby and you are zero years old.")
# else:
#     print("You can't vote.")


# age=int(input("Enter your age:"))
# if(age>=18):
#     print("Yes")
# else:
#     print("No")


# odd even number

# a=int(input("Enter a number: "))
# if(a%2==0):
#     print("Even number.")
# else:
#     print("Odd number.")


# practice set chapter 6

# 1.

# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# c=int(input("Enter 3rd number: "))
# d=int(input("Enter 4th number: "))

# if(a>b and a>c and a>d):
#     print(f"{a} is greatest.")
# elif(b>a and b>c and b>d):
#     print(f"{b} is greatest.")
# elif(c>a and c>b and c>d):
#     print(f"{c} is greatest.")
# else:
#     print(f"{d} is greatest.")

# 2.

# a=int(input("Enter 1st subject marks: "))
# b=int(input("Enter 2nd subject marks: "))
# c=int(input("Enter 3rd subject marks: "))

# d=(a+b+c)/3

# if(d>=40 and a>=33 and b>=33 and c>=33):
#     print("You are passed.")
# else:
#     print("You are failed.")   

# 3.

# a="Make a lot of money"
# b="buy now"
# c="subscribe this"
# d="click this"

# message=input("Enter your message: ")

# if((a in message) or (b in message) or (c in message) or (d in message)):
#     print("Spam message.")

# else:
#     print("Not a spam message.")

# 4.

# username=input("Enter your username: ")
# length=len(username)
# if(length<10):
#     print("Username is less than 10 characters.")

# elif(length==10):
#     print("Username is equal to 10 characters.")

# else:
#     print("Username is greater than 10 characters.")

# 5.

# l1=["Harry","Sohan","Sachin","Rahul"]
# name=input("Enter your name: ")

# if(name in l1):
#     print("Yes")
# else:
#     print("No")

# 6.    

# a=int(input("Enter your marks: "))

# if(a>=90 & a<=100):
#     print("Ex")
# elif(a>=80 & a<=89):
#     print("A")
# elif(a>=70 & a<=79):
#     print("B")
# elif(a>=60 & a<=69):
#     print("C")
# elif(a>=50 & a<=59):
#     print("D")
# else:
#     print("F")

# 7.

# post='''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Proin eget tincidunt neque. Duis ut mauris ut nisi dictum
# luctus. In hac habitasse platea dictumst. Integer nec
# odio nec dolor bibendum bibendum. Nulla facilisi. Nulla
# facilisi. Nulla facilisi. Nulla facilisi. Nulla facilisi.
# Nulla facilisi. Nulla facilisi. Nulla facilisi. Nulla
# facilisi. Nulla facilisi. Nulla facilisi. Nulla facilisi.Harry'''

# if("Harry" in post):
#     print("Yes")
# else:
#     print("No")
