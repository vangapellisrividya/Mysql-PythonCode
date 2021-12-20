'''
@Author: Srividya
@Date: 2021-12-17
@Title :Write a Python program for mysql querys
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
print("connection established....")

def getData(db_connection):
    '''
    Description:
        This method get the data from given database
    Parameter:
        database
    Return:
        None
    '''
    try:
        print("Read")
        cursor = db_connection.cursor();
        cursor.execute("select * from student1")
        for row in cursor:
            print(f'{row}')
        db_connection.commit()
        cursor.close()

    except Exception as e:
        print(e)

def create_table(db_connection):
    '''
    Description:
        This method create the table in given database
    Parameter:
        database
    Return:
        None
    '''
    try:
        print("Read")
        cursor = db_connection.cursor();
        cursor.execute("create table student1(stud_id int primary key, stud_name varchar(100))")
        for row in cursor:
            print(f'{row}')
        cursor.execute("show tables")
        for row in cursor:
            print(f'{row}')
    
    except Exception as e:
        print(e)

def insert_data(db_connection):
    '''
    Description:
        This method insert data into the table in given database
    Parameter:
        database
    Return:
        None
    '''
    try:
        cursor = db_connection.cursor();
        cursor.execute("insert into student1(stud_id,stud_name) values(1,'Vidya'),(2,'Jhanu'),(3,'pavi')")
        cursor.execute("select * from student1")
        for row in cursor:
            print(f'{row}')
            
    except Exception as e:
        print(e)

def delete_data(db_connection):
    '''
    Description:
        This method delete the data in the table in given database
    Parameter:
        database
    Return:
        None
    '''
    try:
        cursor = db_connection.cursor();
        cursor.execute("delete from student1 where stud_id=1")
        cursor.execute("select * from student1")
        for row in cursor:
            print(f'{row}')
        print("deleted...")
        
    except Exception as e:
        print(e)

def update_data(db_connection):
    '''
    Description:
        This method update the data in the table in given database
    Parameter:
        database
    Return:
        None
    '''
    try:
        cursor = db_connection.cursor();
        cursor.execute("select * from student1")
        for row in cursor:
            print(f'{row}')

        print("After updation..")
        cursor.execute("update student1 set stud_name ='Vidya' where stud_id=2")
        cursor.execute("select * from student1")
        for row in cursor:
            print(f'{row}')
        print("updated..")

    except Exception as e:
        print(e)


if __name__=='__main__':
    getData(db_connection)
    print("###################")
    #create_table(db_connection)
    insert_data(db_connection)
    print("###################")
    delete_data(db_connection)
    print("###################")
    update_data(db_connection)