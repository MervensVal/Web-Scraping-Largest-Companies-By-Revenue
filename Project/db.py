import pyodbc as odbc
import queries as q

DRIVER = 'SQL SERVER'
SERVER_NAME = '(local)'
DATABASE_NAME = 'TopCompanyRevenue'

connection_string = f"""
Driver={DRIVER};
Server={SERVER_NAME};
Database={DATABASE_NAME};
Trusted_Connections=yes;
"""

def create_table():
    try:
        conn = odbc.connect(connection_string)
    except Exception as e:
        print('Error occured while making DB onnection: ', e)
    else:
        cursor = conn.cursor()
        try:
            cursor.execute(q.create_table)
            cursor.commit()
        except Exception as e:
            print('Error occured while creating table: ', e)
            cursor.rollback()