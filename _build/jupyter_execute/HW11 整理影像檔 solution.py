#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil

# 設定檔案及路徑
file_name = './櫻桃小丸子.zip'
directory = './output'
unzip_folder = './櫻桃小丸子'

# 建立新目錄
if os.path.exists(directory):
    shutil.rmtree(directory)
os.makedirs(directory)


# In[2]:


# 解壓縮
import zipfile
with zipfile.ZipFile(file_name, 'r') as zip_ref:
    zip_ref.extractall(unzip_folder)


# In[4]:


# 複製檔案並改名
from shutil import copy2

no = 1
for file in os.listdir(unzip_folder):
    source_file_path = os.path.join(unzip_folder, file)
#     print(source_file_path)
    if (file.lower().endswith(".jpg") or file.lower().endswith(".jpeg")) and os.path.getsize(source_file_path) >= 5 * 1024:
        copy2(source_file_path, f'{directory}/{no:03d}.jpg')
        no+=1


# In[ ]:




