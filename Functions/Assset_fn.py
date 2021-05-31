# ASSERTION
# Assertion is a way of telling programme to test a certain condition.
# Whenever the cond is true, then only following statement executes.
# If it is false, then the programme will not execute.
# Normally used for debugging the code.

## fromat : assert<condition>; <optional msg>
# eg;
# def get_age(age):
#     assert age >= 0, "age cannot be negative"
#     print("your age is : ", age)
# get_age(-1)

#
# def avg_list(l, s = 0):
#     assert len(l) > 0, "list cannot be empty"
#     for i in l:
#         s += i
#     print(s/len(l))
# avg_list([1, 2, 3, 4])
# avg_list([])