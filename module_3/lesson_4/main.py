from collections import Counter
from itertools import groupby, chain

# pattern = "aba"
# s = "cat cat cat dog"
# s_split=  s.split()
# tmp = []
# if len(pattern) != len(s.split()):
#     print(False)
# else:
#     j = 0
#     for i in range(len(pattern)):
#         pattern.replace(pattern[i], str(j))
#         s.replace(s_split[i],str(i))

# grid = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# k = 2
# chain_ = list(chain(*grid))
# k_ = k % len(chain_) # 2
# rotate = chain_[-k_:]+chain_[:-k_]
# matrix = []
# for i in range(0, len(rotate), len(grid[0])):
#     matrix.append(rotate[i:i+len(grid[0])])
# print(matrix)


# grid = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# l = len(grid[0])
# print(l)
# k = 1
# matrix = list(chain(*grid))
# k_ = k % len(matrix)
# rotate = matrix[-k_:] + matrix[:-k_]
# print([rotate[i:i + l] for i in range(0, len(rotate), l)])






# nums = [0,3,2,1,3,2]

# d  ={}
# result = []
#
# for i in nums:
#     d[i] = d.get(i , 0) +1
#     if d[i] == 2:
#         result.append(i)
# print(result)

# for key , count in d.items():
#     if count == 2:
#         result.append(key)
# print(result)


# s = "YazaAay"
# find = []
# tmp = []
# for i in range(len(s)-1):
#     slice = s[i:i+2]
#     print(slice)


# print({3,4,5,6}.union({1,2,3,4,5}).union({4,5,6,7}))
# print({1,2,3}.union({5,6,7,8}))


# nums = [[3,6],[1,5],[4,7]]
# result = set()
# [result.update(set((range(row[0] , row[1] + 1)))) for row in nums]
# print(len(result))

# s = "df1afd"
#
# temp = set()
# for i in s:
#     if i.isdigit():
#         temp.add(int(i))
# if len(temp)>1:
#     print(sorted(temp)[-2])
# else:
#     print(-1)



# aliceSizes = [1,2]
# bobSizes = [2,3]
# 8 // 2 = 4

# aliceSizes = [2]
# bobSizes = [1,3]
# 6 // 2 = 3
# bobSizes[1] = 2

# [2,3]


# aliceSizes = [2]
# bobSizes = [3,1]
# alice_sum = sum(aliceSizes)
# summa = sum(bobSizes) + alice_sum
# balance = summa // 2
# bobSizes = set(bobSizes)
# for i in aliceSizes:
#     temp = balance - (alice_sum - i)
#     if temp in bobSizes:
#         print([i , temp])
#         break


# nums1 = [1,2,3]
# nums2 = [2,4]
#
# inter = set(nums1).intersection(nums2)
# print(min(inter) if inter else -1)




# paths = [["B","C"],["A","B"],["C","D"]]
#
# start = {i[0] for i in paths}
# finish = {i[1] for i in paths}
# print({finish.difference(start)}.pop())
#
#
# finish = {"C" , "B" , "D"}
# start = {"B" , "A" , "C"}
# list(dict.items())[]

# a = list(chain(*paths))
# for i in a:
#     if a.count(i) == 1 and a.index(i) % 2 != 0:
#         print(i)

# O(N**2*2)


# docker exec -t pg pg_dump -U postgres -d exam -F t -f /tmp/db_backup.tar
# docker cp pg:/tmp/db_backup.tar /Users/user/Desktop/module4_exam/v3/db_backup.tar








