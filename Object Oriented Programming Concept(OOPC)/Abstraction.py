# ABSTRACTION :
# Python by default does not support abstract method.
# Abstract class should have at least one abstract method.

# from abc import ABC, abstractmethod
# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass
#     def dis(self):
#         print("hi")
# com = Computer()
# com.process()  # We cant create object of abstract class.
# com.dis()  # We cant create object of abstract class.

# from abc import ABC, abstractmethod
# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass
# class Laptop(Computer):
#     pass
# com1 = Laptop()
# com1.process()  # we cant create object of abstract class even after inheritance by this way.


# from abc import ABC, abstractmethod  # ABC: Abstract Base Classes.
# class Computer(ABC):
#     @abstractmethod  # Abstract class should have at least one abstract method
#     def process(self):
#         pass
# class Laptop(Computer):  # Inheriting the abstract class.
#     def process(self):  # Here we redefine the process method of abstract class Computer for creating the object.
#         print("It is running")
#
#
# com1 = Laptop()
# com1.process()
#
# class Polygon(ABC):
#     @abstractmethod
#     def nSide(self):
#         pass
#     def dis(self):
#         print("Non abstract method")
#
# class Square:
#     def nSide(self):
#         return "4 Sides"
#
# class Triangle(Polygon):
#     def nSide(self):
#         return "3 sides"
#
# obj1 = Square()
# print(obj1.nSide())
# obj2 = Triangle()
# print(obj2.nSide())
# obj3 = Polygon()
# print(obj3.nSide())

# from abc import ABC,abstractmethod
# class Polygon(ABC):
#     @abstractmethod
#     def nSide(self):
#         pass
#     def display(self):
#         print("non-abstract method")
#     @abstractmethod
#     def area(self):
#         pass
# class Square(Polygon):
#     def __init__(self,lenght):
#         self.length=lenght
#     def nSide(self):
#         return "4 sides"
#     def area(self):
#         print( "area= ",self.length**2)
#
# class Trangle(Polygon):
#     def __init__(self,b,hight):
#         self.b=b
#         self.hight=hight
#     def nSide(self):
#         return "3 sides"
#     def area(self):
#         print(0.5*self.hight*self.b)
# obj=Square(4)
# print(obj.nSide())
# obj.display()    #we can access normal fn defined inside abstrct class throuhg child class
# obj.area()
# obj1=Trangle(2,3)
# obj1.area()
# print(obj1.nSide())
#
# class X(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
#
# class Y(X):
#     def m1(self):
#         print("this is m1")
# class Z(Y):
#     def m2(self):
#         print("this is m2")
#
# # p1 = Y()
# # p1.m1()  # We cannot create an object through class Y since we havent redefined the two abstract methods of class X.
# #          ie; m1 and m2. Here in class Y only m1 is redefined.
# p2 = Z()
# p2.m1()  # We can create an object through class Z since we have inherited class Y to Z and Y have m1 redefined and
# #          Z have m2 redefined. m1 and m2 being the abstract class of X and both are redefined in class Y and Z.
# #          Hence object creation is possible.
# p2.m2()
