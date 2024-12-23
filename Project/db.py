import pyodbc as odbc
import queries as q
import sys 
import pandas as pd

#create connection string
DRIVER = 'SQL SERVER'
SERVER_NAME = '(local)'
DATABASE_NAME = 'TopCompanyRevenue'

connection_string = f"""
Driver={DRIVER};
Server={SERVER_NAME};
Database={DATABASE_NAME};
Trusted_Connections=yes;
"""

#make connection to database
try:
    conn = odbc.connect(connection_string)
except Exception as e:
    print('Error occured while making DB onnection: ', e)
else:
    #create tables
    def create_table():
       cursor = conn.cursor()
       try:
           cursor.execute(q.create_table)
           cursor.commit()
           cursor.close()
       except Exception as e:
           print('Error occured while creating table: ', e)
           cursor.rollback()
           cursor.close()
           conn.close()
    
    #insert data in db
    def insert_data(df:pd.DataFrame):
        try:
            cursor = conn.cursor()
            for index,row in df.iterrows():
                cursor.execute(
                    "INSERT INTO TopCompany VALUES (?,?,?,?,?,?,?,?,?)",
                    row['Rank'], 
                    row['Name'], 
                    row['Industry'], 
                    int(str(row['Revenue (USD millions)']).replace(',',''))*1000000, 
                    float(str(row['Revenue growth']).replace('%','')), 
                    int(str(row['Employees'].replace(',',''))), 
                    str(row['Headquarters']).split(',')[0],
                    str(row['Headquarters']).split(',')[1],
                    'United States'
                )
            cursor.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print('Error occured while inserting data into table: ', e)
            cursor.rollback()
            cursor.close()
            conn.close()