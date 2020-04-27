#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1+
def implication3(a,b,c):
    def implication2(b,c):
        return not(b and not c)
        
    return implication2(a,implication2(b,c))


# In[2]:


#2-առանց eval—ի չստացվեց

def expr_value(a):
    return str("{:.2f}".format(eval(a)))


# In[3]:


#3 չի աշխատում, բայց

def recursive_or(x):
    return x[:1] or recursive_or(x[1:])


def quick_or(x):
    return True in x


# In[ ]:


def f(a):
    return 
    
    
f([True,False,False])


# In[4]:


#4+
def is_polyndrome(a):
    a_count_even = []
    set_a = set(a)
    for i in set(a):
        if a.count(i)%2!=0:
            a_count_even.append(a.count(i))

    if len(a_count_even)>1:
        return False
    return True


# In[5]:


#5+
#հաշվարկի վարկյանները չհասկացա ոնց պետք է ստուգեմ

# օրինաչափություն եմ գտել ամեն 20-րդ թվի գումարի վերջին թվանշանի համար
def last_digit(a):
    
    last_digit = int()
    while a > 20:
        a -= 20
    for i in range(1,a+1):
        last_digit += i**2
    
    return str(last_digit)[-1]


# In[ ]:




