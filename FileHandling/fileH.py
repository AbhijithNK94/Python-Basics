# ################ FILE HANDLING #################

# We use input fn to input a data. But if the data is huge, it is hard to input every time.
# So we can save that data in file and use it.
# a = input("Enter a name: ")  # every time we want to input data.
# print(a)

# "w" - It is writing mode, it create a file if not exists.
# if the file exists, it truncate it ie; it modifies it.

# Opening a file in writing mode
# file = open("sample.txt", "w")  # Creating a text file by opening it in writing mode ('W')
# file.write("hi, welcome to Expertz lab")
# file.write("\nhi, welcome \nhow are you")
# file.close()  # Close an opened file always.

# Opening a file in read mode. ( Only applicable for existing file, not applicable for creating or truncating)
# file = open("sample.txt", "r")
# print(file.read())  # It prints the whole data into the comment box from the file.
# file.close()  # We cannot use the file once it is closed. If we want to use it again, then we need to open it again in
#               in read mode
# If in read mode the given file is not an existing file, then the error will occur.

# Line by line read mode of existing txt file.

# f = open("sample.txt", mode="r")
# print(f.readline())  # First line of sample.txt file will be printed
# print(f.readline())  # Second line of sample.txt file will be printed
# print(f.readline())  # Third line
# print(f.readline())  # If the read line statement used exceeded the number of lines of txt file,
# #                      then the system will neither print any new line nor it will show any error.
# print(f.readline())

# print(f.readlines())  # Will print the contents of a txt file opened to the var f as a list.

# Line by line printing of txt data by iteration.
# a = f.readlines()  # We cant assign it to another variable as the data from txt file has already been used.
# for i in a:
#     print(i)  # Iteration of the output from readlines statement will display the txt data line by line.

# print(f.readline(5))
# print(f.readline(5))
# print(f.readline(20))  # If the limit arg exceeds the number of characters in the txt file, it will pass the remaining
# #                        characters without generating error.
# print(f.readline(30))

# print(f.readline(5))
# print(f.tell())  # to know the current position of file pointer after the readline statement.
# print(f.readline(5))
# print(f.tell())
# print(f.readline(20))
# print(f.tell())  # will show the default position of pointer irrespective of the exceeded arg passed.
# #                  ie; instead of showing 20+5+5 = 30, the tell statement passes the default position 28.

# print(f.readline())
# print(f.tell())
# f.seek(0)  # redirects the file pointer from current position to the given pos (passed as  an arg). Here we set the
# file pointer pos to 0.
# print(f.readline(5))
# print(f.tell())  # Now when we call the tell statement, it will be 5 as we have set the pointer pos to 0 using seek
# #                  statement.


# Opening a file in reading and writing mode (r+ mode)
# file = open("sample.txt", "r+")  # read and write mode
# print(file.read())
# file.write("\nThis is a new beginning")
# print(file.read())  # Here when we run the program again & again, the written statement will overwrite again and again.
# file.close()

# APPEND MODE
# a - append mode, to add more data, without changing existing data
# it creates a file if it does not exists.
# f = open("sample.txt", "a")
# f.write("\nEvery end has a new beginning\n")
# f = open("sample.txt", "r")
# print(f.read())

# Q) To write data's of one file to another file line by line.

# f0 = open("sample.txt", "r")
# f1 = open("sample_new.txt", "w")
# a = f0.readlines()
# for i in a:
#     f1.write(i)
# f0.close()
# f1.close()

# Q) Create a file with string "first first line second line"
#    write a prgm to count the no of words in the file data as a dict
# f0 = open("sample_1.txt", "w")
# f0.write("first first line second line")
# f0.close()
# f0 = open("sample_1.txt", "r")
# a = f0.read().split()
# b = {"first": len([i for i in a if i == "first"]), "line": len([i for i in a if i == "line"]),
#      "second": len([i for i in a if i == "second"])}
# print(b)

# OR
# f0 = open("sample_1.txt", "w")
# f0.write("first first line second line")
# f0.close()
# f0 = open("sample_1.txt", "r")
# a = f0.read().split()
# dict = {}
# for word in a:
#     if word in dict:
#         print(word)
#         print(dict)
#         dict[word] += 1
#         print(dict)
#     else:
#         print(word)
#         print(dict)
#         dict[word] = 1
#         print(dict)
# print(dict)

# OR
# f0 = open("sample_1.txt", "w")
# f0.write("first first line second line")
# f0.close()
# f0 = open("sample_1.txt", "r")
# words = f0.read().split()
# dict = {i: words.count(i) for i in words}
# print(dict)















