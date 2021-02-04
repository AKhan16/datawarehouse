#!/usr/bin/env python
# coding: utf-8

# In[2]:


from platform import python_version
print (python_version())


# In[4]:


if __name__ == "__main__":
    print("Hello, world!")


# In[5]:


# filename.py
"""
this is the file headr.
the header contains basic information about the file
"""
if __name__=="__main__":
    pass # 'pass' is a temporary placeholder


# In[10]:


def mathematical_opritions (x,y):
    if x==1:
        x=0
    add = x+y
    sub= y-x
    multi = x * y
    divi = x / y
    return add,sub,divi

_ , z , _ = mathematical_opritions(5,4)
print(z)


# In[12]:


$$v=\frac 4 (3).\pi.r^ 3 $$


# In[ ]:




