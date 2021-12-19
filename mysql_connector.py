
'''
@Author: Srividya
@Date: 2021-12-17
@Title :Write a Python program for mysql connection with details
reading from .env file and perform import ,export of databases
'''

import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
db_connection = mysql.connector.connect(
  host=os.getenv("Host"),
  user=os.getenv("User"),
  passwd=os.getenv("Passwd"),
  database = "demodb"
)
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE employee1(empid INT, name VARCHAR(20),dept VARCHAR(20),phone INT,email VARCHAR(20))")
db_cursor.execute("DESCRIBE employee1")
for table in db_cursor:
	print(table)