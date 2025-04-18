from collections import Counter
from itertools import groupby
from math import log

# arr = [1,3,2,3,4,3,2,1,2,2]

# O(N**2)
# maxi = max(arr , key=lambda num: arr.count(num))
# print(maxi)

# O(n)
# d = {}$
# for num in arr:
#     d[num] = d.get(num , 0) + 1
# maxi = max(d.items() , key= lambda i : i[1])
# print(maxi[0])

# Counter
# O(n)
# print(Counter(arr).most_common()[0][0])




# BigO:
#     O(1)      -> sikl aylantirmasdan bita urunishda topsak
#     O(log(N))    -> listni yarimigacha aylanib javobni topsak
#     O(N/2)    -> listni yarimigacha aylanib javobni topsak
#     O(N)      -> 1 ta sikl aylantirib javobni topsak
# ----------------------------------
#     O(N**2)   - 1 ta element uchun yana sikl aylantirishlik
#     O(N!)     - ?
#     O(N**N)   - ?

# print(log(1000, 2))
# print(log(1000000, 2))


# d = {
#     1:2,
#     3:4,
# }
# print(d.items())


# arr = [1,3,2,3,4,3,2,1,2,2,5,7]

# count
# hash table
# Counter
# O(N+N) ~ O(N)
# d = {}
# for num in arr:
#     d[num] = d.get(num , 0) + 1
# for num in arr:
#     d[num] = d.get(num , 0) + 1
# unic_num = sorted([num for num , quantity in d.items() if quantity == 1])
# print(unic_num)


# -------------------------------------------------

arr = [2,2,2,2,2,1,3,2,3,4,3,2,1,2,2,2,5,7]
# O(n)

# counter = 0
# result = []
# for i in range(len(arr)-1):
#     if arr[i] == arr[i+1]:
#         counter += 1
#     else:
#         counter += 1
#         result.append((arr[i] , counter))
#         counter = 0
#
# print(max(result , key=lambda i : i[1]))

# O(n)
# maxi = (0,0)
# for i , massiv in groupby(arr):
#     num = i
#     quantity = len(list(massiv))
#     if quantity > maxi[1]:
#         maxi = (num , quantity)
# print(maxi)

# -------------------------------------------------

# text = "Bu yerdan eng uzun so'z topilsin"

# O(N+N+N)
# O(N**2)

# print(max(text.split(), key=len))


# -----------------------------------------------
# text = "Bu yerdan eng uzun so'z topilsin"
# maxi = ("" , 0 , -1)
# for i , word in enumerate(text.split()):
#     l_ = len(word)
#     if l_ > maxi[1]:
#         maxi = (word ,l_, i )
# print(maxi)

# -----------------------------------------------

# text = "Dasturlash juda qiziq jarayon"

# print(list(map(len, text.split())))
# O(N+N)


# O(N)
# result = []
# tmp = 0
# for char in text:
#     if  char != " ":
#         tmp += 1
#     else:
#         result.append(tmp)
#         tmp = 0
# result.append(tmp)
# print(result)




# words = ["apple" , "banana" , "apple" , "apple" , "Cherry"]

# O(N)
# d = {}
# for word in words:
#     d[word] = d.get(word,0)+1
# print(d)

# O(N)
# print(Counter(words))

# -----------------------------------------

# words = ["apple" , "banana" , "apple" , "apple" , "Cherry"]
# O(N)
# print(s_:=sorted(words, key=len) , s_[-1])

# -----------------------------------------
# O(N/2)
# text = "level"

# two pointer




# -------------------------------------

from string import ascii_lowercase

# alifbo = 'abcdefghijklmnopqrstuvwxyz'
# words = ["aaa","bob","ccc","ddd"]
# words_copy = []
# for i , word in enumerate(words):
#     diff = ord(word[0]) - ord('a')
#     tmp = ""
#     for char in word:
#         tmp += chr(ord(char) - diff)
#     words_copy.append(tmp)
#
# index = words_copy.index(min(words_copy, key=words_copy.count))
# print(words[index])







# {
#     "adc" : '3-1',
#     "wzy" : '3-1',
#     "abc" : '11',
# }

















# ----------------------------------

# s = "Hello how are you Contestant"
# k = 4
# print(" ".join(s.split()[:k]))


# s = "abcde"
# goal = "cdeab"
#
# print(len(s) == len(goal) and goal in s + s)

# sentence = "thequickbrownfoxjumpsoverthelazydog"
#
# print(len(set(sentence)) == 26)

# 1 -> 0
# 2 -> 1
# 3 -> 3
# 4 -> 6
# 5 -> 10
# 6 -> (6 * (6-1))/2
# 7 -> (7 * (7-1))/2

# ....
#
# 1 1 1 1 1 1 1

# 16 : 1...15

# words = ["aba","aabb","abcd","bac","aabc" , "aabc"]
#
# d = {}
#
# for word in words:
#     temp = "".join(sorted(set(word)))
#     d[temp] = d.get(temp , 0) + 1
#
# count = 0
# for i in (d.values()):
#     count += (i * (i-1))//2
# print(count)


# print(Counter('abbc') & Counter('abb'))

# words = ["bella","label","roller"]
# res = Counter(words[0])
#
# for word in words[1:]:
#     res &= Counter(word)
# print(list(res.elements()))


"""
Home Work:
    string     -> 5 ta 
    array      -> 2 ta
    hash table -> 2 ta
    
    Bot Ga screen shot tashisiz
"""













