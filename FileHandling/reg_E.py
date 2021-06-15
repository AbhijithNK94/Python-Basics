# REGULAR EXPRESSIONS:

# Reg Expressions are used for creating username, passwords etc..
# Reg Expressions are a sequence of char used for pattern matching.
# ie; whether the pattern is available in the sequence of char or string.
# Pattern is a char of a group of chars.

# To implement reg expression, we have a module "re".
# It is a collection of predefined fns to process/validate input text.
# ##Fns of "re" module.
# match()  : It is used to test the i/p string starts with a specific pattern or not.
# search() : To test a specified pattern is present or not in string. it return a match obj.
#          : we have diff methods to display the result.
#          : start() -starting pos of occurrence.
#          : span() - tuple of start and end pos.
#          : end() - ending pos.
#          : string() - actual string.
# findall() : to find duplicates of specified pattern in the string.(how many times as a list), else empty list.
# split() : how we can split a string using an expression.
# sub() : to replace the sub string using a pattern.
# compile() : used to create pattern obj and can be re-used.


# match(): Output will be boolean form(True or false)

# it is used to test the input string starts with a sp pattern or not
# on success, it return the match obj with its pos.
# on failure, it returns none.
import re
# line = "python is an obj oriented programming language"
# print(line)
# r1 = re.match('python', line)
# print(r1)
# r2 = re.match('is', line)
# print(r2)
# It will not consider new line
# line = "python is an object oriented programming language \nPython is interpreter"
# r1 = re.match('python', line)
# print(r1)
# r2 = re.match('Python', line)
# print(r2)
# # if the match found, we can use any condition
# if r1:
#     print("Yes we got a match from string")
# else:
#     print("No match found")
# if r2:
#     print("Yes we got a match from string")
# else:
#     print("No match found")


# findall() : Output will be a list

# It returns the chars with the repetetion number in list form
# line = "python is an object oriented programming language \npython is interpreter"
# r1 = re.findall("pyth", line)
# print(r1)
# r2 = re.findall("o", line)
# print(r2)
# r3 = re.findall("xyz", line)
# print(r3)
#
# # search() :
#
# line = "Python is an object oriented programming language \npython is interpreter"
# r1 = re.search("pyth", line)
# print(r1)
# r2 = re.search("pyth", line).end()  # displays the end pos of "pyth" of line.
# print(r2)
# r3 = re.search("pyth", line).span()  # displays the start and end pos of "pyth" of line in tuple form.
# print(r3)
# r4 = re.search("pyth", line).group()
# print(r4)

# line = "Python is an object oriented programming language"
# r1 = re.split("", line)
# print(r1)
# r2 = re.split("P", line)
# print(r2)
# r3 = re.split(" ", line, 2)  # 3rd is max split
# print(r3)
#
# # sub
# line = "python is an object oriented programming language"
# r1 = re.sub("p", "X", line)  # sub the specified char with another
# #                            re.sub("char to be removed", "char to be replaced", string obj)
# print(r1)
# r2 = re.sub("p", "X", line, 1)  # Here 1 is the max position for which sub fn should be executed.
# print(r2)

""" Metacharacters:
# ^      - cap symbol used for startswith
# $      - used for endswith
# *      - 0 or more occurrences of a pattern
# +      - 1 or more occurrences of a pattern
# ?      - 0 or 1 occurrences of a pattern
# {n}    - strictly n times of occurrences
# {n, m} - limit: min 'n' times & max 'm' times occurrence of a pattern.
# {, m}  - 0 to max
# {n,}   - at least n times or more.
"""

"""   Special sequences:
# \w  - a-z,A-Z,0-9,_   it represents
# \W  - non chara. and digits (ie for special sybls)it represents
# \d  - 0-9   it represents
# \D  - non digit it represents
# \s  - white space   it represents
# \S  - non white space chara.   it represents
# .   - any chara. except new line
"""

# regex = "^a...n$"  # It represents that the string regex should start with(^) "a" and end with($) "n"
# result = re.match(regex, "alaan")
# print(result)
#
# regex = "^a...."
# result = re.match(regex, "alaandd")  # Doesn't consider the number of chars in the string since we haven't
# #                                      ended the string.
# print(result)
#
# regex = "^(al)..."
# result = re.match(regex, "alaan")
# print(result)
#
# regex = "^(al)..."
# result = re.match(regex, "fgalaan")
# print(result)
#
# regex = "^...n$"
# result = re.match(regex, "alan")
# print(result)
#
# regex = "^...n$"
# result = re.match(regex, "baalan")
# print(result)  # Output will be none because in the regex there are only 3 positions before ending (...),
# #                but the expression given by us "baalan" have 5 chars before "n".
#
# regex = "^a\w\w\wn$"
# result = re.match(regex, "alaan")
# print(result)
#
# regex = "^a\w+n$"  # + symbolizes that \w occurs 1 or more times.
# result = re.match(regex, "alaan")
# print(result)

