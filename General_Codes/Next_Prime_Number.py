#!/usr/bin/env python
# coding: utf-8

# Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
# 

# In[11]:


def prime(num):
    while (1):
        st = 0
        c = 0
        num = num + 1
        for i in range(2, num + 1):
            if num % i == 0:
                c += 1
                if c > 1:
                    break
        if c == 1:
            print("your next prime number is: ", num)
            print("Do you want next prime number as well (y/n)")
            a = input().lower()
            if a == 'n':
                print("Thank you! bye.")
                break


# In[15]:


a = input("Let me know when to start by typing \'start\'").upper()
if a == 'START':
    prime(1)
else:
    print('Invalid!')

# In[ ]:


# In[ ]:
