create_table = '''
/*CREATE DATABASE TopCompanyRevenue*/

IF(EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'TopCompany'))
    BEGIN
        PRINT('TABLE ALREADY EXISTS. RECREATING TABLE.')
        DROP TABLE TopCompany

        CREATE TABLE TopCompany(
        TopCompanyID INT IDENTITY(1000,1) PRIMARY KEY NOT NULL,
        Rank SMALLINT NOT NULL,
        Name NVARCHAR(100),
        Industry NVARCHAR(100),
        Revenue_USD BIGINT ,
        Revenue_Growth_Percentage FLOAT(2),
        Employee_Count INT,
        Headquarters_City NVARCHAR(100),
        Headquarters_State NVARCHAR(100),
        Headquarters_Country NVARCHAR(100)
        )
    END
    ELSE
        CREATE TABLE TopCompany(
        TopCompanyID INT IDENTITY(1000,1) PRIMARY KEY NOT NULL,
        Rank SMALLINT NOT NULL,
        Name NVARCHAR(100),
        Industry NVARCHAR(100),
        Revenue_USD BIGINT ,
        Revenue_Growth_Percentage FLOAT(2),
        Employee_Count INT,
        Headquarters_City NVARCHAR(100),
        Headquarters_State NVARCHAR(100),
        Headquarters_Country NVARCHAR(100)
        )
'''

avg_revenue_by_state = '''
  SELECT
  Headquarters_State,
  COUNT(TopCompanyID) Number_Of_Companies,
  AVG(Revenue_USD) Avg_Revenue,
  AVG(Employee_Count) Avg_Employee_Count
  FROM [TopCompanyRevenue].[dbo].[TopCompany]
  GROUP BY Headquarters_State
  ORDER BY Avg_Revenue DESC
'''