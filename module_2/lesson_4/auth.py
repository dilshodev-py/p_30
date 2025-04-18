
# class Car:
#     def __init__(self , name , model , email):
#         self.__name = name
#         self._model = model
#         self.email = email
#
#     def get_name(self): # getter
#         # condition
#         return self.__name
#
#     def set_name(self , new_val): # setter
#         self.__name = new_val


# SOLID
# KISS
# DRY

# c1  = Car("S5" , "BMW"  , "e@gmail.com")
# print(c1.get_name())
# c1.set_name("S6")
# print(c1.get_name())


# ===============================================

# class CreditCard:
#     def __init__(self , credit):
#         self.__credit = credit
#         self.__current_credit = credit
#         self.__pay_amount = 0
#
#     def get_credit(self):
#         return self.__credit
#
#     def add_credit(self , new_credit):
#         if new_credit < 0 or new_credit > 50000:
#             print("Max amount 50000! Min amount 0 !")
#         else:
#             self.__credit += new_credit
#             self.__current_credit += new_credit
#
#     def pay_credit(self, pay_sum):
#         if pay_sum < 0:
#             print("Bad request!")
#         else:
#             if self.__current_credit - pay_sum < 0:
#                 print("Ko'p pul o'tkazma qilish mumkin emas !")
#             else:
#                 self.__current_credit -= pay_sum
#                 self.__pay_amount += pay_sum
random_name = "Botir"









