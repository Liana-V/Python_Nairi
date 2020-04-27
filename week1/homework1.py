#!/usr/bin/env python
# coding: utf-8

# In[107]:


#1 +
def all_positive(x,*args):
    return x<0 or True in [i<0 for i in args]

all_positive(1,2,3,7,9)


# In[13]:


#2 +

def xor3(a,b,c):
    def xor4(a,b):
        return a and not b or b and not a
    return xor4(xor4(a,b),c)


xor3(1,0,0)


# In[35]:


#3 +

def mirror_string(a):
    a=list(a)
    for char in range(len(a)):
        if a[char].islower():
            a[char] = chr(122-ord(a[char])+97)
        if a[char].isupper():
            a[char] = chr(90-ord(a[char])+65)
    return "".join(a)
           
print(mirror_string("Hello, World!"))


# In[73]:


#4 +

def bit_concat(x):
    if len(x)==0 or len(x)>4:
        return "Invalid_set"
    
    st_index = 6
    end_index = 8
    b = ""
    
    binary_values = [bin(i)[2:].rjust(8,"0") for i in x]

    
    for i in binary_values:
        b = i[st_index:end_index] + b
       
        st_index -= 2
        end_index -= 2
        
    return int(b,2)
    
    
bit_concat([3,12])


# In[7]:


#5 +

def binary_sum(a,b):
    return int(a,2) + int(b,2)


binary_sum ("1110","1111")


# In[3]:


#6 +
def only_names(a):
    return a

list(filter(only_names, (["Vlad","","Nairi",""])))


# In[39]:


#7 +

discriminant = lambda a, b, c: b ** 2 - 4 * a * c

discriminant (4, 8, 0)


# In[46]:


#8 +

full_name = lambda x,y: f"{x} {y}"

list(map(full_name,["Nairi","Vlad"],["Hakobyan","Poghosyan"]))


# In[ ]:




