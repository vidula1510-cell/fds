#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as ds 
a1 = [2,-1,5,4]
d = ds.array(a1)
print(d.reshape(3,2))


# In[4]:


import numpy as ds 
a1 = [2,-1,5,4]
d = ds.array(a1)
print(d.reshape(2,0))


# In[7]:


import numpy as ds 
a1 = [2,-1,5,4]
d = ds.array(a1)
print(d.reshape(-2,-1))


# In[8]:


print(d.reshape(0,-2))


# In[10]:


import numpy as ds 
a1 = [2,-1,5,4]
d = ds.array(a1)
print(d.reshape(-2,1))


# In[19]:


p = ds.array([[1,2],[3,4],[5,6]])
q = ds.array([[7,8],[9,10],[11,12]])
s = ds.concatenate((p,q),axis =1)
print(s)


# In[21]:


t = ds.array([[13,14],[15,16],[17,18]])
s1 = ds.concatenate((p,q,t),axis =1)
print(s1)


# In[25]:


a = ds.array([1,2,3])
b = ds.array([4,5,6,7])
c = ds.concatenate((a,b))
print(c)


# In[46]:


t1 = ds.array([[19,20],[21,22]])
t2 = ds.concatenate((t,t1))
t2


# In[49]:


a = ds.array([1,2,3,4,5,6])
b1 = ds.array_split(a)
print(b1)


# In[41]:


b2 =ds.array_split(a,0)


# In[32]:


b3 =ds.array_split(a,-2)


# In[39]:


b4 =ds.array_split(a,5)
print(b4)


# In[40]:


b5 =ds.array_split(a,20)
print(b5)


# In[ ]:




