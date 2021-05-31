##### Sets #####

# u = {} ##This is a dictionary
# print(type(u))
# u = set() #### This is a set
# print(type(u))
# a = {1,3,2,7,4,5,6,2,3}
# print(type(a))
# a = set([1,2,3]) ## type concersion from list to set
# print(type(a))
# print(a)
#
# a = {1,3,2,7,4,5,6,2,3}
# print(a) ####output of a set will be sorted and unrepeated
a = {1, 2, 3, 3, 4, 5, 5, 6, 7}
print(a)

a.add(0)
print(a)
a.add('abhi')### we can add a single elemet using add
print(a)
a.update({"anju","sivu"}) ### we can add multiple elements to a set using update
print(a)
a.update(["anu", "vivek"]) ### the update command updates the elements to a set irespective of the type of collection.
print(a)
a.discard("anu")
print(a)
a.discard("anu")## It will not show error even if the mentioned element is not there in the set
print(a)
# a.remove("anu")## It will show error message if the mentioned element is not there in the list
# print(a)
a = {1, 5, 8, 3}
print(a)
a.pop()## randomly removes an element from a set
print(a)
a.pop()
print(a)

a.clear()##Clears all the elements from a set
print(a)

### Aggregate fns
a = {1, 5, 8, 3, 4, 8, 7}
print(min(a))
print(max(a))
print(sum(a))

### Sorted fn
print(sorted(a))### gives the sorted set as an output

###Set operations###
set1 = {1, 2, 3}
set2 = {3, 4, 5}
###UNION operation
print(set1 | set2)
print(set1.union(set2))
print(set2.union(set1))
#### INTERSECTION OPRN
print(set1 & set2)
print(set1.intersection(set2))
#### Difference oprn
print(set1 - set2)
print(set1.difference(set2))
print(set2 - set1)
#### Symmetric difference ### eliminates the common element from two sets and recalls
print(set1 ^ set2)

# x = frozenset([1, 2, 3, 4, 5]) #### We cannot add or update the elements in a frozenset
# print(type(x))
# print(x)
# x.add("srr")
# print(x)