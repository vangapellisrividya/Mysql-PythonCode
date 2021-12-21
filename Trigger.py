'''
@Author: Srividya
@Date: 2021-12-20
@Title:the use of triggers in mysql through python.

'''

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Triggers():
    '''
    This class is mainly for creating and deleting procedures.
    '''
    
db_connection = mysql.connector.connect(
  host=os.getenv("Host"),
  user=os.getenv("User"),
  passwd=os.getenv("Passwd"),
  database = "demodb"
)
    

def create_trigger(db_connection):
    '''
    Description:
        This is used to create a trigger when insert happens.
    '''
    cursor = db_connection.cursor();
    cursor.execute('''CREATE TRIGGER tr_inserting_name
        BEFORE INSERT ON employees
        FOR EACH ROW
        SET NEW.name = UPPER(NEW.name);''')
    
    print("Trigger created succesfully")
    cursor.execute('''INSERT INTO employees VALUES(7,"katie",30, 5000),(8,"jack",28,4552) ''')
    cursor.execute("SELECT * FROM employees")
    
    for row in cursor:
            print(f'{row}')
        

def drop_trigger(db_connection):
    '''
    Description:
        This is used to drop the trigger if exist.
    '''
    cursor = db_connection.cursor();
    cursor.execute("DROP TRIGGER IF EXISTS tr_ins_name")
    
    print("Trigger dropped succesfully")





create_trigger(db_connection)
drop_trigger()
