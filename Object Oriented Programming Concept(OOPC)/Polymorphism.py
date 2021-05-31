
# POLYMORPHISM:
# Poly morphism is of 2 types:
# 1) Method overriding
#    In the case of inheritance, when parent method redefined by child class.
# 2) Operator overloading
#    Method overriding

# class A:
#     def test(self):
#         print("inside A")
#
# class B(A):
#     def test(self):
#         print("inside B")
# class C(A):
#     def test(self):
#         super().test()
#         print("inside C")
# class D(B, C):
#     pass
# d = D()
# d.test()
# b = B()
# b.test()
# c = C()
# c.test()

# EXAMPLE 2

# class Account:
#     def __init__(self, cId, AccNo, name):
#         self.cId = cId
#         self.AccNo = AccNo
#         self.name = name
#
#     def dis(self):
#         print("Customer ID :", self.cId)
#         print("Account No :", self.AccNo)
#         print("Name :", self.name)
#
#
# class SavingsAccount(Account):
#     def __init__(self, cId, AccNo, name, amount, intRate):
#         super().__init__(cId, AccNo, name)
#         self.amount = amount
#         self.intRate = intRate
#
#     def dis(self):  # Method over riding
#         super().dis()  # Redefining the superclass fn "display" here so called over riding
#         print("Amount :", self.amount)
#         print("Interest Rate :", self.intRate)
#
#
# c1 = SavingsAccount("111", "12345", "Anoop", 25000, 8.5)
# c1.dis()

##############################################

# 2) Operator overloading (Using same operator for diff methods)

# a = 5
# b = 6
# print(a + b)
# print(int.__add__(a, b))  # int is an inbuilt class in python and add is  a method in the class int
#
#
# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         m1 = self.m1 + other.m1  # This is what we perform internally. We overrides the internal operator.
#         m2 = self.m2 + other.m2
#         s3 = Student(m1, m2)  # We create a new object
#         return s3
#
#
# s1 = Student(10, 20)
# s2 = Student(5, 25)
# s3 = s1 + s2  #=====> student.__add__(s1, s2) this is happening inside
# print(s3.m1)
# print(s3.m2)
#
# a = 2
# b = 8
# print(int.__sub__(b, a))
# print(int.__mul__(a, b))

# class MyClass:
#     def __init__(self, m1):
#         self.m1 = m1
#
#     def __sub__(self, other):
#         m1 = 2 * self.m1 - other.m1
#         s3 = MyClass(m1)
#         return s3
#
#
# s1 = MyClass(10)
# s2 = MyClass(2)
# s3 = s1 - s2
# print(s3.m1)
#
# # EXAMPLE FOR OPERATOR OVERRIDING IN POLYMORPHISM:
# class Student:
#     def __init__(self, rno, name, marks):
#         self.rno = rno
#         self.name = name
#         self.marks = marks
#
#     def __gt__(self, other):
#         if (sum(self.marks) > sum(other.marks)):
#             return self.name + " has scored more"
#         else:
#             return other.name + " has scored more"
#
#
# s1 = Student(24, "Vijeesh", [50, 65, 85])
# s2 = Student(26, "Zakariah", [56, 60, 64])
# print(s2 < s1)
