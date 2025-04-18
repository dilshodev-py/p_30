import time


# def plus_one(number): # 1
#     def add_one(number): # 3
#         return number + 1 # 5
#     result = add_one(number) # 4 , 6
#     return result # 7
#
#
# print(plus_one(4)) # 2 , 8


# def plus_one(number): # 1
#     return number + 1 # 6
#
# def function_call(function): # 2
#     number_to_add = 5 # 4
#     return function(number_to_add) # 5,7
#
# print(function_call(plus_one)) # 3,8


# def hello_function(): # 1
#     def say_hi(): # 3
#         return "Hi" # 7
#     return say_hi # 4
#
# hello = hello_function() # 2 , 5
# print(hello()) # 6 , 8



# ========================

# def uppercase_decorator(function):
#     def wrapper(name):
#         func = function(name)
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
#
# @uppercase_decorator
# def say_hi(name):
#     return f"Hello {name}"
#
# print(say_hi("Tom"))


# decorator = uppercase_decorator(say_hi) # 3 , 6
# print(decorator()) # 7 , 13


# -----------------------------------

# def time_decorator(function):
#     def wrapper(*args , **kwargs):
#         start = time.time()
#         result = function(*args , **kwargs)
#         end = time.time()
#         print(f"Duration : {end-start}")
#         return result
#     return wrapper


# @time_decorator
# def add(num1,num2):
#     time.sleep(3)
#     return num1+ num2
#
#
# print(add(1, 2))


# users = [
#     {
#         "username" : "Tom",
#         "role" : "ADMIN"
#     },
#     {
#         "username" : "Jerry",
#         "role" : "USER"
#     },
# ]
# def is_admin(function):
#     def wrapper(*args , **kwargs):
#         user_name = kwargs.get("admin_username")
#         for user in users:
#             if user.get("username") == user_name:
#                 if user.get("role") == "ADMIN":
#                     del kwargs['admin_username']
#                     return function(*args , **kwargs)
#                 else:
#                     return "Sizda bu funksiyani ishlatishga huquq yuq"
#         return f"{user_name} Bunday username li account yuq"
#     return wrapper
#
# @is_admin
# def create_user(username , role):
#     new_user = {
#         "name": username ,
#         "role" : role
#     }
#     users.append(new_user)
#     return "Success create user !"
#
# @is_admin
# def sum(num1 , num2):
#     return num1 + num2
#
#
# print(sum(1,2, admin_username='Jerry'))



# def save_results(fun):
#     results = []
#     def wrapper(*args, **kwargs):
#         if not args and not kwargs:
#             return results
#
#         res = fun(*args, **kwargs)
#         results.append(res)
#         return res
#
#     return wrapper
#
# @save_results
# def add_nums(*nums):
#     return sum(nums)
#
# print(add_nums(2,3,4,55,66,6,7))
# print(add_nums(2,3,4,55,66,6,7))
# print(add_nums(2,3,4,55,66,6,7))
# print(add_nums(2,3,4,55,66,6,7))
#
# print(add_nums())

# def power(power_number):
#     def inner(function):
#         def wrapper(*args , **kwargs):
#             result = function(*args , **kwargs)
#             return result**power_number
#         return wrapper
#     return inner

# @power(2)
# def multiple(num1 , num2):
#     return num1 * num2


# print(multiple(3, 2))

# def add_numbers(*numbers):
#     def inner(function):
#         def wrapper(*args , **kwargs):
#             result = function(*args , **kwargs)
#             return result+sum(numbers)
#         return wrapper
#     return inner
#
# @add_numbers(1,1)
# def multiple(num1 , num2):
#     return num1 * num2
#
# print(multiple(3, 4))

