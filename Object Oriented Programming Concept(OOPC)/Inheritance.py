##
# 1) INHERITANCE: Copying some methods and properties from one class to another. The class from which props and methods
#                 are being copied is known as parent class and the class to which props and methods are copied is known
#                 as child class.
# EXAMPLE:

# 1) Simple inheritance:
# class A:
#     def feature1(self):
#         print("feature 1 working")
#
#     def feature2(self):
#         print("feature 2 working")
#
#
# class B(A):  # INHERIT
#     def feature3(self):
#         print("feature 3 working")
#
#     def feature4(self):
#         print("feature 4 working")
#
#
# a1 = A()  # For class A only the methods defined in the class A is available.
# a1.feature1()
# a1.feature2()
#
# b1 = B()  # For class B the methods defined in class A & class B will be available, since we inherited the methods of
# #           class A to B. Here class A is known as parent/super class and class B is known as child/sub class.
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()
#
# # 2) Multilevel inheritance:
#
# class A:
#     def feature1(self):
#         print("feature 1 working")
#     def feature2(self):
#         print("feature 2 working")
# class B(A):
#     def feature3(self):
#         print("feature 3 working")
#     def feature4(self):
#         print("feature 4 working")
# class C(B):
#     def feature5(self):
#         print("feature 5 working")
#
# a1 = A()  # Only methods of class A is available for the object a1, since we havent inherited any methods from any class
# a1.feature1()
# a1.feature2()
# b1 = B()  # Methods of class A and B is available since we have inherited the methods of A to class B.
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()
# c1 = C()  # Methods of class A, B and C will be available, since we have inherited from class B and class B have
# #           inherited from A.
# c1.feature1()
# c1.feature2()
# c1.feature3()
# c1.feature4()
# c1.feature5()
#
# # 3) Multiple inheritance
#
#
# class A:
#     def feature1(self):
#         print("feature 1 working")
#
#     def feature2(self):
#         print("feature 2 working")
#
#
# class B:
#     def feature3(self):
#         print("feature 3 working")
#
#     def feature4(self):
#         print("feature 4 working")
#
#
# class C(A, B):  # C inherit both A and B.
#     def feature5(self):
#         print("feature 5 working")

###################################################
# Constructor in inheritance:


# class A:
#     def __init__(self):
#         print("in A init")
#     def feature1(self):
#         print("feature 1 working")
#     def feature2(self):
#         print("feature 2 working")
# class B(A):
#     def feature3(self):
#         print("feature 3 working")
#     def feature4(self):
#         print("feature 4 working")
# b1 = B()  # When we create an object of B, it initialize init of A, since B doesent have any init.
# #           if we have init in B, it initialize first.
# b1.feature3()


# class A:
#     def __init__(self):
#         print("in A init")
#     def feature1(self):
#         print("feature 1 working")
#     def feature2(self):
#         print("feature 2 working")
# class B(A):
#     def __init__(self):# Init of class B only executes
#         print("in B init")
#     def feature3(self):
#         print("feature 3 working")
#     def feature4(self):
#         print("feature 4 working")
#
# b1 = B()
# b1.feature3()

# If we want to run both init of class A and B:
# class A:
#     def __init__(self):
#         print("in A init")
#     def feature1(self):
#         print("feature 1 working")
#     def feature2(self):
#         print("feature 2 working")
# class B(A):
#     def __init__(self):
#         super().__init__()  # It calls the init of super class (class A) first and then the child class (class B)
#                               according to the order given in the init of class B.
#         #A().__init__()
#         print("in B init")
#     def feature3(self):
#         print("feature 3 working")
#     def feature4(self):
#         print("feature 4 working")
#
# b1 = B()
# b1.feature3()


##### init in case of multiple inheritance ################
# class A:
#     def __init__(self):
#         print("in A init")
#     def feature1(self):
#         print("feature 1 working")
#
#     def feature2(self):
#         print("feature 2 working")
#
#
# class B:
#     def __init__(self):
#         print("in B init")
#     def feature3(self):
#         print("feature 3 working")
#
#     def feature4(self):
#         print("feature 4 working")
#
#
# class C(A, B):  # C inherit both A and B.
#     def __init__(self):
#         print("in C init")
#         super().__init__()  # The init of A will only be executed, since the first position is for A. The inheritance of
#     #                         A is in the first position. It is known as MRO (Method Resolution Order)
#
#     def feature5(self):
#         print("feature 5 working")
#
#
# c1 = C()
# c1.feature5()
# print(C.mro())  # Gives the order of execution while calling the method of class C.

# MRO is applicable for methods too.
# class A:
#     def __init__(self):
#         print("in A init")
#     def feature(self):
#         print("feature A working")
# class B:
#     def __init__(self):
#         print("in B init")
#     def feature(self):
#         print("feature B working")
# class C(A, B):
#     def __init__(self):
#         super().__init__()
# c1 = C()
# c1.feature()

## OUTPUT
# in A init
# feature A working

# Example:
# class School:
#     def __init__(self, name):
#         self.name = name
#     def dis1(self):
#         print("school name is :", self.name)
# class Student(School):
#     def __init__(self, rollno, name):
#         super().__init__(name)
#         self.rollno = rollno
#     def dis2(self):
#         print(self.name, "is high school type")
#         print("Rnum is:", self.rollno)
#
# s1 = Student(14, "ABC")
# s1.dis2()

# EXAMPLE


# class Student:
#     def __init__(self, name, age, rollno):
#         self.name = name
#         self.age = age
#         self.rollno = rollno
#
#
# class Marksheet(Student):
#     def __init__(self, marks, name, age, rollno):
#         self.marks = marks
#         super().__init__(name, age, rollno)
#
#     def total_marks(self, s=0):
#         for i in self.marks:
#             s += i
#         print("Name :", self.name)
#         print("RollNo :", self.rollno)
#         print("Age :", self.age)
#         print("The total marks :", s)
#
#
# s1 = Marksheet([75, 78, 85, 98, 70], "Abhirami", 20, 12)
# s1.total_marks()
#
#
# class Student:
#     def __init__(self, name, age, rollno):
#         self.name = name
#         self.age = age
#         self.rollno = rollno
#
#     def dis1(self):
#         print("Name :", self.name)
#         print("Age :", self.age)
#         print("RollNo :", self.rollno)
#
#
# class Marksheet(Student):
#     def __init__(self, marks, name, age, rollno):
#         self.marks = marks
#         super().__init__(name, age, rollno)
#
#     def total_marks(self, s=0):
#         for i in self.marks:
#             s += i
#         self.dis1()
#         print("The total marks :", s)
#
#
# s1 = Marksheet([75, 78, 85, 98, 70], "Abhirami", 20, 12)
# s1.total_marks()

# EXAMPLE 2 : Bank account showing the current balance after deposit & withdraw by passing the dep and wdraw amount
#             through objects.
# class Account:
#     Bank_name = "ABC Bank"
#     IFSC_code = 45154
#     initbal = 10000
#
#     def dis1(self):
#         print("\nBank Name :", Account.Bank_name)
#         print("IFSC Code :", Account.IFSC_code)
#
#
# class Accountholder(Account):
#     def __init__(self, name, AccNo):
#         self.name = name
#         self.AccNo = AccNo
#
#     def deposit(self, deposit_amount):
#         Account.initbal += deposit_amount
#         self.dis1()
#         print("Acc Holder name : ", self.name)
#         print("Account NO      : ", self.AccNo)
#         print("Current balance : ", self.initbal)
#
#     def withdraw(self, withdraw_amount):
#         Account.initbal -= withdraw_amount
#         if self.initbal > 1000:
#             self.dis1()
#             print("Acc Holder name : ", self.name)
#             print("Account NO      : ", self.AccNo)
#             print("Current balance : ", self.initbal)
#         else:
#             print("\nInsufficient balance, cannot withdraw")
#             Account.initbal += withdraw_amount
#
#     def balance(self):
#         self.dis1()
#         print("Acc Holder name : ", self.name)
#         print("Account NO      : ", self.AccNo)
#         print("Current balance : ", Account.initbal)
#
#
# p1 = Accountholder("Abhijith", 123456)
# p1.deposit(1200)
# p1.withdraw(2500)
# p1.balance()
# p1.withdraw(7800)
# p1.balance()
# p1.withdraw(7000)
