#!/usr/bin/env python
# coding: utf-8

# Fibonacci Sequence

# Enter a number and have the program generate the Fibonacci sequence of that length.

# In[ ]:


# input:
# 5

# output:
# 1
# 1
# 2
# 3
# 5


# In[29]:


while (1):
    A = int(input("Please tell the length of series, (range 1 to 1000) :"))
    if (A > 1 and A < 1001):
        print(f"Here is your Series of {A} Numbers:")
        num1, num2 = 0, 1
        for i in range(1, A + 1):
            print(num2)
            #         temp=num2
            #         num2=num1+num2
            #         num1=temp
            num1, num2 = num2, num1 + num2
        break
    else:
        print('Please enter a valid range')
        continue

# In[ ]:
