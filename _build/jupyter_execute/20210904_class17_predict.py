#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib

clf = joblib.load('model.joblib')


# In[2]:


# pclass	sex	age	sibsp	parch	fare	adult_male	embark_town
X = [[2, 1, 30, 0, 0, 30, 1, 1], [1, 0, 10, 0, 0, 30, 0, 1]]

clf.predict(X)


# In[3]:


clf.predict_proba(X)


# In[ ]:





# In[ ]:




