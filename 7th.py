# chapter 7

# loop in python

# while loop

# i=1
# while(i<6):
#     print(i)
#     i+=1

# 1 to 50
# i=1
# while(i<=50):
#     print(i)
#     i+=1

# 50 to 1
# i=50
# while(i>=1):
#     print(i)
#     i-=1

# l1=[1,"harry",False]
# i=0
# while(i<len(l1)):
#     print(l1[i])
#     i+=1

# for loop

# for i in range(4):
#     print(i)

# for a in range(1,100,2):
#     print(a)

# list in loop

# l1=[1,3,5,6,3214,4,6345]
# for i in l1:
#     print(i)

# tupples in loop

# t=(1,2,3,4,5,6,7,8,9)
# for i in t:
#     print(i)

# string in loop

# s="harry"
# for i in s:
#     print(i)

# for with else

# l=[1,2,3,4,5,6,7,8,9]

# for item in l:
#     print(item)

# else:
#     print("Done")

# break and continue

# for i in range(100):
#     if(i==34):
#         break
#     print(i)


# for i in range(100):
#     if(i==34):
#         continue
#     print(i)
 

# pass statement
# for a in range(100):
#     pass

# i=0
# while(i<=100):
#     print(i)
#     i+=1

# practice set chaptert 7

# 1.

# a=int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{a}X{i}={a*i}")

# 2.

# l = ["Harry", "Soham", "Sachin", "Rahul"] 

# for name in l:
#     if(name.startswith("S")):
#         print("Hello "+name)
    
# 3.

# n=int(input("Enter a number: "))
# i=1

# while(i<11):
#     print(f"{n}X{i}={n*i}")
#     i+=1

# 4.

# n=int(input("Enter a number: "))

# for i in range(2,n):
#     if(n%i)==0:
#         print("Number is not prime")
#         break

# else:
#     print("Number is prime")

# 5.
 
# n=int(input("Enter a number: "))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)

# 6.

# n=int(input("Enter a number: "))
# i=1
# fact=1
# while(i<=n):
#     fact*=i
#     i+=1
# print(fact)

# 7.

# n=int(input("Enter a number: "))

# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")


# 8.

# n=int(input("Enter a number: "))

# for i in range(1,n+1):
#     print("*"*(i),end="")
#     print("")

# 9.

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")

# 10.

# n=int(input("Enter a number: "))
# i=10
# while(i>0):
#     print(f"{n}X{i}={n*i}")
#     i-=1
