"""In this program we will learn how to create Database, Tables in the DB, insert elements to the Table, Table
updating and all the operations performed in the mysql using Pycharm mysql-connector module."""

"""Importing the mysql-connector module"""
# import mysql.connector as m
#
# """Creating a fn to get the connection to the mysql in localhost"""
# def getConnection():
#     connection = m.connect(host="localhost", user="root", password="root")
#     return connection
#
#
"""Creating a fn for viewing all existing databases in mysql"""
# def show_DB():
#     con = getConnection()
#     db_cursor = con.cursor()
#     db_cursor.execute("SHOW DATABASES")
#     for db in db_cursor:
#         print(db)
# # show_DB()
#
#
"""Fn for creating Database in the mysql server of localhost"""
# def createDB():
#     con = getConnection()
#     cursor = con.cursor()
#     cursor.execute("CREATE DATABASE mypyDB")
#     con.commit()
#     cursor.close()
#     con.close()
# # createDB()
#
"""Fn for getting access to the database inside the mysql for DB modifications (creating, deleting table)"""
# def getConnection_toDB():
#     connection_DB = m.connect(host="localhost", user="root", password="root", database="mypyDB")
#     return connection_DB
#
#
"""Fn for creating a table in the database that we have created ie; mypyDB"""
# def createTable():
#     con = getConnection_toDB()
#     cursor = con.cursor()
#     cursor.execute("CREATE TABLE table1 (id INT PRIMARY KEY, name VARCHAR(30), reg_no INT, dept VARCHAR(30), "
#                    "total_marks INT)")
#     con.commit()
#     cursor.close()
#     con.close()
# # createTable()
#
#
"""Fn for inserting elements to the table ie; table1"""
# # VALUES: id, name, reg_no, dept, total_marks
# def insertElements(id, name, reg_no, dept, total_marks):
#     con = getConnection_toDB()
#     cursor = con.cursor()
#     cursor.execute("INSERT INTO table1 VALUES (%s, %s, %s, %s, %s)", (id, name, reg_no, dept, total_marks))
#     con.commit()
#     cursor.close()
#     con.close()
# # insertElements(1, "Abhijith", 72014001, "ENGG", 480)
# # insertElements(2, "Abirami", 72014002, "HR", 465)
# # insertElements(3, "Anjali", 72014003, "FIN", 491)
# # insertElements(4, "Sivani", 72014004, "MED", 475)
#
#
"""Fn for fetching the datas from the table of a DB"""
# def data_mine():
#     con = getConnection_toDB()
#     cursor = con.cursor()
#     cursor.execute("SELECT total_marks FROM table1")
#     res = cursor.fetchall()
#     con.commit()
#     cursor.close()
#     con.close()
#     return res
# data_table1 = data_mine()
#
# def create_per_table():
#     con = getConnection_toDB()
#     cursor = con.cursor()
#     cursor.execute("CREATE TABLE per_table (id INT, percentage FLOAT)")
#     con.commit()
#     cursor.close()
#     con.close()
# # create_per_table()
#
# def insert_to_per_tab(id, per):
#     con = getConnection_toDB()
#     cursor = con.cursor()
#     cursor.execute("INSERT INTO per_table VALUES (%s, %s)", (id, per))
#     con.commit()
#     cursor.close()
#     con.close()
# # per_tab = [[i for i in range(1, 5)], [i[0]/5 for i in data_table1]]
# # for i in range(4):
# #     insert_to_per_tab(per_tab[0][i], per_tab[1][i])
#
# def join_tables():
#     con = getConnection_toDB()
#     cursor = con.cursor()
#     cursor.execute("CREATE  TABLE new_tab (SELECT * FROM table1 JOIN per_table USING (id))")
#     con.commit()
#     cursor.close()
#     con.close()
# # join_tables()
#
# def fetch_max_marks():
#     con = getConnection_toDB()
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM new_tab")
#     res = cursor.fetchall()
#     con.commit()
#     cursor.close()
#     con.close()
#     def max_marks():
#         for i in range(len(res)):
#             yield(res[i][5], res[i][1])
#     m = max_marks()
#     l = list(max(m))
#     print(l[1], "got the max marks with", l[0], "percentage.")
# # fetch_max_marks()
#
# def delete(id):
#     con = getConnection_toDB()
#     cursor = con.cursor()
#     cursor.execute("DELETE from new_tab where id=(%s)", (id,))
#     """here the argument id for delete(id) fn is passed in the form of tuple (id=(%s))
#     Hence we need to pass it as a single element."""
#     con.commit()
#     cursor.close()
#     con.close()
# # delete(3)
#
#
"""In this fn we will update the element of a column in mysql using an identifier from the tableie; id in this table"""
#
# def getConnection_toDB2():
#     connection_DB2 = m.connect(host="localhost", user="root", password="root", database="idndetails")
#     return connection_DB2
#
# def update_name(name, emp_id):
#     con = getConnection_toDB2()
#     cursor = con.cursor()
#     cursor.execute("UPDATE emp SET name=(%s) where emp_id=(%s)", (name, emp_id))
#     con.commit()
#     cursor.close()
#     con.close()
# # update_name("Albin", 1)
#
#
"""PRACTICE PROBLEM 1 : Copying the data's from text file sample1.txt by creating a table in mysql"""
#
# def create_mytable():
#     con = getConnection_toDB()
#     cursor = con.cursor()
#     cursor.execute("CREATE TABLE mytable (id INT, email VARCHAR(20), name VARCHAR(20), salary INT, dept VARCHAR(20))")
#     con.commit()
#     cursor.close()
#     con.close()
# # create_mytable()
#
# def insert_val(id, email, name, salary, dept):
#     con = getConnection_toDB()
#     cursor = con.cursor()
#     cursor.execute("INSERT INTO mytable VALUES (%s, %s, %s, %s, %s)", (id, email, name, salary, dept))
#     con.commit()
#     cursor.close()
#     con.close()
#
# def copy_list():
#     f = open("sample1.txt", "r")
#     k = f.readlines()
#     for i in k:
#         yield(i.strip("\n").split(","))
# a = copy_list()
# lis = list(a)
# # print(lis)
# # for i in range(len(lis)):
# #     insert_val(lis[i][0], lis[i][1], lis[i][2], lis[i][3], lis[i][4])



























