import json
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from openpyxl import load_workbook
import datetime
import re
 
database = MySQLdb.connect(
                host="localhost",
                user="root",
                passwd="Database@2020",
                db="testdb",
                port=3306
            )
cursor = database.cursor()

with open('log.txt') as f:

    for line in f:

        line=line.replace("[", "")

        line=line.replace("]", "")

        splits=line.split()

        insert_query = f"INSERT INTO tbl_logs (service_name,log_date,status_code) VALUES ('{splits[0]}','{splits[3]}','{splits[5]}');" 

        cursor.execute(insert_query)

        database.commit()

cursor.close()
database.close()


