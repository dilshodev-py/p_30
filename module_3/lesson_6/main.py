import time
from asyncio import QueueEmpty, QueueFull
from collections import Counter, deque
from itertools import count
from queue import Queue

#
# with open('solved.txt') as f:
#     code = f.read()
#
# exec(compile(code , "" , "exec"))
#
# nums = [1,2,3,1]
# if Solution().containsDuplicate(nums) == True:
#     print("Solved + | [1,2,3,1] -> True")
# else:
#     print("Incorrect - | [1,2,3,1] -> output :False output: True ")

# banned = [1,6,5]
# n = 5
# maxSum = 6
# summa = 0
# count = 0
#
# for i in set(range(1, n + 1)).difference(banned):
#     if summa + i > maxSum:
#         print(count)
#         break
#     summa += i
#     count += 1


# players = [4,7,9]
# trainers = [8,2,5,8]
# players.sort()
# trainers.sort()
# p_l = len(players)
# t_l = len(trainers)
# i = j = count = 0
# while p_l > i and t_l > j:
#     if players[i] <= trainers[j]:
#         count += 1
#         i += 1
#     j += 1
# print(count)

# changed = [2,1,3,4,6,8]
#
# l = len(changed)
# if l % 2 == 1:
#     print([])
# else:
#     r = []
#     for i in changed:
#         if i % 2 == 0:
#             r.append(i//2)
#     print(r)


"""
1 0.5
2 1
3 1.5
4 2
6 3
8 4
"""

"""
Home Work:
    string -> 2 ta 
    array -> 2 ta 
    sotring -> 2 ta 
    hash table -> 2 ta 
    linked list -> 1 ta 
"""

# class A:
#     __slots__ = ('a' , 'b')
#     def __init__(self , a  , b , u):
#         self.a = a
#         self.b = b


# print(A(1, 2))


# def function(a, b ,/ ,*,k ):
#     print(a , b)
#
#
# function(1,2 , k=90)


# parallel(async) +
# ketma-ket(sync)

# l = [1,2,3]
#
# l.remove(1)
# # O(n)
# l.append(10)
# # O(n)
#
# l.extend({1,2,3})
# # O(n)
#
# l.insert(3,78)
# O(n)

# d = deque()
# d.append(10)
# d.append(11)
# d.append(12)
# d.append(13)
# d.append(14)
# d.remove(10)
# print(d[1])













"""
collection:
    default collection :
        set
        list 
        dict
        str 
        tuple
    
    advanced collection:
        deque
        Stack
        Queue
        LinkedList
        Binary Tree
        Graph
        
Data structure (o'zini ishlash hususiyatiga ega):
    Stack 
    Queue (navbat)
"""



# class Stack:
#
#     massiv = deque()
#     l = 0
#
#     def empty(self):
#         return self.l == 0
#
#     def size(self):
#         return self.l
#
#     def top(self):
#         if not self.empty():
#             return self.massiv[-1]
#         return -1
#     def push(self , data):
#         self.l += 1
#         self.massiv.append(data)
#
#     def pop(self):
#         if not self.empty():
#             self.l -= 1
#             return self.massiv.pop()
#         return -1
#
#     def __str__(self):
#         return self.top()
#
#
#
# class Queue:
#     def __init__(self , maxsize=None):
#         self.maxsize = maxsize
#         self.massiv = deque()
#         self.len = 0
#
#     def empty(self):
#         return self.len == 0
#
#     def full(self):
#         if self.maxsize == None:
#             return False
#         return self.len == self.maxsize
#     def get(self):
#         while self.empty():
#             time.sleep(1)
#         self.len -= 1
#         return self.massiv.popleft()
#
#     def get_nowait(self):
#         if not self.empty():
#             self.len -= 1
#             return self.massiv.popleft()
#         raise QueueEmpty
#
#     def put(self , item):
#         while self.len == self.maxsize:
#             time.sleep(1)
#         self.massiv.append(item)
#         self.len += 1
#
#     def put_nowait(self , item):
#         if self.len == self.maxsize:
#             raise QueueFull
#         self.massiv.append(item)
#         self.len += 1
#
#     def qsize(self):
#         return self.len








# https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=stack
# s = "([{}])"
# d = {
#     "(" : ")",
#     "{" : "}",
#     "[" : "]",
# }
#
# stack = Stack()
# for char in s:
#     if char in d.values():
#         if not stack.empty() and d[stack.top()] == char:
#             stack.pop()
#             continue
#         else:
#             print(False)
#             break
#     stack.push(char)
# print(stack.empty())



# for _ in range(len(s)//2):
#     s = s.replace("{}" , '').replace('()','').replace('[]','')
#
# print(not s)

# d = deque()
# d.popleft()

# students = [1,1,1,0,0,1] # max: rotate 2
# sandwiches = [1,0,0,0,1,1]




# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.top())
# print(s.empty())
# print(s.size())


# a = "{}()[]"


# d = deque()
# d.popleft()

# students = [1,1,0,0]
# sandwiches = [0,1,0,1]
# students = deque(students)
# sandwiches = deque(sandwiches)
#
# while sandwiches and sandwiches[0] in students:
#     if students[0] == sandwiches[0]:
#         students.popleft()
#         sandwiches.popleft()
#     else:
#         students.append(students.popleft())
#
# print(len(students))



# q = Queue(maxsize=5)
# q.put(10)
# q.put(10)
# q.put(10)
# q.put(10)
# q.put(10)
# q.shutdown(True)
# print(q.empty())





# Stack -> FILO
# Queue -> FIFO
# deque -> FILO , FIFO

"""
Home Work:
    array -> 1 ta 
    string -> 1 ta 
    linked list -> 1 ta 
    stack  -> 1 ta 
    queue -> 1 ta 
    sorted -> 1 ta 
"""









