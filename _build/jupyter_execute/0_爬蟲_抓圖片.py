#!/usr/bin/env python
# coding: utf-8

# # 爬蟲解析，使用 Regular Expression
# https://running.biji.co/index.php?q=album&act=photo_list&album_id=30668&cid=5791&type=album&subtitle=%E7%AC%AC%E4%B8%89%E5%B1%86%E5%9F%94%E9%87%8C%E8%B7%91%20Puli%20Power%20%E5%B1%B1%E5%9F%8E%E6%B4%BE%E5%B0%8D%E9%A6%AC%E6%8B%89%E6%9D%BE%20-%20%E5%90%91%E5%96%84%E6%A9%8B(%E7%B4%8434K)

# In[1]:


import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://running.biji.co/index.php?q=album&act=photo_list&album_id=30668&cid=5791&type=album&subtitle=第三屆埔里跑 Puli Power 山城派對馬拉松 - 向善橋(約34K)'
html=requests.get(url)
html.text


# In[2]:


import re
match_list = re.findall(r'photo-img"\ src="\.+"', html.text)

if match_list:
    print(match_list)


# In[3]:


len(match_list)


# In[4]:


import re
match_list = re.findall(r'photo-img"\ src\s*=\s*"(.+?)"', html.text)

if match_list:
    print(match_list)


# In[5]:


match_list[0]


# In[6]:


images_dir='./output'
#加目錄
import os

images_dir='./output'
os.makedirs(images_dir, exist_ok=True)

n=0
for src in match_list:
    if src != None and ('.jpg' in src):
        full_path = src
        filename = full_path.split('/')[-1] 
        print(full_path)
       
        try:
            image = urlopen(full_path)
            with open(os.path.join(images_dir,filename),'wb') as f:
                f.write(image.read())
            n+=1
        except:
            print("{} 無法讀取！".format(filename))
        
print("共下載",n,"張圖片")


# In[ ]:




