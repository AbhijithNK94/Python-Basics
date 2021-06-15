import mysql.connector as m
def getConnection():
    # Creating a connection
    connection = m.connect(host="localhost", user="root", password="root", database="idndetails")
    return connection

# Creating table
def createTable():
    con = getConnection()
    cursor = con.cursor()  # Cursor is a control structure tht enables traversal over the records in a db.
    cursor.execute("CREATE TABLE employee (id INT PRIMARY KEY, email VARCHAR(30), name VARCHAR(20), salary INT, "
                   "dept VARCHAR(20))")
    con.commit()
    cursor.close()
    con.close()
createTable()