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
    print('connection to db is successful')
except Exception as e:
    print('Error occured while making DB onnection: ', e)
    sys.exit()
else:
    #create tables
    def create_table():
       cursor = conn.cursor()
       try:
           cursor.execute(q.create_table)
           cursor.commit()
           cursor.close()
           print('db table created')
       except Exception as e:
           print('Error occured while creating table: ', e)
           cursor.rollback()
           cursor.close()
           conn.close()
           sys.exit()

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
            print('data inserted into db table')
        except Exception as e:
            print('Error occured while inserting data into table: ', e)
            cursor.rollback()
            cursor.close()
            conn.close()
            sys.exit()
    
    #display average revenue by state
    def display_avg_revenue():
        try:
            cursor = conn.cursor()
            cursor.execute(q.avg_revenue_by_state)
            result = cursor.fetchall()
            print('')
            print('displaying average revenue of top companies by state.')
            print('')
            print('')
            print('Headquarters, Num_Companies, Avg_Revenue, Avg_Employee')
            for row in result:
                print(str(row).replace('(','').replace(')','').replace("'",""))
            print('')
            print('')
            cursor.close()
            conn.close()                
        except Exception as e:
            print('Error displaying average revenue by state.',e)
            cursor.close()
            conn.close()
            sys.exit()
