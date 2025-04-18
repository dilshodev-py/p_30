from functools import reduce
from itertools import combinations

# students = {
#     "Ali": {"math": 85, "english": 78, "science": 92 , "fizika" : 80 },
#     "Vali": {"math": 88, "english": 90, "science": 85},
#     "Hasan": {"math": 92, "english": 75, "science": 89},
#     "Husan": {"math": 80, "english": 85, "science": 91}
# }
#
# subjects = set()
#
# for data in students.values():
#     subjects.update(data.keys())
#
# for subject in subjects:
#     print(subject , max(students.items() , key=lambda x : x[1].get(subject,0))[0])

#
#
# data = {
#     "user": {
#         "name": "Ali",
#         "details": {
#             "age": 25,
#             "address": {
#                 "city": "Tashkent",
#                 "zip": "100000"
#             }
#         }
#     }
# }
#
# result = {}
# nested_dict = True
# join_key = ""
# while nested_dict:
#     nested_dict = False
#     for key , val in data.items():
#         if isinstance(val , dict):
#             join_key += f"_{key}"
#             join_key = join_key.strip("_")
#             nested_dict = True
#             data = val
#         else:
#             r = join_key + f"_{key}"
#             r = r.strip("_")
#             result[r] = val
# print(result)
# l = [23,45,32,34]
#
# result = list(map(lambda c : (c * 9/5) + 32  , l))
# print(result)


# nums = [-1, 0, 1, 2, -1, -4]
# result = set()
# for i in list(combinations(nums, 3)):
#     if sum(i) == 0:
#         result.add(tuple(sorted(i)))
# print(result)

# [[0,0,0] , []]

# nums = [-1, 0, 1, 2, -1, -4]
# res=[]
# j=1
# keeper=0
# for i in range(len(nums)):
#     for num in nums[keeper+1+j:]:
#         if num+nums[keeper]+nums[j]==0:
#             res.append([num,nums[keeper],nums[j]])
#     j+=1
#     if j>len(nums)-2:
#         keeper+=1
#         i=keeper
#         j=i
#         j+=1
# print(res)




