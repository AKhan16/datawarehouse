#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.1
from platform import python_version
print (python_version())


# In[5]:


# 1.2
# filename.py
"""
this is the file header.
the header contains basic information about the file.
"""
if __name__ == "__main__":
    pass # 'pass' is a temporary placeholder.


# In[12]:


#the comments can be written in the same block as the code


# the markdown can be in it's own box where it changes the text from code to HTML

# In[13]:


if __name__ == "__main__":
    print("Hello, world!")# indent with four spaces (not a tap).


# In[14]:


help(print)


# In[23]:


# Exercise 2:
x,y = 2,5
print (x+y)
print (x-y)
print (x*y)
print (x/y)
print (x//y)
print (x%y)
print (x**y)


# In[26]:


# Exercise 3:
x= 5
y= 2**2 +1
x == y


# In[27]:


# Exercise 3:
x,y = 5,2**(2+1)
x==y


# In[28]:


def add(x , y):
    return x + y

add(2,5)


# In[39]:


# Exercise 4
def compare(x,y):
    if y ==x:
        result = " y equals x"
    else:
        result = "y doesn't equals x"
    return result


compare(2,2)


# In[42]:


def add(x,y):
    return x,y, x+y

FV, SV, S=add(2,5)

print ("first variable is {} second veriable is {} and summations is {}".format(FV,SV, S))


# In[47]:


# i've been having issues with Exercise 5 and i couldn't find an answer to it


# In[50]:


Course_name = 'IS-372 Data Mining & Data Warehouse'
print(Course_name[2])


# In[56]:


# Exercise 6:
Course_name = 'IS-372 Data Mining & Data Warehouse'
print(Course_name[0:6])
print(Course_name[-1])
print(Course_name[:5])
print(Course_name[6:])


# In[61]:


# 1.4 
my_list =["Hello", 93.8, "World",10]
my_list[0]


# In[60]:


# 1.4 
my_list =["Hello", 93.8, "World",10]
my_list[-2]


# In[62]:


# 1.4 
my_list =["Hello", 93.8, "World",10]
my_list[:2]


# In[69]:


# 1.4 
my_list =[1, 2]
my_list.append(4)
my_list.insert(2, 3)
my_list.remove(3)
my_list.pop()


# In[70]:


# 1.4 
my_list =[1, 2]
my_list.append(4)
my_list


# In[71]:


#1.4
my_list =[1, 2]
my_list.append(4)
my_list.insert(2, 3)
my_list


# In[73]:


#1.4
my_list =[1, 2]
my_list.append(4)
my_list.insert(2, 3)
my_list.remove(3)
my_list


# In[74]:


# 1.4 
my_list =[1, 2]
my_list.append(4)
my_list.insert(2, 3)
my_list.remove(3)
my_list.pop()
my_list


# In[79]:


def arithemtic(a, b):
    """return the difference and the product of the two inputs."""
    return a - b, a * b
x, y = arithemtic(5,2) # Get each Value individually,
print(x, y)
both = arithemtic(5,2) # or get them both as a tuple
print(both) # for some reason the answer is flipped from the lap one


# In[112]:


# Exercise 7
def list_ops(animals = ["bear", "ant", "cat", "dog"]):
    animals.append("eagle")
    animals[2]= "fox"
    del animals[1]
    animals.sort
    animals[3] = "hawk"
    animals.insert(4,"hunter")
    
    return animals
print(animals)


# In[113]:


# Exercise 8
s = "stab"
for i in range(len(s)):
    print(s[0 : i : 1])


# In[ ]:




