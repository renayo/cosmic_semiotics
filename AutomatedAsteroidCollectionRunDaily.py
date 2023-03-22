#THIS IS ALL THE CODE WHICH NEEDS TO RUN AND AFTER THAT RUN MAIN_TASK()

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from datetime import timedelta
#import numpy as np


#dataset containing 1200 names
df = pd.read_csv('names to search Fiverr A.csv')

#creating a list of all 1200 names
all_names = df['NAME'].values
#input_date = '2022-02-16'

input_date0 = date.today()-timedelta(days =1)#gives yesterday date
input_date = input_date0.isoformat()
#print(input_date)


#input_date = input('Enter the date in format yyyy-mm-dd example 2022-02-03:  ')

#Generating Urls from given list of names
def get_url(name):
    url_template = 'https://news.google.com/search?q={}'
    url = url_template.format(name)
    return url



#Scraping news title and date
def get_news(article,name):
    #title = article.h3.text
    title_date = article.div.div.time.get('datetime').split('T')[0]
#    print(title_date)
    if title_date == input_date:
        all_data = (title_date,name)
    return all_data


#Main function to run all code

main_list = []
def Main_task():
    for news_name in all_names:
        records = []
        count = 0
        url = get_url(news_name)
        response = requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        articles = soup.find_all('article','MQsxIb xTewfe R7GTQ keNKEd j7vNaf Cc0Z5d EjqUne')

        for article in articles:
            try:
                all_data = get_news(article,news_name)
                records.append(all_data)

            except:
                continue
        count = len(records)
#        print("---")
        main_list.append((news_name,count))



#CHANGE THE DATE AFTER THE NAMES COLUMN IN COLUMNS FOR WHICH DATE YOU ARE EXTRACTING THE RESULT.
 #THIS WILL CREATE DF OF 2 COL. --> NAMES, 2022-02-03

Main_task()
mynamedata = pd.DataFrame(main_list,columns= ['NAMES',input_date])
mynamedata.to_csv(input_date+'.csv')