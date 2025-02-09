# chapter 8 

# function and recursion

# a=10
# b=12
# c=15

# avg=(a+b+c)/3

# print(avg)

# to do this multiple time we can use function

# function defination

# def avg():
#     a=int(input("Enter 1st number: "))
#     b=int(input("Enter 2nd number: "))
#     c=int(input("Enter 3rd number: "))
#     avg=(a+b+c)/3
#     print("Average of 3 numbers is: ",avg)

# avg()

# def goodday():
#     print("Good Day")

# goodday()

# def goodday(name):
#     print("Good Day" + name)

# goodday("harry")

# def newgoodDay(name,ending):
#     print("Good Day" + name )
#     print(ending)

# newgoodDay("harry","bye")

# def newgoodDay(name,ending):
#     print("Good Day" + name )
#     print(ending)
#     return 5

# newgoodDay("harry","bye")

# def greeting(name,ending="Thank you"):
#     print("Good Day" + name )
#     print(ending)

# greeting("harry")
# greeting("harry","bye")

# recursion

# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     return n*factorial(n-1)

# n=int(input("Enter the number: "))
# print("The factorial of ",n," is ",factorial(n))


# chapter 8 practice set

# 1.

# def greatestNumber(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c

# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# c=int(input("Enter 3rd number: "))

# print("The greatest number is: ",greatestNumber(a,b,c))

# 2.

# def farenheit(celcius):
#     return (celcius*(9/5))+32

# celcius=int(input("Enter the temperature in celcius: "))
# print("The temperature in farenheit is: ",farenheit(celcius))

# 3.

# print("a")
# print("b")
# print("c", end=" ")
# print("d", end=" ")


# 4.

# def recursiveSum(n):
#     if n==1:
#         return 1
#     return n+recursiveSum(n-1)

# n=int(input("Enter the number: "))
# print("The sum of first ",n," natural numbers is: ",recursiveSum(n))

# 5.

# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)

# pattern(5)

# 6.

# def inchtoCm(inch):
#     return inch*2.54

# inch=int(input("Enter the length in inches: "))
# print("The length in cm is: ",inchtoCm(inch))

# 7.

# def rem(l, word):
#     n = [] 
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n


# l = ["Harry", "Rohan", "Shubham", "an"]

# print(rem(l, "an"))

# 8.

# def multiply(n):
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n*i}")

# multiply(5)
