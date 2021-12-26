#!/usr/bin/env python
# coding: utf-8

# In[5]:


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


# In[6]:


fact(5)


# In[32]:


def add_rec(n):
    if n > 0:
        b = n % 10
        return b + add_rec(n // 10)
    else:
        return 0


# In[35]:


add_rec(1234567)

# In[ ]:
