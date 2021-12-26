#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


# In[2]:


Head = None
Tail = None
a = Node(56)
b = Node(46)
Head = a
Tail = b

# In[3]:


a.nextnode = b
c = Node(86)
d = Node(46)
e = Node(85)
Tail = e
Head = c
c.nextnode = a
b.nextnode = d
d.nextnode = e

# In[4]:


head = Head
while head.nextnode != None:
    print(head.value)
    head = head.nextnode
if (head.nextnode == None):
    print(Tail.value)

# In[6]:


last = Node(6)
new = Node(6855)
new.nextnode = Head
Head = new
Tail.nextnode = last
Tail = last
head = Head
while head.nextnode != None:
    print(head.value)
    head = head.nextnode
if (head.nextnode == None):
    print('last node: ', Tail.value)

# In[11]:


head = Head
while head.nextnode != None:
    print(head.value)
    head = head.nextnode
if (head.nextnode == None):
    print('last node: ', Tail.value)

# In[ ]:
