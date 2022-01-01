#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy
import scipy.misc
import matplotlib.pyplot as plt


# In[2]:


# mask
x = np.array([1,2,3,4,5])
print(x>3)
x[x>3]


# # 讀取 scipy 內建影像，並轉為灰階

# In[3]:


face = scipy.misc.face(gray=True)
plt.imshow(face, cmap=plt.cm.gray)
plt.axis('off')
plt.show()


# ## 圓以外設成黑色(0)，白色(255)

# In[4]:


lx, ly = face.shape
# 取得影像 X、Y 座標
X, Y = np.ogrid[0:lx, 0:ly]

# 圓以外設成黑色(0)
mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/4
face[mask] = 255


# In[5]:


X.shape, Y.shape


# In[6]:


plt.imshow(face, cmap=plt.cm.gray)
plt.axis('off')


# # 縮小圓

# In[7]:


# 縮小圓, lx*ly/4 ==> lx*ly/6
# 圓以外設成黑色(0)
mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/6 
face[mask] = 255

plt.imshow(face, cmap=plt.cm.gray)
plt.axis('off')


# # 讀取影像檔

# In[8]:


import matplotlib.image as mpimg

img = mpimg.imread('./lena.jpg')     
plt.imshow(img) 
plt.axis('off')
plt.show()


# # 讀取影像檔，並轉為灰階

# In[45]:


import matplotlib.image as mpimg

def rgb2gray(rgb):
    print(rgb.shape)
    # gray = 0.2989 R + 0.5870 G + 0.1140 B 
    return np.dot(rgb, [0.2989, 0.5870, 0.1140])

img = mpimg.imread('./lena.jpg')     
gray = rgb2gray(img)    
plt.imshow(gray, cmap='gray')
plt.axis('off')
plt.show()


# # 圓形特效

# In[46]:


img = mpimg.imread('./lena.jpg')   

lx, ly, lz = img.shape
# 取得影像 X、Y 座標
X, Y, Z = np.ogrid[0:lx, 0:ly, 0:lz]
X.shape, Y.shape, Z.shape


# In[47]:


type(img), img.shape


# In[48]:


img.flags


# ## RGB 分別處理

# In[92]:


img2 = np.array(img.copy())
mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/6 
R = img2[:,:,0:1]
R[mask] = 0
# R.shape

G = img2[:,:,1:2]
G[mask] = 0

B = img2[:,:,2:]
B[mask] = 0

mask_rgb = np.concatenate((R,G,B), axis=2) 
mask_rgb.shape


# In[93]:


plt.imshow(mask_rgb) 
plt.axis('off')
plt.show()


# In[ ]:





# ## 逐點處理(pixel-wised)

# In[49]:


# 圓以外設成黑色(0)
# mask = (X - lx/2)**2 + (Y - ly/2)**2 > lx*ly/6 
img2 = img.copy()
for i in range(lx):
    for j in range(ly):
        if (i - lx/2)**2 + (j - ly/2)**2 > lx*ly/6:
            img2[i,j,:] = 255

plt.imshow(img2) 
plt.axis('off')
plt.show()


# ## 採剪

# In[50]:


import matplotlib.image as mpimg

img = np.array(mpimg.imread('./lena.jpg'))
img_trim = img[128:384, 128:384, :]  
plt.imshow(img_trim)
plt.axis('off')
plt.show()


# In[51]:


import matplotlib.image as mpimg

img = np.array(mpimg.imread('./lena.jpg'))
img_trim = img[244:386, 236:386, :]  
plt.imshow(img_trim)
plt.axis('off')
plt.show()


# # 黑白、彩色混合

# In[49]:


gray = rgb2gray(img)    
gray.shape


# In[52]:


gray = gray.reshape(*gray.shape,1)
gray.shape


# In[53]:


gray_rgb = np.concatenate((gray, gray, gray), axis=2) / 255
gray_rgb.shape


# In[54]:


plt.imshow(gray_rgb)
plt.axis('off')
plt.show()


# In[55]:


gray_rgb[244:386, 236:386, :] = img_trim / 255
plt.imshow(gray_rgb)
plt.axis('off')
plt.show()


# In[ ]:




