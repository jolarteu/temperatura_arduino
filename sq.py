import sqlite3
from datetime import datetime
import time

def insert_data(table, value):

    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()
        # sqlite_insert_query = """INSERT INTO temp
        #                           (value, time)
        #                            VALUES
        #                           (1,"""+str(datetime.now())+")"

        sqlite_insert_query ="""INSERT INTO """+table+"""
                                  (value, time)
                                   VALUES
                                      ("""+str(value)+',"'+str(datetime.now())+'")'


        print(sqlite_insert_query)

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully", cursor.rowcount)
        cursor.close()

    except Exception as e:
        print(e)

# 
# if __name__=='__main__':
#     while True:
#         main("temp",1)
#         time.sleep(10)
