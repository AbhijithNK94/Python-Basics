# #PRINT OUTPUT#
# print("hello world")
# print("Welcome to Expertzlab")
# # ##KEYWORDS
# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# ##IDENTIFIERS
# _jh5 = 25
# print(_jh5)
# ##Python Statement
# ##Single statement in a single line
# # a=10
# # print(a)
# # a=10
# # b=5.5
# # c=5+4j
# ##Multiple statements in a single line
# a = 10;b = 5;c = 5+4j
# ##Multiline statement
# x=1+2+3+4+\
#     7+8+9+\
#     12+13
# #
# print(x)
# ##
# x=(1+2+3+4+7+8+9+12+13)
# print(x)
# ##
# # z=[1+2+3+
# #    4+8+9+
# #    8+9+17]
# # print(z)
# ##python without indendation 4 whitespace or one TAB for representing a block
# # z=100
# # for i in range(5):
# #     print(i)
# #     print(i)
# # print(z)
# ##with indentation >>> for loop in a for loop
# for i in range(10):
#     for j in range(5):
#         print(j)
#     print(i+2)
# #print(z)
# ##Python collections list
# fruits = ["apple",10,"mango","orange"]
# print(fruits)
# print(fruits[0])
# print(fruits[2])
# ##Python collections tuple
# numbers = (1,2,3)
# print(numbers)
# number1=(3)
# number=(1,) ## Comma used after the integer to form a tuple. If comma is not used the type will be integer
# print(number)
# print(type(number1))
# print(type(number))
# ##Dictionary
# al={'a':'apple','b':'ball','c':'cat'}
# v={'a','e','a','i','o','u',5}
# ##Memory allocation
# a=10
# print(a)
# print(id(a))
# b=5
# print(id(b))
# c=10
# print(id(c)) ## a and c will have same memory allocation since the values are same
# a=a+20
# print(id(a))
# d=30
# print(id(d))
# ##Python Datatypes
# x=5
# y=4.99
# z=7+2j
# w="abcdef lk"
# u="""hbvc"""
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(u))
# print(type(v))
# print(type(w))
# ##isinstance: used for validation of statement
# print(isinstance(x,int))
# print(isinstance(x,float))
# ##Indexing
# s="This is an online AI course"
# print(s)
# print(type(s))
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[12])
# print(s[4])
# print(s[11])
# print(s[0:10])
# print(len(s))
# ##Boolean Type
# a=True
# b=False
# print(type(a))
# print(type(b))
# ##Converting float to integer
# a=458.987
# f=int(a)
# print(f)
# ##Converting string to tuple
# s="This is online"
# v=tuple(s)
# print(v)
# ##Converting string to list
# s="This is online"
# l=list(s)
# print(l)
# ##Customisation of output
# a=120
# print(a)
# print("value of a is:",a)
# print(a,"value of a is:",a)
# ##Input function
# # a=input("Enter a number")
# # print(a)
# # print("Enter a number")
# # a=input()
# # print(a)
# # print(type(a))## Input function will always be a string
# ##Task1
# # a=int(input("Enter value of a"))
# # b=int(input("Enter value of b"))
# # c=a+b
# # print("The sum is:",c)
# x=10
# y=20
# s=x+y
# print("adding",x,"and",y,"the result is",s)
# print("adding {} and {} the result is {}".format(x,y,s))
# print("adding {2} and {0} the result is {1}".format(y,s,x))##By mentioning the position or indexing
# print("adding {0} and {1} the result is {2}".format(x,y,s))
# print("adding {0} and {1} the result is {s}".format(x,y,s=x+y))
# x=12.565656
# print("The value of x is %.4f"%x)
# print("hello {name},{greetings}".format(greetings="GM",name="Bibin"))
# ##ADD operation of string datatype and int datatype
# a=10
# b=20
# s=a+b
# print(s)
# a="hello"
# b="world"
# s=a+b
# print(s)
# ##DIVISION
# a=25
# b=5
# s=a/b
# print(s)
# ##Multiplication
# a=15
# b=2
# print(a%b)
# print(a/b)
# print(a//b)##used to round off the output value to the nearest whole number
# print(a*b)
# print(a**b)
# ##Comparison Operators(<,>,==,<=,>=,!=)
# # a=2
# # b=4
# # print(a>b)
# # print(a<b)
# # print(a>=b)
# # print(a>=b)
# # print(a==b)
# # print(a!=b)
# a=True
# b=True
# print(a and b)
# a=2
# b=4
# print(a!=b and a<=b)
# a=False
# b=True
# print(a or b)
# a=2
# b=4
# print(a>=b or a<=b)
# a=False
# print(not a)
# ##Bitwise operator
# a=13
# b=60
# c=a & b
# print(c)
# c=a | b
# print(c)
# ##Assignment operator
# a=50
# a+=10
# print(a)
# a=250
# a-=50
# print(a)
# a=250
# a/=50
# print(a)
# a=250
# a%=50
# print(a)
##IDENTITY OPERATORS (is and isnot)
# x1=5
# y1=10
# print(x1 is y1)
# print(x1 is not y1)

# x3=[1,2,3]
# y3=[1,2,3]
# print(x3 is y3) ##Even though the elements of list are same but the memory allocation is diff, hence identities are diff
# print(x3==y3) ##Since the elements are same, the comparison will be equal
# print(x3 is not y3)

##Membership operators (in & not in)
# x="Hello World"
# print("W" in x)
# print('wd' in x)
# print('y' in x)
# print('y' not in x)
# print('Wo' in x)

##Control flow statements
##Python If statement
##Executes next command if the condition is true

# i=int(input("Enter a number"))
# if i>=0:
#     print("positive number")
#     print("..........")
# print("I am not in if")## Command executes irrespective of the satisfaction of condition since it is outside the loop

# i=-9
# if i>=0:
#     print('positive number')
# else:
#     print("it is a negative number")
# print("its outside")

# a=int(input('Enter a number'))
# i=a%2
# if i==0:
#     print("even number")
# else:
#     print("The number is odd")

# i=-9
# if i==0:
#     print("it is zero")
# elif i>0:
#     print("It is positive")
# else:
#     print("It is negative")

##Checking
# a= int(input("Enter first number"))
# print(a)
# b= int(input("Enter 2nd number"))
# print(b)
# c= int(input("Enter 3rd number"))
# print(c)
# if (a>b) and (a>c):
#     print("Largest number is:",a)
# elif (b>c) and (b>a):
#     print("Largest number is:",b)
# else:
#     print("Largest number is:",c)

##Nested if
# i=int(input("Enter a number"))
# if i>=0:
#     if i==0:
#         print("it is zero")
#     else:
#         print("it is a positive number")
# else:
#     print("Its a neg number")

##WHILE LOOP (used for iteration)

##Sum of first n terms
# n= int(input("Enter a number: "))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
#     print(i)
# print("sum:",sum)

##Prime number using while loop

# n= int(input("Enter a number: "))
# isdivisible= False
# i=2
# while i<n:
#     if n % i == 0:
#         isdivisible= True
#         print(i)
#     i += 1
#     # print(i)
# if isdivisible:
#     print("Not a Prime number")
# else:
#     print("Is a prime number")

##Find all numbers div by 5 or 7 under 100
# i=1
# while i<100:
#     if (i%5==0) or (i%7==0):
#         print(i)
#     i += 1

##Finding sum of numbers in GP with common ratio r=3 from 2 to n
# n=int(input("Enter number of terms: "))
# sum=0
# i=2
# print(i)
# while i<=(n-1)**3:
#     i *= 3
#     sum=sum+i
#     print(i)
# print("SUM:",sum+2)

##Finding sum of numbers in GP with common ratio r=5 from 2 to n
# n = int(input("Enter number of terms: "))
# sum = 0
# i = 2
# print(i)
# while i <= 5**(n-1):
#     i *= 5
#     sum = sum+i
#     print(i)
# print("SUM:", sum+2)

