### OBJECT ORIENTED PROGRAMMING CONCEPT###
# it is a programming style that is associated with
# the concept of Class, Objects and various other concepts
# abstraction, encapsulation, inheritance and polymorphism.
# A class is formed by using different variables and functions.
# In OOPC, we call variables as properties and functions as methods.
# A class is a compilation of many objects.
# Class is a blueprint or design of a software product.
# For example, Consider the blue print of a car (ie; design)
## It consists of some variables alias properties:-
## Color, Seating capacity, Fuel eff, Transmission, Braking system
## It consists of some functions alias methods:-
## Start, Stop, Accelerate, Move, Throttle


# OPERATIONS IN OOPC:

# 1) ABSTRACTION
#    In abstraction concept, only a certain objects will be accessible to the user
#    even though there are many internal objects in the class.

# 2) INHERITANCE
#    In inheritance concept, we can copy some props and methods from one class to another. The class from which we copy
#    is known as parent class and the class which copies is known as child class.

# 3) ENCAPSULATION
#    Creating class and objects is known as encapsulation

# 4) POLYMORPHISM
#    Same function exists in multiple forms.


# 1) ENCAPSULATION (Creating class and objects is known as encapsulation)

#    CREATING A CLASS:-

# Format :
# class <name of the class>:
#        statements - class variables  = prps
#                   - functions        = method

#####################
# class car: ## we created a class named car
#     def spec(self):
#         print("1000cc, hatchback")
# # obj_name = class_name()
# car1 = car() ## car1 is an object of class car.
# print(type(car1)) ## we check the class of object car1 by using this command
# a = 10
# print(type(a))  # a = 10 is an integer and comes under the class integer of python and will be able to execute all
#                   basic arithmetic and logical ops using an integer.
# # Calling the function of a class by its objects
# car1.spec() ## will returns the methods of the function spec inside class car
#
# ####
# class car:
#     def spec(self):
#         print("1000cc, hatchback")
# car1 = car()
# car1.colour = "red"
# car2 = car()
# car1.spec()
# print(car1.colour)
# car2.spec()

##########
# class car:
#     model = "Tata"
#     def spec(self):
#         print("1000cc, hatchback")
# car1 = car()
# car1.spec()
# print(car1.model)
# ##
# car2 = car()
# car2.spec() ## Calling the methods available in the class through object.
# print(car2.model)
#####
# class car:
#     model = "Tata"
#     def spec(self):
#         print("1000cc, hatchback")
#         print("It is a product of:", self.model) ## property can access inside method
# car1 = car() ##Object creation
# car1.spec() ##method calling
# car2 = car()
# car2.spec()
# car1.model = "BMW"
# print(car1.model)
# car1.spec()
# car2.spec()
#
# ## Q) Create a class person with a method "display" to print its properties are "name, age"
# class person:
#     age = int(input("Enter the age: "))
#     name = input("Enter the name: ")
#     def display(self):
#         print("Name:", self.name, "Age:", self.age)
# person1 = person()
# person1.age = 18
# person1.name = "Nikhil"
# person1.display()
# person2 = person()
# person2.display()
##
# class Person:
#     name = "Alen"
#     age = 20
#     def display(self):
#         place = "Cochin"
#         print("Name is:", self.name)
#         print("Age is:", self.age)
#         print("location is:", place)
# p1 = Person()
# p1.display()
####
# ## Q) Create a class student with properties rollno, name, age, marks
# we should pass the values to the properties through object
# then class should have a method to display all these along with his total mark

# class student:
#     rollno = 0
#     name = ""
#     age = 0
#     marks = []
#     def display(self):
#         print("Roll no:", self.rollno, ",", "Name:", self.name, ',',  "Age:", self.age)
#         s = 0
#         for i in self.marks:
#             s += i
#         print("Total mark is:", s)
#
# s1 = student()
# s1.name = "Sivanand"
# s1.age = 20
# s1.rollno = 22
# l = []
# for j in range(5):
#     j = int(input("Enter the marks: "))
#     l.append(j)
# print(l)
# s1.marks = l
# s1.display()

##

# class Student:
#     school = "DON BOSCO INTERNATIONAL SCHOOL"
#
#     def __init__(self, name, id):  # init method is used to pass arguments on the time of object creation
#         self.Name = name
#         self.ID = id
#
#     def get_marks(self):
#         l = list(map(int, input("Enter the marks: ").strip(",").split(",")))[:5]
#         return l
#
#     def total_marks(self):
#         print("\nSchool name: ", Student.school)
#         print("Name: ", self.Name)
#         print("Roll No: ", self.ID)
#         s = 0
#         for i in self.get_marks():
#             s += i
#         print("Total marks:", s)
#         print("Percentage:", (s/150)*100)
#
#     def get_name(self):
#         return self.Name


# s1 = Student("David", 8)
# s1.total_marks()
# s2 = Student("John", 15)
# s2.total_marks()
# s3 = Student("Immanuel", 23)
# s3.total_marks()

##
# class car:
#     wheel = 4  # This is a common property for all the objects in the class car. Hence, it is executed outside the
#                  __init__ (Instance variables) function. It is known as class variables or static variables.
#     def __init__(self):
#         self.mil = 12 ## These variables are called instance variables. The values will be diff at each instance.
#                       # Changes according to the objects.
#         self.model = "BMW"
# c1 = car()
# c2 = car()
# print(c1.mil)
# print(c1.model)

# class car:
#     wheel = 4
#     def __init__(self, x, y):
#         self.mil = x
#         self.model = y
# c1 = car(15, "Tata")
# c2 = car(22, "Suzuki")
# c2.mil = 18
# print(c1.mil, c1.model, c1.wheel)
# print(c2.mil, c2.model, c2.wheel)
# car.wheel = 6  # we can change the class variable by calling the (class_name.variable_name)
# print(car.wheel)  # class variable can be called using the class_name


# STATEMENTS IN PYTHON:

# 1) Normal statements
# 2) Critical statements

# a = 5
# b = 0  # Normal statements. There will be no error while execution.
# print(a/b)  # Critical statement (Since div by 0 is not defined) Zero div error.
# print("hi")
# # Execution stops, but the user may not understand what error it is.
# # To solve this issue, we use separate block. (Try except block)


# EXAMPLE OF TRY EXCEPT BLOCK
# a = 5
# b = 0
# try:  # try to execute the statement, error may happen.
#     print(a/b)  # When critical statement gives error, except block handle it.
# except Exception: # Except block only executes only if we have error.
#     print("You cannot divide by zero") # Its more readable than the error shown before.
# print("hi")

#
# a = 5
# b = 0
# try:
#     print(a/b)
# except Exception as e:
#     print(e)  # Prints the exception statement(Critical statement) by python.
#     print("you cannot divide by zero")
# print("hi")
#
# # FINALLY BLOCK
# # If we open a resource and perform the operations, we create a seperate block for closing the resource.
# # Example:
#
# a = 5
# b = 0
# try:
#     print("resource open")
#     print(a/b)
# except Exception as e:
#     print("you cant divide by zero :", e)
# finally:  # It works in both the cases.
#     print("resource close")

# Value error
# k = int(input("Enter a number : "))
# print(k)  # It shows value error if we give a character as input instead of an integer.

# try:
#     print("resource open")
#     a = int(input("Enter the 1st number : "))
#     b = int(input("Enter the 2nd number : "))
#     print(a / b)
# except ZeroDivisionError as e:  # This block executes when there is a zero division error
#     print("you cant divide by zero :", e)
# except Exception as e:  # On the safe side it will handle all type of errors.
#     print("something went wrong.... :", e)
# finally:  # It works in both the cases.
#     print("resource close")


# def division(x, y=100):
#     try:
#         result = y/x
#     except ZeroDivisionError as z:
#         print("Division Error")
#         print(z)
#     except ValueError as v:
#         print("Type error")
#
#
# division(0)


# def div():
#     try:
#         print("Execution started")
#         a = int(input("Enter the 1st number : "))
#         b = int(input("Enter the 2nd number : "))
#         print(a / b)
#     except ZeroDivisionError as Z:  # This block executes when there is a zero division error
#         print("you cant divide by zero :", Z)
#     except ValueError as V:
#         print("Invalid input :", V)
#     except Exception as e:  # On the safe side it will handle all type of errors.
#         print("something went wrong.... :", e)
#     else:
#         print("No exception !!!")
#     finally:  # It works in both the cases.
#         print("Finally executed")
# div()

# class AccountNumberError(Exception):  # We are inheriting this error to the class exception.
#     pass
#
#
# class NotEnoughFundError(Exception):
#     pass


# accInfo = {"111": 1000, "222": 2000}  # We created a dict which contains the account number as key and available fund as
#                                       variable.


# def call(a, m):
#     try:
#         amount = m
#         accountNumber = a
#         print("account is :", a)
#         print("amount recieved is :", m)
#         if accountNumber not in accInfo:
#             raise AccountNumberError()
#         if amount > accInfo[accountNumber]:
#             raise NotEnoughFundError()
#     except AccountNumberError:
#         print("Incorrect Account number")
#     except NotEnoughFundError:
#         print("Insufficient fund")
#     except Exception as e:
#         print(e)
#         print("Sorry, something went wrong!!!")
#     finally:
#         print("Thank you, Visit Again!!!\n")
#
#
# call("111",2000)
# call("1112", 2000)
# call("111", 200)
# call("222", 1500)
# call("2221", 500)
# call("222", 2500)

# def withdraw(accountNumber, amount):
#     if accountNumber not in accInfo:
#         raise AccountNumberError()
#     if amount > accInfo[accountNumber]:
#         raise NotEnoughFundError()
#     return amount
# def call(a, m):
#     try:
#         amountRecieved = withdraw(a, m)
#         print("Rs.", amountRecieved, "received")
#     except AccountNumberError:
#         print("Incorrect Account number")
#     except NotEnoughFundError:
#         print("Insufficient fund")
#     except Exception as e:
#         print(e)
#         print("Sorry, something went wrong!!!")
#     finally:
#         print("Thank you, Visit Again!!!\n")
#
# call("111",2000)
# call("1112", 2000)
# call("111", 200)
# call("222", 1500)
# call("2221", 500)
# call("222", 2500)

# class car:
#     __model = "Tata"  # Private variable (__ indicates for private variable)
#     color = "Red"  # Public variable
#     cc = 1000
#     def __start(self):  # Private method
#         print("Started")
#     def move(self):
#         print("moving")
#         print(self.__model)  # calling private variable.
#     def stop(self):
#         self.__start()  # calling private method
#         print("stopped")
# car1 = car()
# print(car1.color)
# car1.start()  # Private instance methods is not callable from outside the class
# car1.stop()
# print(car1.model)  # Private variables is not callable from outside the class. Scope: Inside the class

# In for loop, we iterate over elements from first to last.
# Eg:
# num = [7, 5, 8, 9]
# one way of printing the values
# print(num[0])
# print(num[1])
# print(num[2])
# print(num[3])
# # print(num[4])
# # if we give num[4], it gives an error since the max pos of list num is 4.
# # Other way of printing the elements of num is
# for i in num:
#     print(i)
# Or
# we have one more way of getting the elements.
# it = iter(num)  # iter is a function which iterates the elements of num and we name it as "it"
#                 The iterator gives only one value.
#                 To pass on the values we need to use next fn.
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))  # If we gives the next fn beyond the limit ie the length of list num, it shows error.

# Iterating using the fns iter and next.
# class Top:
#     def __iter__(self):  # It gives the object of the iterator.
#         self.num = 1
#         return self
#     def __next__(self):  # It gives the next value/object
#         if self.num <= 5:  # If we didn't mention the limit, it will run infinite number of times.
#             val = self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration  # Stops the iteration.
# values = Top()
# for i in values:
#     print(i)

# Infinite iteration:
# class Inf:
#     def __iter__(self):
#         self.num = 1
#         return self
#     def __next__(self):
#         val = self.num
#         self.num += 1
#         return val
# values = Inf()
# for i in values:
#     print(i)

# Q) Create an iterable obj with inc 2, starting and ending values

# class NumSeries:
#     def __init__(self, start, end, inc):
#         self.start = start
#         self.end = end
#         self.inc = inc
#
#     def __iter__(self):
#         self.num = self.start
#         return self
#
#     def __next__(self):
#         if self.num <= self.end:
#             val = self.num
#             self.num += self.inc
#             return val
#         else:
#             raise StopIteration
#
#
# a1 = int(input("Enter the first no : "))
# an = int(input("Enter the last no : "))
# inc = int(input("Enter the increment val : "))
# values = NumSeries(a1, an, inc)
# for i in values:
#     print(i)

# We have some built in attributes special methods for every class.

# class Student:
#     school = "ABC"
#
#     def __init__(self, name, id, age):
#         self.name = name
#         self.id = id
#         self.age = age
#
#
# s = Student("Theertha", 101, 22)
# s1 = Student("Abhijith", 102, 27)
# print(s.__doc__)
# print(s1.__doc__)
# print(s.__dict__)
# print(s1.__dict__)
# print(s.__getattribute__("name"))
# print(s.__getattribute__("id"))

# PROPERTY DECORATOR:
# class Student:
#     def __init__(self, no, name, mark):
#         self.rollno = no
#         self.name = name
#         self.mark = mark
#         self.msg = self.name + " obtained " + str(self.mark) + " marks."
#
# obj = Student(2, "Alan", 90)
# print(obj.name)
# print(obj.mark)
# print(obj.msg)
# obj.name = "anju"  # we change name to anju
# print(obj.name)
# print(obj.msg)  # But in the msg, the name change will not be reflected, since msg is an instance var.

# Hence we can create another user defined fn msg, so that the changes will be reflected.
#
# class Student:
#     def __init__(self, no, name, mark):
#         self.rollno = no
#         self.name = name
#         self.mark = mark
#     def msg(self):
#         return self.name + " obtained " + str(self.mark) + " marks."
#
# obj = Student(2, "Alan", 90)
# print(obj.name)
# print(obj.mark)
# print(obj.msg)
# obj.name = "anju"  # we change name to anju
# print(obj.name)
# print(obj.msg()) # Calling fn is a time consuming process.

# Hence we use property decorator.
# class Student:
#     def __init__(self, no, name, mark):
#         self.rollno = no
#         self.name = name
#         self.mark = mark
#
#     @property  # Property decorator
#     def msg(self):
#         return self.name + " obtained " + str(self.mark) + " marks."
#
# obj = Student(2, "Alan", 90)
# print(obj.name)
# print(obj.mark)
# print(obj.msg)
# obj.name = "anju"  # we change name to anju
# print(obj.name)
# print(obj.msg)









