# words = ["a","aba","ababa","aa"]
# l = len(words)
# res = 0
# for i in range(l):
#     for j in range(i+1, l):
#         i_val = words[i]
#         j_val = words[j]
#         if j_val.startswith(i_val) and j_val.endswith(i_val):
#             res += 1
# print(res)
from collections import Counter
from itertools import groupby

# =========================================

# s = "ac"
# goal = "cab"
#
# sl = len(s)
# gl = len(goal)
# if sl != gl:
#     print(False)
# if s == goal and len(set(s)) != sl:
#     print(True)
#
# t_s = ""
# t_goal = ""
# for i in range(sl):
#     if s[i] != goal[i]:
#         t_s += s[i]
#         t_goal += goal[i]
#
# print(len(t_s) == 2 and t_s == t_goal[::-1])


# ========================================

# word = "poazaeuioauoiioaouuouaui"
#
# def count_vowel_combination(vowel):
#     count = 0
#     if len(set(vowel)) == 5:
#         count += len(set(vowel)) == 5
#         for i in range(1,len(vowel)-1):
#             j = set(vowel[:-i])
#             if len(set(vowel[:-i])) == 5:
#                 count += 1
#             else:
#                 break
#         return count
#     return 0
#
#
# result = 0
# i = 0
# while i < len(word):
#     if word[i] in "aioue":
#         vowel = ""
#         for char in word[i:]:
#             if char in "aioue":
#                 vowel += char
#             else:
#                 result += count_vowel_combination(vowel)
#                 vowel = ""
#         if vowel:
#             result += count_vowel_combination(vowel)
#         i += 1
#     else:
#         i += 1
# print(result)


# tmp = "aeuioauoiioaouuouaui"
# print(Counter(tmp))


# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
#
# print("".join(word1)=="".join(word2))
#
# x , y = 0 , 0
# d = {
#     "D" : -1,
#     "U" : 1,
#     "L" : -1,
#     "R" : 1
# }
moves = "UD"
#
# for move in moves:
#     if move in ('D' , 'U'):
#         x += d[move]
#     else:
#         y += d[move]
# print(not x and not y)


# count = Counter(moves)
# count['U'] == count['D'] and count['L'] == count['R']

# Home Work:
#     str - > 5 ta
#     list -> 5 ta
#     hash table -> 2 ta
#     linked list -> 0 ta














# length_s=len(s)
# if length_s!=len(goal):
#     return False
#
# if len(set(s))==length_s and s==goal:
#     return False
#
# if sorted(s)!=sorted(goal):
#     return False
# count=0
# for i in range(length_s):
#     if s[i]!=goal[i]:
#         count+=1
# if count>2:
#     return False
# return True




