#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://in.tradingview.com/markets/stocks-india/market-movers-gainers/"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,"html.parser")
print(soup)


# In[2]:


names=soup.find_all(class_="apply-common-tooltip tickerDescription-GrtoTeat")
names


# In[3]:


Company=[]
for i in range(0,len(names)):
    Company.append(names[i].get_text())
print(Company)


# In[4]:


Percentage_Change=soup.find_all(class_="positive-p_QIAEOQ")
Percentage_Change


# In[5]:


PercentageChange=[]
for i in range(0,len(Company)):
    PercentageChange.append(Percentage_Change[i].get_text())
print(PercentageChange)


# In[6]:


import pandas as pd
df=pd.DataFrame({'Company_Name':Company,'Change %':PercentageChange})
df


# In[7]:


df.to_csv("Top gainer stocks.csv",index= False)


# In[8]:


Stocks_info=pd.read_csv("Top gainer stocks.csv")
print(Stocks_info)

