### Function is a block of code to perform a specific task
### Its for re usability
## We can pass parameters/ arguments (it is optimal)

### Example for a user defined function ###
# def function_name():
#     """to print output"""
#     print("Hi")
# ##


# print("outside")
# function_name()
### to print docstring inside the function
# print(function_name.__doc__)
# print(len.__doc__)### The doc string in the len function
# ##
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# def add():
#     sum = a+b
#     return sum ### if return sum is not given we will get output as none for this function
#     # print(sum)
# print("output is:", add())

###
# def greetings(str, msg = "hello"): ### fn greetings## str is a variable for which we can assign any form of data
#     print(str, msg)
# greetings(1)
### Fn with no arguments
# def printt():
#     print("This is python 3.8 tutorial")
# printt()
#
# ### Fn with arguments
# def avg_number(x, y):
#     print("Av of", x, "and", y, "is:", (x+y)/2)
# print("RESULT:")
# avg_number(5, 4)

### Print the elements of a list by passing the elements of the list as an argument of a fn:
# a = [4, 8, 6, 7, 9]
# def ele(k):
#     for i in k:
#         print(i)
# ele(a)

#### return and print square of the sum of 2 and 3(user input)
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# def sqa(a, b):
#     x = (a+b)**2
#     return x
# print("The square of the sum of", a, "&", b, "is", sqa(a, b))

#### TYPE OF ARGUMENTS ###

## 1) Required arguments:-

# Position is imp, no of arguments should be same
# def avg_number(x, y):
#     print("Av of", x, "&", y, "is", (x+y)/2)
# avg_number(3,4)
#
# ## 2) Default arguments:-
# def man(name, abc, msg="good morning"): ## Here msg is the default argument, we dont need to pass the value to the arg while def the fn
#     print(abc)
#     print(msg)
#     print(name)
#     print(name, msg)
# man("Akhil", "jnf")
#
# ## 3) Keyword arguments :-## We will define the values of arguments at the time of calling the fn
# def display(a,b):
#     print(a)
#     print(b)
# display(a = 10, b = 20)
#
# ## 4) Variable length arguments (Arbitrary arguments):-
# def emp(*args): ## we can pass on infinte number of values using this arg.. The output will be in tuple
#     print("hello", args)
#     print("good morning all")
# emp("Bibin", "Krishna", "Priya")
#
# ### Q finding sum of n numbers, given to a fn during calling time.
# def num_tot(*nums):
#     s = 0
#     for i in nums:
#         s += i
#     return s
# print("The sum of numbers is", num_tot(1,2,3,4,5))
#
# ## 5) Variable length keyword args:-
# def man(**kwargs): ## infinite number of key value pairs can be called by using this fn
#     print(kwargs["msg3"])
#     print(kwargs["name"])
#     print(kwargs["msg1"])
#     print(kwargs["msg2"])
# man(name = "Jeena", msg1 = "good morning", msg2 = "have a nice day", msg3 = "Hi")
# ### All the iterations used in a dictionary is applicable for the variable length keyword args
#
# def man(**values):
#     for val in values.items():
#         print(val)
# man(name = "Jeena", msg1 = "good morning", msg2 = "have a nice day", msg3 = "Hi")
# ## Problem:
# a = int(input("Enter the first no: "))
# b = int(input("Enter the 2nd no: "))
# c = input("Enter the operator: ")
# def opr(a, b, c):
#     if c == "+":
#         s = a+b
#     else:
#         s = a-b
#     return s
# print("The result is:", opr(a,b,c))

### Example of all the type of args applied in a function
# def add(a, b):
#     return a+b
#
#
# def add1(*a):
#     sum = 0
#     for x in a:
#         sum = sum + x
#     return sum
#
#
# def add2(**a):
#     sum = 0
#     for x, y in a.items():
#         sum = sum+y
#     return sum
#
#
# def add3(x, y, *a, **b):
#     sum = 0
#     sum = sum + add(x, y)
#     print(sum)
#     sum = sum + add1(*a)
#     print(sum)
#     sum = sum + add2(**b)
#     print(sum)
#
#
# add3(10, 20, 30, 40, 55, 77, num1=10, num2=20, num3=30, num4=50)

### RECURSIVE FUNCTION ###
# Calling the same function inside a function.
# import sys
# sys.setrecursionlimit(100) ### For setting recursion limit ## The default recursion limit is 1000
# i = 0
#
#
# def greet():
#     global i
#     i += 1
#     print("hello", i)
#     greet()
#
#
# greet()
## Example of a recursive fn is finding the factorial
## 3! = 3*2*1*1
## n! = n*(n-1)!
### Finding factorial of a number
# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return(num*fact(num-1))
# num = int(input("Enter the number: "))
# print("Factorial is:", fact(num))
#
# ### if we dont set the limit ie 0 then it will go infinite recursions
# def factorial(num):
#     return(num*factorial(num-1))
# print("Factorial is:", factorial(5))

### Fibonacci series ##
## This is a fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
## The sum of tow prev cons numbers will be the number
## Creating fibonacci of a number
# def fib(num):
#     if num == 0 or num == 1:
#         return num
#     else:
#         return(fib(num-2) + fib(num-1))
# a = int(input("Enter the range: "))
# for i in range(a):
#     print(fib(i))

### PASS statement:- Used in a function for null execution ###
# months = ["jan", "feb"]
# for m in months:
#     pass
# print("it is outside")
# #
# def calc():
#     pass
# def display(number):
#     if number == 2:
#         pass
#     else:
#         print("The number is: ", number)
#
# display(2)
# display(5)
# for i in range(5):### disolays all the numbers in range5 except 2 due to pass statement in the fn display
#     display(i)


### GLOBAL VARIABLE & LOCAL VARIABLE
# x = 10 ## Global variable: will be assigned outside the function and the scope of the variable will be for the whole python page
# def test():
#     print(x)
# test()
#
# x = 10 ## Global variable
# def test():
#     x = 20 ## Local variable: will be assigned within the function and the scope of the variable will be within the function
#     print(x)
# test()
# print(x)
#
# ### Modify global
# x = 10
# def test():
#     x = x+30 ## we cant modify global variable inside directly
#     print(x)
# test()

# x = 10
# def test():
#     global x ## we should define the var x as a global x inside the function for any sort of modification
#     x = x+30
#     print(x)
# test()

##eg:

# x = 10
# y = 10
#
#
# def somefn():
#     global x ## now we can modify var x since we have assigned x as a global var inside the fn
#     x = x+10
#     print(x)
#     print(y) ## we cant modify var y since we didnt assign y as a global var inside the fn and also we cant assign 2 global var inside a fn
#              ### if we want to modify x and y simultaneously set either x as a global var and y as a local var or x as a local var and y as a global var
#
#
# somefn()
#
#
# ##
# name = "abc"
#
#
# def change():
#     global name
#     name = "Abhijith"
#     print(name)
#
#
# change()


### Function inside a function ####

## Example 1
# x = 100
# def outer():
#     print(x)
#     def inner(x = 10):
#         print("inside fn")
#         print(x)
#     inner()
# outer()
#
## Example 2
# def outer(a, b):
#     x = 100
#     print("Outer start")
#     def add(y):
#         return a+b+x+y
#     sum = add(1)
#     print("sum is ", sum)
#     print("Outer end")
# outer(10, 20)


### To modify a local variable of a fn in its inner fn use 'nonlocal'
# x = 10
# def outer():
#     x = 100
#     def inner():
#         nonlocal x
#         x = x+10
#         print(x)
#     inner()
#     print(x)
# outer()
# print(x)

##
# x = 100
# def outer():
#     x = 111
#     print(x)
#     def inner1():
#         nonlocal x
#         x = x+10
#         print(x)
#         def inner2():
#             global x
#             x = x + 10
#             print(x)
#         inner2()
#         print(x)
#     inner1()
#     print(x)
# outer()


### Q add 5 numbers to a list, if added 5 numbers, show the list is full
# s = []
# def lis():
#    for i in range(6):
#        i = int(input("Enter the numbers: "))
#        s.append(i)
#        if len(s) == 6:
#             print("Max lim exceeded")
#        else:
#             print(s)
# lis()

# ### LAMBDA FUNCTION ###
# ## Fn without a name
# ## Fn treat as an object so we can assign its value to a variable
# ## A fn is expressed as a Lambda fn when we dont need that fn for future reference
# #
# double = lambda x: x*2
# print(double(5))
# ## we can pass one or more arguments, but only one expression
# #eg
#
# add = (lambda x, y: x+y)
# print("sum =", add(2, 3))
# printMsg = lambda msg1, msg2: print("{}, {}".format(msg1, msg2))
# printMsg("Hello", "How are you ?")
#
# ## MAP FUNCTION ###
# # if we want to perform any operation on each element of a sequence, same like FOR we use MAP
#
# def add(n):
#     return n+10
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new = list(map(add, l))
# print(new)
#
# new = list(map(lambda x: x+10, l))
# print(new)
#
# new = map(lambda x: x+10, l)
# print(new)## Shows the memory allocation of the whole mapped object
# for i in new: ## if we want to print each element, we need to iterate the variable new
#     print(i)

##Q Using lambda fn multiply each element with 10.
# l = [10, 20, 30, 40]
# new = list(map(lambda x: x*10, l))
# print(new)

## FILLTER FUNCTION ###
# Its used to filter a data from a sequence based on a condition.
#Eg: using filter data sort the even numbers from list l
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def iseven(n):
#     if n % 2 == 0:
#         return n
# even = list(filter(iseven, l))
# print(even)
#
# def isodd(n):
#     if n % 2 != 0:
#         return n
# odd = list(filter(isodd, l))
# print(odd)
#
# def iseven(n):
#     if n % 2 == 0:
#         return n
# even = list(map(iseven, l)) ## if we use map instead of filter, it returns none based on the cond
# print(even)
#
# ## Using lambda fn
# even = list(filter(lambda x: x % 2 == 0, l))
# print(even)
#
# ##Q Find words starts with "h"
# words = ["hi", "hello", "how", "are", "you"]
# new = filter(lambda x: "h" in x[0], words)
# for i in new:
#     print(i)
#
# ## Q Filter the vowels in the list
#
# #Using lambda fn
# letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# vowels = ['a', 'e', 'i', 'o', 'u']
# new = list(filter(lambda x: x in vowels, letters))
# print(new)
#
# ##Using normal fn
# def vow(x):
#     if x in vowels:
#         return x
# new = list(filter(vow, letters))
# print(new)






