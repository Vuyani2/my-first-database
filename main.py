import mysql.connector



mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234", host="127.0.0.1", database="mydb",
                               auth_plugin="mysql_native_password")

mycursor = mydb.cursor()
xy = mycursor.execute("Select * from mytable")


for i in mycursor:
    print(i)
