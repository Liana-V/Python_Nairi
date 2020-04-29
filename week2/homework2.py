#!/usr/bin/env python
# coding: utf-8

# In[3]:


#2+
def all_sums(number):
    list_sums = []

    for i in range(number // 2 + 1):
        for j in range(number // 2, number):
            if i + j == number:
                list_sums.append((i, j))
                
    return list_sums


all_sums(7)


# In[2]:


#3+
from collections import defaultdict

def duplicate_characters(string):
    d_dict = defaultdict(int)
    dup_char = set()
    
    for i in string.replace(" ",""):
        d_dict[i] += 1
    
    for i in d_dict:
        if d_dict[i] > 1:
            dup_char.add(i)
            
    return dup_char
    
    
duplicate_characters("Here we have some duplicates")


# In[1]:


#4+
def compare_lists(listOne, listTwo):
    productOne = 1
    productTwo = 1
    
    for i in listOne:
        productOne *= i
        
    for i in listTwo:
        productTwo *= i
        
    if sum(listOne) == sum(listTwo) and productOne == productTwo:
        return True
    return False
    
compare_lists([0,5,6], [6,0,5])


# In[14]:


#5+
def heapq(a,b):
    a.append(b)
    if len(a) % 2 != 0:
        for i in range(len(a) // 2):
            if a[i] >= a[2 * i + 1]:
                a[i], a[2 * i + 1] = a[2 * i + 1], a[i]
            if a[i] >= a[2 * i + 2]:
                a[i], a[2 * i + 2] = a[2 * i + 2], a[i]
    
    else:
        a.append(max(a))
        for i in range(len(a) // 2):
            if a[i] >= a[2 * i + 1]:
                a[i], a[2 * i + 1] = a[2 * i + 1], a[i]
            if a[i] >= a[2 * i + 2]:
                a[i], a[2 * i + 2] = a[2 * i + 2], a[i]
        a.pop()


    return a
    
    
heapq([1],2)


# In[1]:


# 6
def merge_sort(main_list,*args):
    lenght = len(main_list)
    if lenght > 1:
        mid = lenght // 2
        left_list = main_list[:mid]
        right_list = main_list[mid:]
        
        merge_sort(left_list, *args) #recursion for sublists
        merge_sort(right_list, *args)
        
        i = j = k = 0 #merging
        while i < len(left_list) and j < len(right_list):
            
            if len(args) > 0 and args [0] == "descending":
                if left_list[i] >= right_list[j]:
                    main_list[k] = left_list[i]
                    i += 1
                    k += 1
                else:
                    main_list[k] = right_list[j]
                    j += 1
                    k += 1
            else:
                if left_list[i] >= right_list[j]:
                    main_list[k] = right_list[j]
                    j += 1
                    k += 1
                else:
                    main_list[k] = left_list[i]
                    i += 1
                    k += 1
                  
            while i < len(left_list): #if elements of one list end, but remain elements of second list
                main_list[k] = left_list[i]
                i += 1
                k += 1

            while j < len(right_list):
                main_list[k] = right_list[j]
                j += 1
                k += 1
           
        return main_list
        
    
merge_sort([1,4,7,7,8,0,100],"descending")


# In[ ]:




