#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Single input int
A = int(input())
print(A)

# In[3]:


# single input string
B = input()
print(B)

# In[9]:


# two inputs
C, D = input().split(' ')

# In[1]:


# input list for a single line input
E = []
E = input().split(' ')
print(E)

# In[2]:


# Multi line input
F = []
for i in input().split(' '):
    F.append(i)
print(F)

# In[ ]:


# In[ ]:
