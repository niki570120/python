#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 引進相關套件
import requests
from io import StringIO
import pandas as pd
import numpy as np


# In[2]:


# 資料日期
date1 = '20210720'
stockNo = '2330'
# 網址
url= 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date={}&stockNo={}'.format(date1, stockNo)


# In[3]:


response = requests.post(url)


# In[4]:


clean_data=[]
for row in response.text.split('\n'):
    fields=row.split('",')
    if len(fields) == 10 and row[0] != '=':
        clean_data.append(row.replace(' ',''))

csv_data = "\n".join(clean_data)
print(csv_data)


# In[5]:


df = pd.read_csv(StringIO(csv_data))
df.head(100)


# In[6]:


df['日期'] = df['日期'].apply(lambda x:str(int(x[:3])+1911)+'-'+x[4:6]+'-'+x[-2:])
df.head()


# In[7]:


from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse
import pandas as pd
import matplotlib.pyplot as plt

# Import Data 時間序列
df = pd.read_csv((StringIO(csv_data))
dates = pd.日期([parse(d).strftime('%Y-%m-01') for date in df['date']])
df.set_index(dates, inplace=True)

# Decompose 
result = seasonal_decompose(df['value'], model='multiplicative')

# Plot
plt.rcParams.update({'figure.figsize': (10,10)})
result.plot().suptitle('Time Series Decomposition of Air Passengers')
plt.show()


# In[ ]:




