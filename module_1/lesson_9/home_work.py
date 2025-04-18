# print({1, 1.0, "string", (5, 3, 7)})


# array = {
#     (1,2,3,4),
#     (64,3,7,5),
#     4,
#     6,
#     7
# }

# [print(sum(item)/len(item)) for item in array if isinstance(item , tuple)]
# tmp = []
# for item in array:
#     if isinstance(item , tuple):
#         tmp.extend(item)
# print(sum(tmp)/len(tmp))


# ============================================

# fruits = {"apple" , "orange" , "banana" , "cherry" , "limon" , "mandarin"}
# new_set = set()
# for _ in range(5):
#     new_set.add(fruits.pop())
# print(new_set)


# =============================================

# tmp1 = {7,3,9,43,134,6,4,2,5}
# tmp2 = {34,2211,4,5,2,5,7,5,43,2}
# print(tmp1 & tmp2)
# print(tmp1.intersection(tmp2))

# tmp = set(range(1,51))
# new_set = {i for i in tmp if i % 2 == 0}
# print(new_set)

# /////////////////////////////////////
# from math import prod
# array = {
#     (1,2,3),
#     (1,2),
#     (1,2,3,4)
# }
#
# new_set = sorted(array , key=lambda x : prod(x))
# print(new_set)

# t = (
#     (1,2,3,4),
#     (1,2,3,5),
#     (1,2,3,6),
#     (1,2,3,7),
#     "hello",
# )

# print(tuple(item for array in t for item in array if isinstance(array, tuple)))
# nums=(1,2,3,4,5,6,2,"sal","asl","da")
# new_tuple=()
# for i in nums:
#     new_tuple+=(i,)
# print(new_tuple)

# lugat = {
#     "kalit1" : "value1",
#     "kalit2" : "value2"
# }

# lugat = dict(kalit1= "qiymat1" , kalit2 = "qiymat1")
# print(lugat)


# print(lugat)

random_name = "Doniyor"



