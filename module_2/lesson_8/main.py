from dataclasses import dataclass


# file = open("example.txt" , "r")
# matn = file.read()
# print(matn)
# file.close()

# with open("example.txt" , "r") as file:
    # matn = file.read()
    # row1 = file.readline()
    # row2 = file.readline()
    # row3 = file.readline()
    # file.seek(0)
    # row1 = file.readline()
    # print(row1)
    # print(row1, end="")
    # print(row2,end="")
    # print(row3, end="")
    # i=0
    # while row := file.readline():
    #     print(row, end="")
    # print(file.readlines())



# ------------------------------------------------

# with open('example.txt' , "r+") as f:
#     print(f.read())
#     f.write("yangi malumot")

# with open('example.txt' , "w+") as f:
#     print(f.read())
#     f.write("yangi malumot")

# with open('example.txt' , "a+") as f:
#     f.seek(0)
#     print(f.read())
#     f.write("yangi malumot")

# with open('example1.txt' , "x") as f:
#     f.write("Salom")


# numpy
# pandas

# 1 000 000   PYTHON
# 100 000 000 GO
# Azmijon Po'latov

# CPYTHON


# ============================================

# @dataclass
# class User:
#     name : str = None
#     age : int = None
#
#     def save(self):
#         with open("users.txt" , "a+") as f:
#             f.write(f"\n{self.name}|{self.age}")
#
#     def show(self):
#         with open("users.txt" ) as f:
#             for user in f.readlines():
#                 name , age = user.split('|')
#                 print(f"Ismi : {name} , Yoshi : {age}")
#
# v = "Y"
# while v != "n":
#     User(name=input("Name:") , age=int(input("Age"))).save()
#     v = input("Continue ? [Y/n]:")
#
# User().show()



# ======================================

# @dataclass()
# class Region:
#     name : str = None
#
#     def save(self):
#         # read
#         with open("regions.txt" , "a") as f:
#             f.write(f"{self.name}\n")
#
#     def show_sorted(self):
#         with open("regions.txt") as f:
#             print("Alifbo tartibida shaharlar : ",sorted(f.readlines()))
#
# v = "Y"
# while v != "n":
#     Region(name=input("Name:")).save()
#     v = input("Continue ? [Y/n]:")
#
# Region().show_sorted()


# ================================================













