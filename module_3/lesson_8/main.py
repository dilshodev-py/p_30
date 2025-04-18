# =======================
# Iterable
# Iterator
# Generator
# Decorator
# Send Email

""""""
# from itertools import accumulate

"""
Iterable -> Massiv shaklidagi to'plamga iterable 
    list , tuple , set , dict , str
    
    
Iterator:
    
"""
# l = [1,2,3,4,5,6] # iterable
# for i in l: # iterator
#     print(i)
# l = [1,2,3,4,5,6]

# iterator = iter(l)
# while True:
#     try:
#         print(next(iterator))
#     except:
#         print("Finish")
#         break

# ==================================

# generator
# def generator_name():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     yield 6

# print(generator_name())
# Lazy qoidasi bilan ishlidi
# for i in generator_name():
#     print(i)



# l = range(1, 10000000)
# for i in l:
#     print(i)
"""
Generator + tomonlari:
    hotirdan samarali foydalanadi 
    va ishlash tezligi nisbatan tezroq
    
"""
# range(start ,stop , step)
#
# def my_range(*args):
#     start = 0
#     step = 1
#     if len(args) == 1:
#         stop = args[0]
#     if len(args) == 2:
#         start = args[0]
#         stop = args[1]
#     if len(args) == 3:
#         start = args[0]
#         stop = args[1]
#         step = args[2]
#
#     while start < stop:
#         yield start
#         start += step
#
#
# for i in my_range(1,10 , 2):
#     print(i)


# print(map(str, [1, 2, 3, 4]))
# print(list(map(lambda x: x ** 2, [1, 2, 3, 4])))
# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))

# print(list(map(lambda x: x ** 2 if x % 2 == 0 else x, [1, 2, 3, 4])))


# def custom_map(function , iterable):
#     for i in iterable:
#         yield function(i)
#
# print(list(custom_map(lambda x: x ** 2 if x % 2 == 0 else x, [1, 2, 3, 4])))


# def custom_filter(function , iterable):
#     for i in iterable:
#         if function(i):
#             yield i


# print(list(accumulate([1, 2, 3, 4, 5, 6])))
#
# print(list(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))



# def accumulate(iterable):
#     summa = 0
#     for item in iterable:
#         summa += item
#         yield summa
#
# for i in accumulate([1,2,3,4,5,6]):
#     print(i)

