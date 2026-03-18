#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.round(9.510597450,3)
print(a)


# In[3]:


a=np.floor(15.97)
print(a)


# In[4]:


b=np.floor(99.72)
print(b)


# In[5]:


c=np.floor(-72.72)
print(c)


# In[6]:


a=np.ceil(0.01)
print(a)


# In[7]:


b=np.ceil(2.99)
print(b)


# In[8]:


c=np.ceil(-4.97)
print(c)


# In[12]:


#logrithmic function
import numpy as  ds
a=ds.log2(7)
b=ds.arange(1,20)
c=ds.log2(b)
print(c)


# In[13]:


a=ds.log10(8)
b=np.arange(1,20)
c=ds.log10(b)
print(c)


# In[14]:


a=ds.log(10)
print(a)


# In[15]:


#sumetion function
import numpy as abc
test1=abc.array([1,2,3,4])
test2=abc.array([5,6,7,8])
a=abc.sum([test1,test2])
print(a)


# In[23]:


test1=abc.array([1,2,3,4])
test2=abc.array([5,6,7,8])
test3=abc.array([2,9,1,4,])
a=abc.sum([test1,test3])
print(a)


# In[25]:


tes1=abc.array([1,-2,-3,4,5])
test2=abc.array([5,6,-7,8])
d=abc.sum([test1,test2])
print(d)


# In[26]:


e=abc.sum([test1,test3],axis=1)
print(e)


# In[31]:



#production
import numpy as np
test1=abc.array([1,2,3,4])
a=np.prod(test1)
print(a)


# In[33]:


test1=abc.array([1,2,3,4])
test2=abc.array([5,6,7,8])
b=np.prod(test1,test2)
print(b)


# In[ ]:





# In[ ]:




