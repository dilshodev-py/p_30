# from itertools import groupby


# l = ["abd" , "abc" , "ab"]
# for val , massiv in groupby(l , len):
#     print(val ,list(massiv) )

# list(chain([[12,34] , [1,2,3]]))
# [12,34,1,2,3]


# def custom_groupby(iterable , key=None):
#     if not key:
#         groups = []
#         for i in range(1, len(iterable)):
#             if iterable[i-1] == iterable[i]:
#                 groups.append(iterable[i-1])
#             else:
#                 yield iterable[i-1] , groups
#                 groups.clear()
#         if groups:
#             yield key(iterable[-1]) , groups
#
#     else:
#         groups = []
#         for i in range(1, len(iterable)):
#             if key(iterable[i - 1]) == key(iterable[i]):
#                 groups.append(iterable[i - 1])
#             else:
#                 groups.append(iterable[i-1])
#                 yield key(iterable[i - 1]), groups
#                 groups.clear()
#         else:
#             groups.append(iterable[-1])
#
#         if groups:
#             yield key(iterable[-1]), groups
#
#
# l = ["abc" , "123" , "123" , "ab", "12"]
# for i in custom_groupby(l , len):
#     print(i)




