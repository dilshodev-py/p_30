import time
from dataclasses import dataclass


# print("Hello world!")
# print(10 / 0)



# =======================

# start = time.time()
#
# try:
    # num = int(input("Son kiriting:"))
#     print(f"Son kvadrati : {20/0}")
# except (ValueError , ZeroDivisionError) as error :
#     print("Iltimos son kiring" , error)
# finally:
#     print("Dastur yakunlandi !")
#
# end = time.time()
# print(end - start)

# try:
#     raise Exception("xatolik")
# except Exception as message:
#     print(message)

# ================================================
# from dataclasses import dataclass
#
# @dataclass
# class User:
#     name : str = None
#     age : str = None
#
#     def is_valid(self):
#         assert self.name , "Ismni to'liq kiriting !"
#         assert self.age.strip("-").isdigit() and int(self.age) > 0 , "Yosh manfiy kiritilmasin"
#         assert self.age.isdigit() ,"Yoshni raqamlarda kiriting"
#
# class UI:
#     def main(self):
#         try:
#             user = {
#                 "name" : input("Ism:"),
#                 "age" : input("Yosh:"),
#             }
#             user = User(**user)
#             user.is_valid()
#             print("Success valid")
#         except AssertionError as message:
#             print(message)
#             self.main()
#
# UI().main()
# print(int("-10"))



# =================================================

# try:
#     assert 1 == 1 , "Teng emas"
# except AssertionError as message:
#     print(message)
# else:
#     print("Teng")

# =================================================


# date = input("[YYYY-mm-dd]:")
#
# try:
#     assert len(date.strip('-').split("-")) == 3 , "Format xatto"
#     year , month , day = date.split("-")
#     assert year , "Yil kiritilmagan"
#     assert month , "Oy kiritilmagan"
#     assert day , "Kun kiritilmagan"
#     print("Valid !")
# except AssertionError as message:
#     print(message)




