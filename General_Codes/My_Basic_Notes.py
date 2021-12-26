#!/usr/bin/env python
# coding: utf-8

# # Hello World!

# In[2]:


# Hello World
print("Hello World!")


# # Python Indentation

# In[8]:


def func():
    # it is the first level indentation
    # everything with this indentation is in function func()
    if (True):
        # it is the second level indentation
        # everything with this indentation is in function func() but deep inside if block
        pass
    # if block ends
    else:
        # it is the second level indentation
        # everything with this indentation is in function func() but deep inside else block
        if (True):
            # it is the third level indentation
            # everything with this indentation is in function func() but deep inside else and then in if block
            pass
        # it is the second level indentation
        # everything with this indentation is in function func() but deep inside else block
        pass


print("We're officially out of the function func()")
print("Python Indentation")

# # Python Comments

# In[3]:


# This is a comment 
# Print “Hello python !” to console 
print("Hello Python!")

# In[4]:


""" 
This would be a multiline comment in Python that 
spans several lines without any limit.
"""
print("Hello Nikita!")

# # Variables

# In[6]:


# An integer assignment 
age = 45

# A floating point 
salary = 1456.8

# A string   
name = "John"

# A boolean
Employed = True

print("Age:", age)
print("salary:", salary)
print("name:", name)
print("employed:", Employed)

# # Operators

# In[9]:


# Examples of Arithmetic Operator 
a = 9
b = 4

# Addition of numbers 
add = a + b
# Subtraction of numbers  
sub = a - b
# Multiplication of number  
mul = a * b
# Division(float) of number  
div1 = a / b
# Division(floor) of number  
div2 = a // b
# Modulo of both number 
mod = a % b

# print results 
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)

# In[10]:


# Examples of Relational Operators 
a = 13
b = 33

# a > b is False 
print(a > b)

# a < b is True 
print(a < b)

# a == b is False 
print(a == b)

# a != b is True 
print(a != b)

# a >= b is False 
print(a >= b)

# a <= b is True 
print(a <= b)

# In[11]:


# Examples of Logical Operator 
a = True
b = False

# Print a and b is False 
print(a and b)

# Print a or b is True 
print(a or b)

# Print not a is False 
print(not a)

# ##### How logical operators work

# In[13]:


# Logical operator returns True if both the operands are True else it returns False.
# Python program to demonstrate 
# logical and operator 

a = 10
b = 10
c = -10

if a > 0 and b > 0:
    print("The numbers are greater than 0")

if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")

# In[14]:

# Python program to demonstrate
# logical and operator 

a = 10
b = 12
c = 0

if a and b:
    print("The numbers are greater than 0")
if a and b and c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")

# In[16]:

'''the logical operators work on the principle if any number is greater than 0 then its true and if any number is less than
or equal to 0 then its false'''

# In[28]:


# Examples of Bitwise operators 
a = 10
b = 4

# Print bitwise AND operation 
print("bitwise AND operation ")
print(bin(a))
print(bin(b))
print(bin(a & b))
print("a AND b:", a & b)
print("-----------------------------")

# Print bitwise OR operation 
print("bitwise OR operation ")
print(bin(a))
print(bin(b))
print(bin(a | b))
print("a OR b:", a | b)
print("-----------------------------")

# Print bitwise NOT operation  
print("bitwise NOT operation ")
print(bin(a))
print(bin(~a))
print("NOT of a:", ~a)
print("-----------------------------")

# print bitwise XOR operation  
print("bitwise XOR operation ")
print(bin(a))
print(bin(b))
print(bin(a ^ b))
print("a XOR b:", a ^ b)
print("-----------------------------")

# print bitwise right shift operation  
print("bitwise right shift operation ")
print(bin(a))
print(bin(a >> 2))
print("right shift a by 2 bit:", a >> 2)
print("-----------------------------")

# print bitwise left shift operation  
print("bitwise left shift operation ")
print(bin(a))
print(bin(a << 2))
print("left shift a by 2 bit:", a << 2)
print("-----------------------------")

# ### Special operators: Special operators are of two types-
# ###### Identity operator that contains is and is not.
# ###### Membership operator that contains in and not in.

# In[32]:


# Examples of Identity and 
# Membership operator


a1 = 'Vijay Mourya'
b1 = 'Mourya Vijay'

# Identity operator
print(a1 is not b1)
print(a1 is b1)

# Membership operator
print("G" in a1)
print("N" not in b1)

# with if block
if "V" in a1:
    print("character found in a1")
elif "V" in b1:
    print("character found in b1")
else:
    print("character found")

# # User Input

# In[33]:


# Never make prompts while reading user input unless it is asked in w=question or application requirement
username = input("Enter username:")
print("Username is: " + username)

# In[34]:


phone = int(input("Enter your number:"))
print("Phone Number:", phone)

# In[36]:


