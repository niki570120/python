#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://running.biji.co/index.php?q=album&act=photo_list&cid=9261&type=special&subtitle=%E6%B5%AA%E6%BC%AB%E5%8F%B0%E4%B8%89%E7%B7%9A%202021%20%E6%88%80%E6%88%80%E6%A1%90%E8%8A%B1%E5%85%A8%E5%9C%8B%E8%B7%AF%E8%B7%91%E8%B3%BD-%E7%B7%A8%E8%BC%AF%E7%B2%BE%E9%81%B8'
html=requests.get(url)
html.text


# In[2]:


import re
match_list = re.findall(r'photo-img"\ src\s*=\s*"(.+?)"', html.text)

if match_list:
    print(match_list)


# In[3]:


match_list[0]


# In[4]:


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




