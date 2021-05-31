# GENERATOR FUNCTION

# If our fn consist at least one yield keyword, then the fn is called generator fn.
# It is similar to return, but return will terminate the fn yield can preserve its state.

# 1) Without return we cannot assign the elements of this fn to another variable "a"
# def getSeries():
#     for i in range(10):
#         print("value :", i)
#         # return i
# a = getSeries()
# print(a)

# With return inside the for loop
# def getSeries():
#     for i in range(10):
#         print("value :", i)
#         return i  # return will terminate the fn
# a = getSeries()
# print(a)

# With return statement outside the for loop.
# def getSeries():
#     for i in range(10):
#         print("value :", i)
#     return i  # return will terminate the fn
# a = getSeries()
# print(a)
# But with return statement we can only assign the last iterated element to another variable, since return statement
# cannot preserve its state.

# OR we can use yield statement for running the fn without terminating and preserving the values.
# def getSeries():
#     for i in range(10):
#         yield i  # yield can preserve its state.
# a = getSeries()
# print(a)
# for k in a:
#     print(k)

# def prt():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# a = prt()
# print(next(a))  # using next statement, we can call the preserved values by yield statement one by one.
# print(next(a))
#
# # printing 10 - 19
# def integer():
#     for i in range(10, 20):
#         yield i
# a = integer()
# print(list(a))
#
# # RANDOM NUMBER:
# import random
# print(random.randint(10, 100))  # it will gen a number b/w 10 & 100.

# Q) Create 10 random numbers using gen fn.
# import random
# def random_no():
#     for i in range(10):
#         i = random.randint(10, 100)
#         yield i
# a = random_no()
# print(list(a))

# Q) 1 - 10 numbers sqrs using while.
# def sqr(limit, i=0):
#     while i < limit:
#         i += 1
#         a = i**2
#         yield a
# a = sqr(10)
# print(list(a))
