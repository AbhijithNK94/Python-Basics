# ####String slicing using character position
# a="hello world"
# print(a[4])
# print(a[1:4])
# print(a[1:8:2]) ##[starting pos : Ending pos : Step size]
# print(a[::2])
# print(a[0:6:1])
# print(a[0:len(a):2])
# print(a[-1])
# print(a[-3:-1])
# print(a[::-1]) ## Character reversing
# ##Deleting the string
#
# ##Concatenation (adding the strings)
# b=" world"
# a=a+b
# print(a)
# ##Iteration
# for i in b:
#     print(i)
# ##Membership operator(Output of membership operator will be true or false)
# print("l" in "hello")
# print('hl' in "hello")
# ##lower case and upper case
# print("HELLO".lower())
# print("heLLo".upper())
# ##Split (Output will always be list)
# print("Hello world".split())##Space is a default splitter
# print("Hello,world".split(","))
# print("Hello/World".split("/"))
# ##Join
# print("".join(["hey","morning"]))##join without space
# print(" ".join(["hey","morning"]))##join with space
# print(",".join(["hey","morning"]))
# ###REVERSING
# a="ernakulam"
# print(reversed(a))##only shows the memory allocation of the reversed string
# s=list(reversed(a))
# print(s)
# #or
# s=print(a[::-1])
# #Sort
# a=["zbc","acs","dfg"]
# b=sorted(a)
# print(b)
# print(a)
# a.sort()
# print(a)
# #find(Finds the position of a string in a string by identifying the position of its 1st char
# print("how are you".find('ow'))
# print("how are you".find('are'))
# ##REPLACE (replaces an existing string)
# print("how are you".replace('how','where'))
# ##Capitalize (makes the first character of a string uppercase and the remaining lower)
# print("welcome to experTz Lab".capitalize())
# ##CENTER (Makes the string to the center)
# print("welcome to experTz Lab".center(50,"*"))
# ##Counts the number of the defined character in the string
# a="Welcome to Expertz Lab"
# print(a.count("o"))
# print(a.count("om"))
# ##Starts with and ends with
# print(a.startswith("W"))
# print(a.startswith("w"))
# print(a.endswith("b"))
# ##INDEX(finds position)
# print(a.index("c"))
# ##print words in alphabetical order
# a="Hi world how are you"
# b=a.lower()
# c=b.split()
# print(c)
# d=sorted(c)
# print(d)
# for i in d:
#     print(i)
#
# ## STRIP (removes white space or mentioned char from both side(left start and right end))
# a=" Hi world how are you"
# print(a)
# print(len(a))
# s=a.strip()
# print(len(s))
# print(s)
# f=a.strip("u")
# print(f)
# ##lstrip and rstrip (removes white space or mentioned char from left side)
# a="uHi world how are you"
# s=a.lstrip("u")
# print(s)
# a="uHi world how are youuuu"
# s=a.rstrip("u")
# print(s)
#
#
# ###
# a = [1,"python",[2,'4']]
# # a += [2]
# # print(a)
# a.extend([2,3])
# print(a)
# a.append('5')
# print(a)