import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://realpython.github.io/fake-jobs/")
# print(response)

sou =BeautifulSoup(response.content,"html.parser")
# print(sou)

names=sou.find_all(class_="title is-5")
# print(names)
name_list=[]
for name in names:
    result=name.get_text(strip=True)
    name_list.append(result)
print(name_list)

companies=sou.find_all(class_="subtitle is-6 company")
# print(companies)
company_list=[]
for company in companies:
    result1=company.get_text(strip=True)
    company_list.append(result1)
print(company_list)

locations=sou.find_all(class_="location")
location_list=[]
for location in locations:
    result2=location.get_text(strip=True)
    location_list.append(result2)
print(location_list)

df=pd.DataFrame()
# print(df)
df["Job Title"]=name_list
df["Company"]=company_list
df["Location"]=location_list
df.to_csv("Fake_jobs.csv")