# regex = "^a[a-z]n$"
# result = re.match(regex, "alaan")
# print(result)
#
# regex = "\w+"
# res = re.match(regex, "alaan")
# print(res)
#
# regex = "\w\w"
# res = re.match(regex, "alaan")
# print(res)

# regex = "\w\w"
# res = re.search(regex, "alaan")
# print(res)
#
# regex = "\w\w"
# res = re.findall(regex, "alaan")
# print(res)
#
# regex = "\w\w"
# res = re.findall(regex, "alaanl")
# print(res)
#
# regex = "\w+"
# res = re.search(regex, "alaan")
# print(res)
# if res:
#     print("result obtained")

# regex = "\w{3}"
# res = re.search(regex, "aaaaa")
# print(res)
#
# regex = "\w{3}"
# res = re.findall(regex, "aaaaa")
# print(res)
#
# regex = "\w{2}"
# res = re.findall(regex, "aaaaa")
# print(res)
#
# regex = "\S"  # every char other than whitespace
# res = re.findall(regex, "akjf lknfv")
# print(res)
#
# regex = "\s"  # whitespace only
# res = re.findall(regex, "akjf lknfv")
# print(res)
#
# regex = "\S+"  # every one or more char other than whitespace, ie each word in the string
# res = re.findall(regex, "akjf lknfv")
# print(res)
#
# regex = "\S+"  # every one or more char other than whitespace, ie each word in the string
# res = re.findall(regex, "akjf")
# print(res)
#
# regex = "\S+"
# res = re.search(regex, "akjf lknfv")
# print(res)
#
# s = "Hello, There, How"
# res = re.findall("[A-Z]", s)
# print(res)
# res = re.search("[A-Z]", s)
# print(res)
# res = re.findall("[A-Z,]", s)
# print(res)
# s = "HELLO, There, How"
# res = re.findall("[A-Z]+", s)
# print(res)
# res = re.findall("[A-Z]*", s)
# print(res)
# res = re.findall("[a-zA-Z, ]+", s)  # Order is not important while giving the conditions.
# print(res)
# s = "Hello,There,How"
# res = re.findall("[a-zA-Z,]+", s)
# print(res)
#
# res = re.findall("[A-Z]?[a-z]+", s)
# print(res)
#
# s = "Hello,there,how"
# res = re.findall("[A-Z]?[a-z]+", s)
# print(res)
#
# s = "HELLO,There,How"
# res = re.findall("[A-Z]?[a-z]+", s)
# print(res)


# Q) Find phone no: from the string
s = """Its purpose is to allow the telephone number 9876543210 of a subscriber identified by name
and address 46846 to be found. The rise of the Internet 5654665 and 56545654651535 smart phones in the 21st
Century greatly reduced the need for a paper phone book"""

# res = re.findall("\s\d{10}\s", s)
# print(res)

# FLAGS:
# Only used for giving sp condition, its an optional parameter.
# s = """Readers can gain knowledge of what it was like to work in New York City in the early 1900's.
# One of the things that was especially interesting was that there were no safety laws at work.
# Also, there was a big contrast between the rich and the poor. Some
# Readers may not like this book because it is very depressing, but it is an important event in history to Remember."""
# regex = "^R"  # Consider staring of a string.
# # Flag changes the property of the regex, not the fns property.
#
# result = re.search(regex, s)
# print(result)
# result = re.search(regex, s, flags=re.MULTILINE)  # Multiline searches for each line.
# print(result)
# """search fn searches everywhere, ^ searches the starting of a line"""
#
# res = re.match(regex, s, flags=re.MULTILINE)
# print(res)
#
# res = re.findall(regex, s)
# print(res)
#
# res = re.findall(regex, s, flags=re.MULTILINE)
# print(res)
#
# s = """Readers can gain knowledge of what it was like to work in New York City in the early 1900's.
# One of the things that was especially interesting was that there were no safety laws at work.
# Also, there was a big contrast between the rich and the poor. Some
# readers may not like this book because it is very depressing, but it is an important event in history to Remember."""
#
# regex = "Read"
# res = re.findall(regex, s)
# print(res)
# res = re.findall(regex, s, flags=re.IGNORECASE)
# print(res)

