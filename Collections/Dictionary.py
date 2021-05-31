#### DICTIONARY ##### Important

# #### Set and dictionary are represented by using {}
# s = {} ### This is an empty dictionary, not an empty set
# print(type(s))
# q = {"a": 5, "b": 1, 55: "c"} ### In  a dictionary the elements are represented in the form of (key:value) pairs
# print(q)
# w = dict([("a", 8), ("b", 3)]) ## another way of creating a dict by means of list of tuples
# print(w)
#
# ### Eventhough dictionary is not indexable, we can call an element by using the key
# q = {"a": 5, "b": 1, 55: "c"}
# print(q["a"])
# print(q[55])
# ##or
# print(q.get("a"))
# print(q.get(55))
#
# q = {"a": 5, "b": 1, 55: "c"}
# q["x"] = 45 ## genertates a new key:value pair to the dictionary q
# print(q)
# q['a'] = "boy" #### mutates an existing key "a" of dict q from 5 to "boy"
# ####
# r = q.pop("b") ### removes the key and returns the value of key to the assigned variable
# print(r)
# print(q)
# q.popitem()### pops an element from a dictionary randomly
# print(q)
# # q.clear() ###clears all the elements from the dictionary
# # print(q)
# del q["a"] ### deletes the particular element from the dict by using the assigned key
# print(q)
#
# ##### Problems on dict #### change key city to location
# S = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# # c = S.pop("city")
# # S["location"] = c
# # print(S)
# ###or
# S["location"] = S.pop("city")
# print(S)
#
# #### Creating dict by usiing dot from keys method
# s = {}.fromkeys(["maths", "chem", "eng"], 0)### keys mentioned as a list
# print(s)
# s = {}.fromkeys(("maths", "chem", "eng"), 0)### keys mentioned as a tuple
# print(s)
# s = {}.fromkeys(["maths"], 0)
# print(s)
# s = {}.fromkeys("maths", 0) ### if the key maths is not represented as a collection, .fromkeys considers each letter of the string as a key
# print(s)
# #### ITEMS #### IMP
# s = {"a": 10, "b": 20, "c": 30}
# print(s.items())
# # a = s.items()
# # print(type(a))
# print(s.keys()) ### returns the keys of dict s
# print(s.values()) ### returns the values of dict s
#
# ####UPDATE inserts multiple elements to a dict(2 or more).....
# s.update({"ann":"cs", "akhil":"mech"})
# print(s)
#
# ###dir mentions the list of attributes that we can do in a particular dict
# print(dir(s))
#
# ### Iteration in a dictionary
# ## Iteration of items/elements ### output will be in the tuple format
# d = {"a":10, "b":50, "c":40}
# for item in d.items():
#     print(item)
#
# ###Iteration of keys in a dict
# for key in d.keys():
#     print(key)
#
# ###Iteration of values in a dict
# for value in d.values():
#     print(value)
#
# ### Iteration of keys and values of a dict by recalling into two variables k and v
# for k,v in d.items():
#     print(k)
#     print(v)

####Problem####Calculate total marks
# d = {'Math': 10, "Chem": 50, "Eng": 40}
# s = 0
# for i in d.values():
#     s += i
# print("Total mark is:-", s)
#
# #### Max value
# s = []
# for i, j in d.items():
#     s.append(j)
# print("Max mark is:", max(s))
# ###OR
# max = 0
# for v in d.values():
#     if max < v:
#         max = v
# print(max)
# ##find the key value pair if the value > 2
# new = {}
# d = {"a": 1, "b": 5, "c": 0, "d": 3}
# for j,k in d.items():
#     if k > 2:
#         a = (j,k)
#         print(a)
#         new.update({a})
# print(new)
# ##OR
# for j,k in d.items():
#     if k > 2:
#         new.update({j:k})
# print(new)
# ###update the items of dict d to kc:v**2
# new = {k+'c': v**2 for k, v in d.items()}
# print(new)
#
# ###Nested dictionary###
# d = {101: {"name": "Ram", "mark": 100},
#      102: {"name": "Bibin", "mark": 99}}
#
# print(d)
# print(d[101])
# print(d[101]["name"])
# print(d[101]["mark"])

###Q chage varshas salary to 70000
# s = {
#      'emp1': {'name': 'John', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Varsha', 'salary': 6500}
# }
# for i, j in s.items():
#     for k, v in j.items():
#         if v == 'Varsha':
#             s[i]['salary'] = 70000
# print(s)

#### Find the min value
# studentinfo = {
#    "name": "anil",
#    "email": "anil@ddd.com",
#    "marks": {"sem1": 100, "sem2": 200, "sem3": 300}
# }
# s = 0
# for i, j in studentinfo.items():
#     if i == "marks":
#         for k, v in j.items():
#             s += v
#     if i == "name":
#         a = j
#         print(a)
# print(a, ":", s)
# ### OR
# l = studentinfo["marks"].values()
# print(sum(l))

####print id,name,mailid,total mark of both students
# data = {
#    "100": {
#        "name": "anil",
#        "email": "anil@ddd.com",
#        "marks": {"sem1": 100, "sem2": 200, "sem3": 300}
#             },
#    "101": {
#        "name": "binil",
#        "email": "binil@ddd.com",
#        "marks": {"sem1": 200, "sem2": 200, "sem3": 300}
#             }
# }
# for k, v in data.items():
#     a = k
#     s = 0 ### given here since the sum should be done within the nested dict
#     for k1, v1 in v.items():
#         if k1 == "name":
#             n = v1
#         elif k1 == "email":
#             e = v1
#         else:
#             for i in v1.values():
#                 s = s + i
#     print("ID", ":", a, "||", "Name", ":", n, "||", "Email ID", ":", e, "||", "Total marks", ":", s)


# for id, info in data.items() :
#    #print (id, "-" , y)
#    total_mark =0
#    for k, v in info.items ():
#        #print (k, "-", v)
#        if k == "marks":
#            #print (v)
#            for sem, mark in v.items():
#                total_mark = total_mark + mark
#
#    print(id, info["name"], info["email"], total_mark)

####
studentdata = {
    "111": {"name": "TOM",
            "email": "tom@gmail.com",
            "sem": {
                "sem1": {"sub1": 2, "sub2": 2, "sub3": 8},
                "sem2": {"sub1": 7, "sub2": 6}
            }},
    "222": {"name": "RAMU",
            "email": "ramu@gmail.com",
            "sem":  {
                "sem1": {"sub1": 8, "sub2": 2, "sub3": 9},
                "sem2": {"sub1": 7, "sub2": 6}
            }}
}
for i, j in studentdata.items():
    for k, v in j.items():
        s = 0
        if k == "sem":
            for k1, v1 in v.items():
                # print(v1)
                for k2, v2 in v1.items():
                    s += v2
    print(i, j["name"], j["email"], s)

















