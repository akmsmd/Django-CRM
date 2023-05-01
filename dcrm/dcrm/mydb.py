import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="upblues25",

)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE dcrm ")
print("All Done!")