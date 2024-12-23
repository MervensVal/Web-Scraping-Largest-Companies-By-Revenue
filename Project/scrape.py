from bs4 import BeautifulSoup
import requests
import pandas as pd
import secret
import datetime
import db

folder_path = secret.folder_path

def pull_revenue_data():
    try:
        #make request and pull table
        url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
        page  = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find_all('table')[0]

        #get column titles (table headers)
        world_titles = table.find_all('th')
        table_titles_list = [title.text.strip() for title in world_titles]

        #loop through table rows (tr), find td tags for each row, get inividual data text, clean text, and insert
        df = pd.DataFrame(columns = table_titles_list)
        table_rows = table.find_all('tr') 
        for row in table_rows[1:]:
            row_data = row.find_all('td')
            individual_row_data = [data.text.strip() for data in row_data]
            length = len(df)
            df.loc[length] = individual_row_data
        
        #insert dataframe into into csv file
        current_time_str = datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
        revenue_file_path = folder_path + '\\Revenue Data\\Largest_Company_Revenue'+current_time_str+'.csv'
        df.to_csv(revenue_file_path, index=False)

        #create table and insert data into SQL Server database
        db.create_table()
    except Exception as e:
        print("Error occured during data scraping to csv file: ", e)