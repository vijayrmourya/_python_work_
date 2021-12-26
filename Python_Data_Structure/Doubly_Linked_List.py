#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prevnode = None


# In[4]:


A = Node(25)
B = Node(50)
C = Node(75)
A.nextnode = B
B.nextnode = C
B.prevnode = A
C.prevnode = B
Head = A
Tail = C

# In[7]:


head = Head
while head.nextnode != None:
    print(head.value)
    head = head.nextnode
if (head.nextnode == None):
    print(Tail.value)

# In[8]:


Z = Node(100)
F = Node(20)
Head.prevnode = F
F.nextnode = Head
Head = F
Tail.nextnode = Z
Z.prevnode = Tail
Tail = Z

# In[12]:


head = Head
while head.nextnode != None:
    print(head.value)
    head = head.nextnode
if (head.nextnode == None):
    print(head.value)

# In[13]:


tail = Tail
while tail.prevnode != None:
    print(tail.value)
    tail = tail.prevnode
if (tail.prevnode == None):
    print(tail.value)

# In[ ]:
