# scope:
#     local , global
from dataclasses import dataclass
from types import NoneType


# a = 10
#
# def tmp():
#     global a
#     a = 20
#
# print(a)



# class A:
#     # def __init__(self , a):
#     #     self.a  =a
#
#     def tmp(self):
#         print("a")
#
# class B:
#     # def __init__(self, b):
#     #     self.b = b
#
#     def tmp(self):
#         print("b")
#
# class C(A , B):
#     # def __init__(self, c):
#     #     self.c = c
#     # def tmp(self):
#     #     print("c")
#     pass
#
# class D(C):
#     # def __init__(self , a , b , c , additional):
#     #     A.__init__(self , a)
#     #     B.__init__(self , b)
#     #     C.__init__(self , c)
#     #     self.additional  = additional
#     pass
#
# d = D()
# print(D.mro())



# class A:
#     count = 0
#
#     @classmethod
#     def increment_count(cls):
#         cls.count += 1
#
#
# A.increment_count()
# A.increment_count()
# a1 = A()
# print(a1.count)


# class A:
#     count = 0
#     def __init__(self):
#         A.count += 1


# A.increment_count()
# A.increment_count()

# a1 = A()
# a2 = A()
# a3 = A()
# print(a1.count)
# print(a2.count)
# print(a3.count)



# a1 = A()
# print(a1.count)
# a1.count += 1
# print(a1.count)
#
# a2 = A()
# print(a2.count)




# from datetime import datetime
#
# print(datetime.fromisoformat("2025-01-13"))
# print(datetime.fromtimestamp(1736743500.827696))
# print(datetime(2025 , 1 , 13))
# print(datetime.now().timestamp())




# class User:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_list(cls , l : list[str | int]):
#         return cls(*l)
#
#     @classmethod
#     def from_str(cls, s: str):
#         return cls(*s.split(","))
#
#     @classmethod
#     def from_dict(cls, d: dict[str , int]):
#         return cls(**d)
#
# u1 = User("Botir" , 27)
# u2 = User.from_list(["Botir" , 27])
# u3 = User.from_str("Botir,27")
# u4 = User.from_dict({"name":"Botir" , "age":27})
# print(u4)



# class MyClass:
#     div = 3
#     @staticmethod
#     def add(x , y):
#         return x + y
#
#     def div_increment(self):
#         self.div += 1
#
#
# print(MyClass.add(1, 2))



# class Student:
#     all_students = []
#
#     @classmethod
#     def add_student(cls , name , age):
#         cls.all_students.append(f"{name},{age}")



# class Calculator:
#     def __init__(self , x  ,y):
#         self.x = x
#         self.y = y
#
#     @property
#     def add(self):
#         return self.x + self.y
#
#
# c = Calculator(10,20)
# print(c.add)

# ============================================

# class Product:
#     def __init__(self , name , price , quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity









# #         print(self.check)
#
#
#     @property
#     def check(self):
#         if self.price <= 0:
#             return "Xatto malumot"
#
#
# p = Product("Laptop" , 1500 , 10)
#


# ===============================

# from dataclasses import dataclass
# @dataclass
# class Point:
#     x : int
#     y : int
#
#
# p = Point(1,2)
# print(p)



# =======================================
# from dataclasses import dataclass  , field
#
# @dataclass
# class Student:
#     name : str
#     marks : list = field(default_factory=list)
#
#     def add_ball(self , score):
#         self.marks.append(score)
#
#     def average_ball(self):
#         return sum(self.marks)/len(self.marks)

# s = Student("Tom")
# print(s)


# @dataclass
# class A:
#     x : str

    # def __add__(self, other):
    #     return self.x + other.x
    #
    # def __mul__(self, other):
    #     return self.x * other.x

    # def __len__(self):
    #     return len(self.x)


# print(len(A("hello")))

