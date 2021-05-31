## Creating a list
# A = [] ##Empty list
# print(A)
# print(type(A))
# S = "kfghui sdn"
# l = list(S)
# print(l)
# print(len(l))
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(L[0])
# print(L[:]) ##Output = Entire list
# print(L[4])
# print(L[:5])
# print(L[2:5])
# print(L[2:10:2])
# print(L[::2])##Start to End of a list with stepsize 2
# print(L[0::2])
# print(L[0:len(L):2])
# L = [1, 2, 3, 4, [4, 9, 6]] ##List in a list
# print(L[4])
# print(L[4][0])
# print(L[-1][0])##-1 represents the last pos of list L
# print(L[-1][-1])
#
# ##List Concatenation
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# K = ["one", "two"]
# L = L+K
# new = K+L
# print(L)
# print(new)
#
# ##Assign Value to an Index
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# L[6] = "five"
# print(L)
#
# ##Append
# L.append("Five")
# print(L)
#
# ##Insert
# L.insert(3, "three")
# print(L)
# print(L.index(2))##Checking the position of character 2 in the list L
#
# # del L
# # print(L)
#
# # L.remove(2)## remove used for deleting an element by identifying the element itself
# # print(L)
#
# # del L[1]## del used for deleting an element from a list by identifying the position of element
# # print(L)
#
# ##POP method ##Deletes an element from a list and returns element at the index pos mentioned in the command to a variable
# # a = L.pop(4)
# # print(L)
# # print(a)
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # a = L.pop(4)
# # print(L)
# # print(a)
# b=["a", "b", "c"]
# L.extend(b)
# print(L) ## Extends the list L by extracting the elements from list b
# L.append(b)
# print(L) ## Extends the list L by the list b
#
# ## Count: Counts the number of mentioned element in a list
# L = [1, 2, 3, 4, 2, 5, 6, 7, 2, 8, 9]
# print(L.count(2))
#
# ##Clear : Clears the element of a list and return as an empty list
# L.clear()
# print(L)
#
# ##Slicing and copying
# L = [1, 2, 3, 4, 2, 5, 6, 7, 2, 8, 9]
# s = L.copy()
# k = L
# s = L[2:5].copy()
# print(s)
# print(k)
#
# ##Membership operators
# L = [1, 2, 3, 'three', 4, 5, 6, 'five', 8, 9, 'Five']
# if "three" in L:
#     print("it is there in the list")
# if 10 not in L:
#     print("empty")
#
# ########
# s = [1, 5, 6, 8, 9, 2, 0]
# s.sort()
# print(s)
#
# #####
# v = sorted(s, reverse=True)
# print(v)
# print(s)
#
# ##### Iteration of list
# # for i in s:
# #     print(i)
#
# ############ squaring the elements of a list
# t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s = []
# for i in t:
#     s.append(i**2)
# print(s)
#######
# L = [-10, -20, 10, 20, -15, 30]
# s = []
# for i in L:
#     if i > 0:
#         s.append(i)
# print(s)
# ######
# L = [45, 8, 6, 89, 7, 15, 35, 100]
# for i in L:
#     if i is max(L):
#         print(i)
#
# ######
# L = ["xyz", "aba", "abcd", "1231", "sdhbks"]
# s = 0
# for i in L:
#     if i[0] == i[-1]:
#         s += 1
# print(s)
# ####deleting the duplicate elements#####
# L = [10, 20, 30, 20, 10, 50, 10]
# s = []
# for i in L:
#     if i not in s:
#         s.append(i)
#     # print(s)
# print(s)
#
# #####Aggregate fns:
# L = [1, 2, 3, 4, 5, 6, 17, 18.5]
# print(max(L))
# print(min(L))
# print(sum(L))
#
# #####Nested list
# L = [[1,2,3],[4,8,9],[8,5]]
# print(L[1])
#
# #### List Comprehension #######
# sqrs = []
# for i in range(5):
#     sqrs.append(i**2)
# print(sqrs)
# #### OR #######
# sqrs = [i**2 for i in range(5)]
# print(sqrs)
#
# #####pos nums from the list by using comprehensive method
# L = [10,-20,9,45,-33]
# L = [i for i in L if i>=0]
# print(L)
#
# ### Finding Transpose of a matrix
# m = [[1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]]
# s = []
# for i in range(4): ###Since length is 4
#     lst = []
#     for row in m:
#         lst.append(row[i])
#     s.append(lst)
# print(s)
###### Practice of finding transpose of a matrix
# L = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12]]
# s = []
# for i in range(4):
#     lst = []
#     for j in lst: #### Creates 4 lists in a list
#         lst.append(j[i])
#         # print(l)
#     s.append(l)
# print(s)
# for i in range(4):
#     lst = []
#     for j in L: #### Creates 4 lists in a list and iterates the elements of L
#         lst.append(j[i])
#         # print(lst)
#     s.append(lst)
# print(s)