# taking multiple user input in seperate variables
A, B, C, D, E = "V", "I", "J", "A", "Y"
print(A + B + C + D + E)

# In[39]:


# Taking multiple user inputs in a list by default all are string
A = input().split()
print(A)
# to conver in into in use type conversion
for i in range(len(A)):
    A[i] = int(A[i])
print(A)

# # printing output

# In[1]:


# printing one lines using multiple print statements
print("Nikita", end=" ")
print("Narendra", end=" ")
print("Kondalkar", end=" ")

# In[7]:


# Using +" "+ to concat string
A, B, C, D = "Vijay", "R", "Mourya", 22
print("Name :" + A + ", Father's initial :" + B + ", Surname :" + C + ", Age :" + str(D))

# In[8]:


# Using , to concat string
A, B, C, D = "Vijay", "R", "Mourya", 22
print("Name :", A, ", Father's initial :", B, ", Surname :", C, ", Age :", str(D))

# In[9]:


# Using .format{} to print
A, B, C, D, E = "one", "two", "three", 4, 5
print("number {}, number {}, number {}, number {}, number {}".format(A, B, C, D, E))

# In[14]:


# Using .format{} to print multi line string with custome fomating variable
A, B, C = "Vijay", "Mourya", "TCS"
print(
    "Name {name} {surname} working at {Company}, {name} is 22 Years old, will continue to work at {Company} for 2 years more".format(
        name=A, surname=B, Company=C))

# In[15]:


# Using f" " to print
A, B, C, D, E = "one", "two", "three", 4, 5
print(f"number {A}, number {B}, number {C}, number {D}, number {E}")

# # Data Type

# In[24]:


# Python program to  
# demonstrate numeric value 

print("Type of a: ", type(5))

print("\nType of b: ", type(5.0))

c = 2 + 4j
print("\nType of c: ", type(c))

# In[26]:


# Python Program for  
# Creation of String  

# String with single quotes   
print('Welcome to the Python World')

# String with double quotes  
print("I'm a Python coder")

# String with triple quotes
print('''I'm a vijay and I live in a world of "Python"''')

# In[28]:


String1 = "Vijay Mourya"

# Printing First character 
print(String1[0])

# Printing Last character 
print(String1[-1])

# # Python Program to Update / delete  character of a String  
# String1 = "Hello, I'm a Geek"
#      
# ##### Updating a character
# String1[2] = 'p' 
# ##### ‘str’ object does not support item assignment gives error
# '''Traceback (most recent call last):
# File “/home/360bb1830c83a918fc78aa8979195653.py”, line 6, in
# String1[2] = ‘p’
# TypeError: ‘str’ object does not support item assignment'''
#    
# ##### Deleting a character   
# del String1[2]
# ##### ‘str’ object doesn’t support item deletion gives error
# Traceback (most recent call last):
# File “/home/499e96a61e19944e7e45b7a6e1276742.py”, line 8, in
# del String1[2]
# TypeError: ‘str’ object doesn’t support item deletion

# # String: Operating, Manipulating and Functions

# In[39]:


# capitalize() 	Converts the first character to upper case
A = "vijay mourya"
print(A)
B = A.capitalize()
print(B)

# In[43]:


# count()	Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
x = txt.count("a")
print(x)
x = txt.count("l")
print(x)

# In[48]:


# endswith()	Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith("world.")
print(x)
x = txt.endswith("ld.")
print(x)
x = txt.endswith("Hello")
print(x)
x = txt.endswith("to my world.")
print(x)

# In[97]:


# ----------------------------------------------------------------------------------------------------------
# find()	Searches the string for a specified value and returns the position of where it was found
# index()	Searches the string for a specified value and returns the position of where it was found

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print("find", x)
x = txt.find("welcome")
print("index", x)

# Where in the text is the first occurrence of the letter "w"?:
x = txt.find("w")  # there are two W but it returns first index
print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
x = txt.find("w", 5, 10)  # there is one W in " welc" it returns first index
print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 8 and 23?:
x = txt.find("w", 8, 23)  # there is one W in "elcome to my wor" it returns first index
print(x)

# ----------------------------------------------------------------------------------------------------------
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found

txt = "Hello, welcome to my world."
x = txt.rfind("welcome")
print("rfind", x)
x = txt.rindex("welcome")
print("rindex", x)

# Where in the text is the first occurrence of the letter "w"?:
x = txt.rfind("w")  # there are two W but it returns first index
print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
x = txt.rfind("w", 5, 10)  # there is one W in " welc" it returns first index
print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 8 and 23?:
x = txt.rfind("w", 8, 23)  # there is one W in "elcome to my wor" it returns first index
print(x)

# In[80]:


# isalnum()	Returns True if all characters in the string are alphanumeric i.e. alphabets/numbers
txt = "Company 12"
x = n.isalnum()
print(x)
txt = "Company"
x = txt.isalnum()
print(x)
txt = "121512"
x = txt.isalnum()
print(x)
txt = "---------"
x = txt.isalnum()
print(x)