##Finding sum of numbers in GP with common ratio r=7 from 4 to n
# n = int(input("Enter number of terms: "))
# sum = 0
# i=4
# print(i)
# while i <= 7**(n-1):
#     # print(i)
#     i *= 7
#     sum = sum+i
#     print(i)
# print("SUM:", sum+4)

##Finding sum of numbers in GP with common ratio r from a to n terms
# a = int(input("Enter the first term: "))
# n = int(input("Enter number of terms: "))
# r = int(input("Enter the common ratio: "))
# s = 0
# i = a
# print(i)
# if r < a:
#     while i <= r**n:
#         i *= r
#         s = s+i
#         print(i)
# else:
#     while i <= r**(n-1):
#         i *= r
#         s = s+i
#         print(i)
#
# print("SUM OF THE GP is:", s+a)

##FOR LOOP
# L= [1,2,"PYTHON",4,5]
# for i in L:
#     print(i)
#     print("*"*10)
# print("it is outside")

#####String slicing using character position
# a="hello world"
# print(a[4])
# print(a[1:4])
# print(a[1:8:2]) ##[starting pos : Ending pos : Step size]
# print(a[::2])
# print(a[0:6:1])
# print(a[0:len(a):2])
# print(a[-1])
# print(a[-3:-1])
# print(a[::-1]) ## Character reversing
# ##Deleting the string
#
# ##Concatenation (adding the strings)
# b=" world"
# a=a+b
# print(a)
# ##Iteration
# for i in b:
#     print(i)
# ##Membership operator(Output of membership operator will be true or false)
# print("l" in "hello")
# print('hl' in "hello")
# ##lower case and upper case
# print("HELLO".lower())
# print("heLLo".upper())
# ##Split (Output will always be list)
# print("Hello world".split())##Space is a default splitter
# print("Hello,world".split(","))
# print("Hello/World".split("/"))
# ##Join
# print("".join(["hey","morning"]))##join without space
# print(" ".join(["hey","morning"]))##join with space
# print(",".join(["hey","morning"]))
####REVERSING
# a="ernakulam"
# print(reversed(a))##only shows the memory allocation of the reversed string
# s=list(reversed(a))
# print(s)
##or
# s=print(a[::-1])
##Sort
# a=["zbc","acs","dfg"]
# b=sorted(a)
# print(b)
# print(a)
# a.sort()
# print(a)
##find(Finds the position of a string in a string by identifying the position of its 1st char
# print("how are you".find('ow'))
# print("how are you".find('are'))
# ##REPLACE (replaces an existing string)
# print("how are you".replace('how','where'))
# ##Capitalize (makes the first character of a string uppercase and the remaining lower)
# print("welcome to experTz Lab".capitalize())
# ##CENTER (Makes the string to the center)
# print("welcome to experTz Lab".center(50,"*"))
# ##Counts the number of the defined character in the string
# a="Welcome to Expertz Lab"
# print(a.count("o"))
# print(a.count("om"))
# ##Starts with and ends with
# print(a.startswith("W"))
# print(a.startswith("w"))
# print(a.endswith("b"))
# ##INDEX(finds position)
# print(a.index("c"))
# ##print words in alphabetical order
# a="Hi world how are you"
# b=a.lower()
# c=b.split()
# print(c)
# d=sorted(c)
# print(d)
# for i in d:
#     print(i)
#
# ## STRIP (removes white space or mentioned cahr from both side(left start and right end))
# a=" Hi world how are you"
# print(a)
# print(len(a))
# s=a.strip()
# print(len(s))
# print(s)
# f=a.strip("u")
# print(f)
# ##lstrip and rstrip (removes white space or mentioned char from left side)
# a="uHi world how are you"
# s=a.lstrip("u")
# print(s)
# a="uHi world how are youuuu"
# s=a.rstrip("u")
# print(s)


####
# a = [1,"python",[2,'4']]
# # a += [2]
# # print(a)
# a.extend([2,3])
# print(a)
# a.append('5')
# print(a)

## Creating a list
# A = [] ##Empty list
# print(A)
# print(type(A))
# S = "kfghui sdn"
# l = list(S)
# print(l)
# print(len(l))
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(L[0])
# print(L[:]) ##Output = Entire list
# print(L[4])
# print(L[:5])
# print(L[2:5])
# print(L[2:10:2])
# print(L[::2])##Start to End of a list with stepsize 2
# print(L[0::2])
# print(L[0:len(L):2])
# L = [1, 2, 3, 4, [4, 9, 6]] ##List in a list
# print(L[4])
# print(L[4][0])
# print(L[-1][0])##-1 represents the last pos of list L
# print(L[-1][-1])
#
# ##List Concatenation
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# K = ["one", "two"]
# L = L+K
# new = K+L
# print(L)
# print(new)
#
# ##Assign Value to an Index
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# L[6] = "five"
# print(L)
#
# ##Append
# L.append("Five")
# print(L)
#
# ##Insert
# L.insert(3, "three")
# print(L)
# print(L.index(2))##Checking the position of character 2 in the list L
#
# # del L
# # print(L)
#
# # L.remove(2)## remove used for deleting an element by identifying the element itself
# # print(L)
#
# # del L[1]## del used for deleting an element from a list by identifying the position of element
# # print(L)
#
# ##POP method ##Deletes an element from a list and returns element at the index pos mentioned in the command to a variable
# # a = L.pop(4)
# # print(L)
# # print(a)
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # a = L.pop(4)
# # print(L)
# # print(a)
# b=["a", "b", "c"]
# L.extend(b)
# print(L) ## Extends the list L by extracting the elements from list b
# L.append(b)
# print(L) ## Extends the list L by the list b
#
# ## Count: Counts the number of mentioned element in a list
# L = [1, 2, 3, 4, 2, 5, 6, 7, 2, 8, 9]
# print(L.count(2))
#
# ##Clear : Clears the element of a list and return as an empty list
# L.clear()
# print(L)
#
# ##Slicing and copying
# L = [1, 2, 3, 4, 2, 5, 6, 7, 2, 8, 9]
# s = L.copy()
# k = L
# s = L[2:5].copy()
# print(s)
# print(k)
#
# ##Membership operators
# L = [1, 2, 3, 'three', 4, 5, 6, 'five', 8, 9, 'Five']
# if "three" in L:
#     print("it is there in the list")
# if 10 not in L:
#     print("empty")
#
# ########
# s = [1, 5, 6, 8, 9, 2, 0]
# s.sort()
# print(s)
#
# #####
# v = sorted(s, reverse=True)
# print(v)
# print(s)
#
# ##### Iteration of list
# # for i in s:
# #     print(i)
#
# ############ squaring the elements of a list
# t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s = []
# for i in t:
#     s.append(i**2)
# print(s)
#######
L = [-10, -20, 10, 20, -15, 30]
s = []
for i in L:
    if i > 0:
        s.append(i)
print(s)
######
L = [45, 8, 6, 89, 7, 15, 35, 100]
for i in L:
    if i is max(L):
        print(i)

######
L = ["xyz", "aba", "abcd", "1231", "sdhbks"]
s = 0
for i in L:
    if i[0] == i[-1]:
        s += 1
print(s)
####deleting the duplicate elements#####
L = [10, 20, 30, 20, 10, 50, 10]
s = []
for i in L:
    if i not in s:
        s.append(i)
    # print(s)
print(s)

#####Aggregate fns:
L = [1, 2, 3, 4, 5, 6, 17, 18.5]
print(max(L))
print(min(L))
print(sum(L))

#####Nested list
L = [[1,2,3],[4,8,9],[8,5]]
print(L[1])

#### List Comprehension #######
sqrs = []
for i in range(5):
    sqrs.append(i**2)
print(sqrs)
#### OR #######
sqrs = [i**2 for i in range(5)]
print(sqrs)

#####pos nums from the list by using comprehensive method
L = [10,-20,9,45,-33]
L = [i for i in L if i>=0]
print(L)
L = [25, 30, 54, 85, 90]
L = [i/2 for i in L]

















