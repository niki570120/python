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
url= 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date=20210701&stockNo=2327'.format(date1, stockNo)


# In[3]:


# 送出要求，並取得回應資料
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
df.head()


# In[6]:


# method 1：lambda
df['日期'] = df['日期'].apply(lambda x:str(int(x[:3])+1911)+'-'+x[4:6]+'-'+x[-2:])
df.head()


# In[7]:


# method 2：function
def convert_date(x):
    year = int(x[:3])+1911
    month = x[4:6]
    day = x[-2:]
    return str(year) +'-'+month +'-'+day

df['日期'] = df['日期'].apply(convert_date)
df.head()


# In[8]:


df.info()


# In[9]:


df['日期'] = pd.to_datetime(df['日期'])
df.head()


# In[12]:


df.info()


# In[7]:


# 刪除無用的欄位
df.drop(df.columns[-1], axis=1, inplace=True)


# In[8]:


df.info()


# In[9]:


# 將以下欄位轉為數值
numeric_columns=['成交股數','成交金額','成交筆數']
for i in numeric_columns:
    df[i]=df[i].map(lambda x:x.replace(',', '').replace('--', ''))
    df[i]=pd.to_numeric(df[i])
df.info()


# In[10]:


df.to_csv('個股日成交資訊.csv', index=False)


# In[11]:


df.to_excel('個股日成交資訊.xlsx', index=False)


# In[ ]:




