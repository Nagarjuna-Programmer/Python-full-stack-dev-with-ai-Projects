import numpy as np
import pandas as pd
data=pd.read_csv("richest.csv",delimiter=';')
data
data.info()
data.head()
data.tail()
print(data.columns.tolist())
data.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'],axis='columns',inplace=True)


data
data.head()
data.isnull().sum()
data.dropna(axis=0,inplace=True)
data.isnull().sum()
data['Country'].values
data['Country'].unique()
data=data.replace('Viet Nam','veitnam')
data['Country'].unique()
data
data.columns
data=data.replace(['\$',""],"",regex=True)
data

data['Total Net Worth']=data['Total Net Worth'].replace("B"," ",regex=True)
data
data["Total Net Worth"]=pd.to_numeric(data["Total Net Worth"],errors="coerce")
data["Total Net Worth"].dtype
def value_to_float(x):
    if x is None:
        return None

    if isinstance(x, str):
        x = x.strip().replace('$', '')

        if 'K' in x:
            return float(x.replace('K', '')) * 1000

        if 'M' in x:
            return float(x.replace('M', '')) * 1000000

        if 'B' in x:
            return float(x.replace('B', '')) * 1000000000



    return x


data['$ Last Change'] = data['$ Last Change'].apply(value_to_float)
data.head()
display(data[data['Total Net Worth']>=50])
display(data[data.Country=='India'])
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib import figure
style.use('fivethirtyeight')
india=data[data.Country=='India']
plt.bar(india['Industry'],india['Total Net Worth'],color='r')
plt.title("Industry")
plt.xlabel("Total Net Worth")
plt.gcf().set_size_inches(30, 10)
plt.show()
country=data["Country"].value_counts().head(10).values
name=data["Country"].value_counts().head(10).index
plt.gcf().set_size_inches(20, 11)
plt.pie(country,labels=name,autopct="%1.1f%%",wedgeprops={'edgecolor':'black'},explode=[0.1,0,0,0,0,0,0,0,0,0])
plt.title('Top 10')
plt.show()
data[data.Country=='UnitedStates'].head(10)
plt.bar(india['Name'],india['$ Last Change'],color=(india['$ Last Change']>0.0).map({True:'#DBB40C',False:'#A52A2A'}))
plt.xlabel("Indian Richies")
plt.ylabel("$ Last Change")
plt.gcf().set_size_inches(15, 8)
plt.xticks(rotation=90)
plt.show()