#!/usr/bin/env python
# coding: utf-8

# For the given array find the largest possible sum from the elements and the list of element

# In[3]:


# input:
# 1 3 -5 6 -8 9 -4 2 9 7

# output:
# 37
# [1, 3, 6, 9, 2, 9, 7]


# In[4]:


a = input().split(' ')
b = [int(i) for i in a]
sum = 0
lis = []
for i in b:
    osum = sum
    sum = sum + i
    if osum > sum:
        sum = osum
    else:
        lis.append(i)
print(sum)
print(lis)

# In[ ]:
