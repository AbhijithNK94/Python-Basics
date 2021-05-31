# Methods are of 3 types:
# 1) INSTANCE METHOD
# 2) STATIC METHOD
# 3) CLASS METHOD

# 1) INSTANCE METHOD
# inside a method we are passing self, so it is called "instance method".


# class Student:
#     def __init__(self, name, age):
#         self.Name = name
#         self.Age = age
#
#     def display(self):
#         print("Name: ", self.Name)
#         print("Age: ", self.Age)
#
#
# s1 = Student("John", 22)
# s1.display()
##############instance method can take values from outside through arguments.


# class Student:
#     def __init__(self, name, age):
#         self.Name = name
#         self.Age = age
#
#     def dis(self, PhnNo):
#         print("Name :", self.Name)
#         print("Age :", self.Age)
#         print("Phn :", PhnNo)
#
#
# s1 = Student("John", 22)
# s1.dis(3654)

# INSTANCE method is of 2 types:
#   A) Accessor method (accessors)
#   B) Mutator method (mutators)

#   A) Accessor method


# class Student:
#     def __init__(self, name, age):
#         self.Name = name
#         self.Age = age
#
#     def get_name(self):  # This is only a conventional way of fetching. Or we can use the method above.
#         return self.Name
#
#     def get_age(self):
#         return self.Age
#
#
# s1 = Student("John", 25)
# print("Name :", s1.get_name())
# print("Age :", s1.get_age())

#   B) Mutator method

# class Student:
#     def __init__(self, name, age):
#         self.Name = name
#         self.Age = age
#
#     def dis(self):
#         print("Name :", self.Name)
#         print("Age :", self.Age)
#
#     def get_name(self):
#         return self.Name
#
#     def get_age(self):
#         return self.Age
#
#
# s1 = Student("David", 24)
# print("Name :", s1.get_name())  # Conventional method
# print("Age :", s1.get_age())
# s1.dis()  # Another method. Both will give the same output.


# 2) CLASS METHOD:

# class Student:
#     school = "Don Bosco"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def dis(self):
#         print("Name :", self.name)
#         print("Age :", self.age)
#
#     @classmethod  # to create a class method we should use this decorator
#     def schoolinfo(cls, x):
#         print("School name is :", cls.school)  # It can access class variables only and args that pass through objects are not accessible
#                                                # It cant access instance variables
#         print("Location is :", x)
#
#
# s1 = Student("David", 25)
# s2 = Student("John", 24)
#
# Student.schoolinfo("Cochin")  #class method is calling by class name
#
# ## OR ##
#
#
# class Student:
#     school = "Don Bosco"
#     location = "Cochin"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def dis(self):
#         print("Name :", self.name)
#         print("Age :", self.age)
#
#     @classmethod  # to create a class method we should use this decorator
#     def schoolinfo(cls):
#         print("School name is :", cls.school)  # It can access class variables only and args that pass through objects are not accessible
#                                                # It cant access instance variables
#         print("Location is :", cls.location)
#
#
# Student.schoolinfo()

# Class method is also called as factory method, since it can return class object
# class Student:
#     school = "DON BOSCO"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def dis(self):
#         print("Name :", self.name)
#         print("Age :", self.age)
#
#     @classmethod
#     def schoolinfo(cls):
#         x = "Dibin"
#         y = 25
#         return cls(x, y)  # Class method return class objects
#
#
# obj1 = Student("John", 22)
# obj2 = Student("Amith", 21)
# obj1.dis()
# print(obj1.name)
# print(obj2.age)
# obj3 = Student.schoolinfo()  # Returns the class object
# print(obj3.name)
# print(obj3.age)

#
# 3) STATIC METHOD (It does not use class variables as well as instance variables.)
# It can access instance and class variables indirectly.


# class Student:
#     school = "DON BOSCO"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def dis(self):
#         print("Name :", self.name)
#         print("Age :", self.age)
#
#     @staticmethod
#     def info(x):
#         print("Location is :", x)
#
#
# obj1 = Student("John", 22)
# obj2 = Student("Amith", 21)
# Student.info("cochin")  # Using static method we can assign values to the variables of included fn at the time of call.
# Student.info(obj1.name)  # It access instance variable indirectly
# Student.info(Student.school)  # It access class variable indirectly

#####
# Q) Create a class with instance variables "name and "age".
# Class should have a static method to know he is eligible for vote or not.


# class Voter_ID:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def dis(self):
#         print("Name :", self.name)
#         print("Age :", self.age)
#
#     @staticmethod
#     def eligibility(Age):
#         if Age >= 18:
#             print("Person is eligible for vote")
#         else:
#             print("Denied")
#
#
# per1 = Voter_ID("Ajith", 22)
# per1.dis()
# Voter_ID.eligibility(per1.age)
# per2 = Voter_ID("Amal", 17)
# per2.dis()
# Voter_ID.eligibility(per2.age)
# per3 = Voter_ID("Abraham", 18)
# per3.dis()
# Voter_ID.eligibility(per3.age)


############

# from datetime import date
# presentyr = date.today().year
#
#
# class Voter_ID:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def eligibility(name, age):
#         if age >= 18:
#             print(name, ": Eligible")
#         else:
#             print(name, ": Denied")
#
#     @classmethod
#     def voter_info(cls, name, year):
#         return cls(name, presentyr - year)
#
#
# p1 = Voter_ID.voter_info("Abhijith", 1994)
# p2 = Voter_ID.voter_info("Rakesh", 2007)
# p3 = Voter_ID.voter_info("Abhiraj", 2000)
# p4 = Voter_ID.voter_info("Theertha", 2000)
# p5 = Voter_ID.voter_info("Nikhisha", 2008)
# p1.eligibility(p1.name, p1.age)
# p2.eligibility(p2.name, p2.age)
# p3.eligibility(p3.name, p3.age)
# p4.eligibility(p4.name, p4.age)
# p5.eligibility(p5.name, p5.age)
