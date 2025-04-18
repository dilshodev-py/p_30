from shutil import which


class Node:
    def __init__(self , val , next = None):
        self.val = val
        self.next = next


l = [1,89,34,65,12]
head = Node(l[0])
tmp = head
for i in l[1:]:
    tmp.next = Node(i)
    tmp = tmp.next

# node1 = Node(1)
# node2 = Node(89)
# node3 = Node(34)
# node4 = Node(65)
# node5 = Node(12)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5


# -------------- (insert)task ----------------
# pos = 4
# new_data = 100
# i = 2
# tmp = head
#
# if pos == 1:
#     new_node = Node(new_data)
#     new_node.next = head
#     head = new_node
# else:
#     while tmp:
#         if i == pos:
#             new_node = Node(new_data)
#             new_node.next = tmp.next
#             tmp.next = new_node
#         i += 1
#         tmp = tmp.next
#
#
# tmp = head
# while tmp:
#     print(tmp.val)
#     tmp = tmp.next


# class LinkedList:
#     head = Node(None)
#     def print(self):
#         tmp = self.head.next
#         while tmp:
#             print(tmp.val)
#             tmp = tmp.next
#
#
#     def append(self , val):
#         new_node = Node(val)
#         tmp = self.head
#         while tmp.next:
#             tmp = tmp.next
#         tmp.next = new_node
#
#     def insert(self , val , pos):
#         tmp = self.head
#         curr_pos = 1
#         while tmp:
#             if curr_pos == pos:
#                 new_node = Node(val)
#                 new_node.next = tmp.next
#                 tmp.next = new_node
#             curr_pos += 1
#             tmp = tmp.next
#
#     def delete(self , data):
#         tmp = self.head
#         while tmp and tmp.next:
#             if tmp.next.val == data:
#                 tmp.next = tmp.next.next
#                 break
#             tmp = tmp.next
#
#     def find(self, data):
#         tmp = self.head.next
#         pos = 1
#         while tmp:
#             if tmp.val == data:
#                 return pos
#             pos += 1
#             tmp = tmp.next
#         return -1
#
#     def delete_dublicate(self):
#         tmp1 = self.head.next
#         tmp2 = self.head.next
#         while tmp2:
#             if tmp1.val != tmp2.val:
#                 tmp1.next = tmp2
#                 tmp1 = tmp1.next
#             tmp2 = tmp2.next
#         if tmp1:
#             tmp1.next = tmp2
#
#     def marge_linked_list(self , list1 , list2):
#         pass



# l1 = LinkedList()
# l.append(1)
# l.append(1)
# l.append(1)
# l.append(2)
# l.append(2)
#
# l2= LinkedList()


# LinkedList().marge_linked_list(l1,l2)
# l.append(1)
# l.append(89)
# l.append(12)
# l.append(34)
# l.append(12)
# l.insert(100, 1)
# l.delete(12)
# print(l.find(12))
# l.delete_dublicate()
# l.print()




# Home Work:
#     array -> 2 ta
#     string -> 2 ta
#     hash table -> 2ta
#     sorting -> 1 ta
#     Linked List -> 2 ta
