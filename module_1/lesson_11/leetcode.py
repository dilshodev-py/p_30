# ================== 1047 ===================

# s = "aaca"
#
# for char in s:
#     if char+char in s:
#         s = s.replace(char+char , "")
# print(s)

# l = ["c" , "a"]
# for char in s:
#     if l and l[-1] == char:
#         l.pop()
#     else:
#         l.append(char)
# print("".join(l))

# ================== 1961 ===================

# s = "iloveleetcode"
# words = ["i","love","leetcode","apples"]
# r = ""
# print(True in [(r:= r + word)==s for word in words])
# r = ""
# for word in words:
#     r := r+ word
#     if r == s:
#         print(True)
#
# print(False)


# ============================================

# n = 4

# print("a" * n if n% 2 else "a"*(n-1) + "b")
# if n % 2:
#     print("a" * n)
# else:
#     print("a"*(n-1) + "b")

# ======================= 415 =====================

# num1 = "999"
# num2 = "1"
#
# max_len = len(max(num1 , num2 , key=len))
# num1 = num1.zfill(max_len)[::-1]
# num2 = num2.zfill(max_len)[::-1]
# result = ""
# q = 0
# for i in range(max_len):
#     sum = int(num1[i]) + int(num2[i]) + q
#     if sum > 9:
#         q = 1
#         result = str(sum)[1] + result
#     else:
#         q = 0
#         result = str(sum) + result
#
# if q:
#     print(f"{q}{result}")
# else:
#     print(result)


# ====================================

# num = "354270"
# t= ["1" , "3" , "5" , "7" , "9"]
# result = ""
# for i in range(len(num)-1 , -1 , -1):
#     if num[i] in t:
#         result = num[:i+1]
#         break
# print(result)