# Q) Find a phone number starts with 987
# s = "9876543210 46846 5654665 9876532358 98745654651"
# res = re.search("^(987)\d{7}\s", s)
# print(res)
# res = re.findall("\d{10}\s", s)
# for i in res:
#     print("Mobile no. is: ", i)
# res = re.findall("^987\d{7}", s)
# print(res)
# res = re.findall('\s?[9][8][7]\d{7}\s', s)
# print(res)

# s = """+919446532358 +918547672358 +917012018647 +614522559159 +614567879821"""
# res = re.findall("\s?[+][9][1]\d{10}\s?", s)
# res1 = re.findall("\s?[+][6][1]\d{10}\s?", s)
# print("INDIAN USERS :")
# for i in res:
#     print(i)
# print("\nAUSTRALIAN USERS :")
# for i in res1:
#     print(i)
#
# s="9874565455 987654321056 46846 5654665 9874565465 7745654655"
# ph=s.split()
# # print(ph)
# regex='[9][8][7]\d{7}$'
#
# l=[]
# for i in ph:
#     res=re.findall(regex,i)
#     if len(res)!=0:
#         l.append(res)
# print(l)
# for j in l:
#     print(j[0])
#
# # EMAIL VALIDATION
# s = input("Enter the emailID : ")
# email = ["@gmail.com", "@yahoo.in", "@Outlook.com"]
# res = re.findall("\w+@gmail.com", s)
# res1 = re.findall("\w+@yahoo.in", s)
# res2 = re.findall("\w+@Outlook.com", s)
# if res != []:
#     print(res)
# if res1 != []:
#     print(res1)
# if res2 != []:
#     print(res2)


# class Person:
#     def __init__(self, name, age, mob_num):
#         self.name = name
#         self.age = age
#         self.mob_num = mob_num
#     def dis(self):
#         print("Name :", self.name)
#         print("Age :", self.age)
#         print("Ph.No :", self.mob_num)
# class User(Person):
#     def __init__(self, name, age, mob_num, user_name, password):
#         super().__init__(name, age, mob_num)
#         self.user_name = user_name
#         self.password = password
#
# def user1(self):
#     res = re.findall("[a-zA-Z]+", self.user_name)
#     res1 = re.findall("\w+", self.password)
#         if res != [] and res1 != []:
#             user1 = User.user1(self)
#                 Person.dis(self)
#                 print(res)
#                 print(res1)



class person:
    def __init__(self, name, age, mobile_no):
        self.name = name
        self.age = age
        self.mobile_no = mobile_no
class user(person):
    def __init__(self, name, age, mobile_no, username, password):
        super().__init__(name, age, mobile_no)
        self.username = username
        self.password = password
        print("details:", self.name, self.age, self.password, self.username, self.mobile_no)
def main():
    a = []
    print("Enter name,age,mobile number,user name and password")
    for i in range(0, 5):
        a.append(input())
    print(a)
    # regex = '[a-zA-Z]{5}'
    # regex = '[a-zA-Z]+'
    regex = '^[a-zA-Z][a-zA-Z]*[a-zA-Z]$'
    # regex = '[a-zA-Z0-9]{5,15}'
    test1 = re.match(regex, a[3])
    print(a[3])
    if test1:     # if user name is correct, check for pswd
        reg = '[\da-zA-Z]+[\da-zA-Z]$'
        test2 = re.match(reg, a[4])
        if test2:   # if passwd is correct create object
            user1 = user(a[0], a[1], a[2], a[3], a[4])
        else:
            print("password must be digits or alphabets")
    else:
        print("user name must be  alphabets")
main()

def main():
    users=[]
    a=[]
    print("Enter name,age,mobile number,user name and password")
    for i in range(0,5):
        a.append(input())
    print(a)
    regex = '^[a-zA-Z][a-zA-Z]*[a-zA-Z]$'
    test1 = re.match(regex,a[3])
    if test1:     # if user name is valid, check for pswd
        reg='[\da-zA-Z]+'
        test2 = re.match(reg, a[4])
        if test2:   # if paswd is correct create object
            user1=user(a[0],a[1],a[2],a[3],a[4])
            users.append(user1)
        else:
            print("password must be digits or alphabets")
    else:
        print("usre name must be alphabets")
    user2=user("A",12,"1234","abc","a123")
    user3=user("B",15,"558662","DCG","dm12")
    users.append(user2)
    users.append(user3)
    print(users)   #it get object in list
    k=map(lambda i:"+91"+i.mobile_no,users)#   add +91 to the mobile numbers using map
    print(k)
    for j in k:
        print(j)
main()


