# In[81]:


# isalpha()	Returns True if all characters in the string are in the alphabet
txt = "Company 12"
x = n.isalpha()
print(x)
txt = "Company"
x = txt.isalpha()
print(x)
txt = "121512"
x = txt.isalpha()
print(x)
txt = "---------"
x = txt.isalpha()
print(x)

# In[82]:


# isdigit()	Returns True if all characters in the string are digits
txt = "Company 12"
x = n.isdigit()
print(x)
txt = "Company"
x = txt.isdigit()
print(x)
txt = "121512"
x = txt.isdigit()
print(x)
txt = "---------"
x = txt.isdigit()
print(x)

# In[85]:


# islower()	Returns True if all characters in the string are lower case
# lower()	Converts a string into lower case
txt = "hello world!"
x = txt.islower()
print(x)
txt = "HeLLO world!"
x = txt.islower()
print(x)
txt = txt.lower()
x = txt.islower()
print(x)

# In[102]:


# isupper()	Returns True if all characters in the string are upper case
# upper()	Converts a string into upper case
txt = "HELLO WORLD!"
x = txt.isupper()
print(x)
txt = "HeLLO world!"
x = txt.isupper()
print(x)
txt = txt.upper()
x = txt.isupper()
print(x)

# In[103]:


# swapcase()	Swaps cases, lower case becomes upper case and vice versa
txt = "HELLO WORLD!"
x = txt.swapcase()
print(x)
txt = "HeLLO world!"
x = txt.swapcase()
print(x)

# In[92]:


# replace()	Returns a string where a specified value is replaced with a specified value
A = "Nikita Kondalkar"
A = A.replace("N", "K")
print(A)
A = "Nikita Kondalkar"
A = A.lower()
A = A.replace("N", "K")
print(A)
A = "Nikita Kondalkar"
A = A.lower()
A = A.replace("n", "K")
print(A)

# In[101]:


# split()	Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

# # List: operating manipulating and functions

# In[110]:


# Python program to demonstrate   
# Creation of List   

# Creating a List  
List = []
print(List)

# Creating a list of strings
List = ['GeeksForGeeks', 'Geeks']
print(List)

# Creating a Multi-Dimensional List  
List = [['Geeks', 'For'], ['Geeks']]
print(List)

# In[111]:


# Python program to demonstrate   
# Addition of elements in a List  

# Creating a List  
List = []

# Using append()
List.append(1)
List.append(2)
print(List)

# Using insert()
List.insert(3, 12)
List.insert(0, 'Geeks')
print(List)

# Using extend()  
List.extend([8, 'Geeks', 'Always'])
print(List)

# In[112]:


# Python program to demonstrate   
# accessing of element from list  


List = [1, 2, 3, 4, 5, 6]

# accessing a element
print(List[0])
print(List[2])

# Negative indexing
# print the last element of list  
print(List[-1])
# print the third last element of list   
print(List[-3])

# In[113]:


# Python program to demonstrate   
# Removal of elements in a List  

# Creating a List  
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]

# using Remove() method  
List.remove(5)
List.remove(6)
print(List)

# using pop()
List.pop()
print(List)

# In[115]:


fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# In[117]:


a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

# In[118]:


fruits = ['apple', 'banana', 'cherry', 'orange']
print(fruits)
fruits.clear()
print(fruits)

# In[119]:


fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# In[121]:


fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

# In[123]:


fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

# In[125]:


fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

# In[128]:


# insert()	Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

name = ['Nikita', 'Kondalkar']
name.insert(1, 'Narendra')
print(name)

# In[132]:


# pop()	Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop()
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(0)
print(fruits)

# In[138]:


# remove()	Removes the first item with the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

point = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 1, 2, 3, 4]
print(point)
print("count before removing 3 from list :", point.count(1))
point.remove(1)
print("count after removing 3 from list :", point.count(1))
print(point)

# In[139]:


# reverse()	Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# In[142]:


# sort()	Sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

point = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 1, 2, 3, 4]
point.sort()
print(point)

# In[143]:


# Sort the list descending:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

point = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 1, 2, 3, 4]
point.sort(reverse=True)
print(point)

# # Genrally used combined string and list function

# In[145]:


# dividing each letter of string into a list
txt = "welcome to the jungle"
x = list(txt)
print(x)
a = "".join(x)
print(a)

# In[149]:


txt = "welcome to the jungle"
x = txt.split(" ")
print(x)
a = "---".join(x)
print(a)

txt = "welcome to the jungle"
x = txt.replace(" ", "---")
print(x)

# In[154]:


A = 'A function that returns the length of the value'
x = A.split(" ")
print(x)
print(f'string has {len(x)} words')
x.sort()
print('words sorted in alphabetical order', x)
x.sort(reverse=True)
print('words sorted in reverse order', x)

# In[ ]:
