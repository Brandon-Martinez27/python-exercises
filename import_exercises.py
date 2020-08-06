#!/usr/bin/env python
# coding: utf-8

# ## 1. Import and test 3 of the functions from your functions exercise file.
# 
# Import each function in a different way:
# 
#     - import the module and refer to the function with the . syntax
#     - use from to import the function directly
#     - use from and give the function a different name

# In[13]:


# import the function_exercises.py file from
# my personal directory
import function_exercises
# call the function 'is_two' from my module
function_exercises.is_two(2)


# In[14]:


# from module, import the function 'is_vowel'
from function_exercises import is_vowel
# call the function 'is_vowel' to evaluate the string 'o'
is_vowel('o')


# In[15]:


# from module, import the function 'is_consonant',
# set function alias to ic
from function_exercises import is_consonant as ic
# call the function alias 'ic' to evaluate the string 'b'
ic('b')


#    
# ### For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# 
# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# 2. How many different ways can you combine two of the letters from "abcd"?

# In[16]:


# importing std library itertools
import itertools as it


# In[203]:


# 1.
# accessing chain function which outputs
# two sequences as one respectively
chain_1 = list(it.chain('123', 'abc'))

chain_2 = list(it.chain.from_iterable(chain_1))

product_1 = list(it.product('abc', '123'))

combo_1 = list(it.combinations('abc123', 2))


# In[18]:


# 2. 
# accesing combinations function which takes 
# 2 parameters (argument, and length of tuples)
# output in a list
combo_2 = list(it.combinations('ABCD', 2))
# gives back all possible unique combinations

perm_1 = list(it.permutations('ABCD', 2))

combo_3 = list(it.combinations_with_replacement('ABCD', 2))


# ### Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 
# - Total number of users
# - Number of active users
# - Number of inactive users
# - Grand total of balances for all users
# - Average balance per user
# - User with the lowest balance
# - User with the highest balance
# - Most common favorite fruit
# - Least most common favorite fruit
# - Total number of unread messages for all users

# In[92]:


# import profiles.json
import json
with open('profiles.json', 'r') as pj:
    profiles = json.load(pj)


# In[93]:


# total number of users
len(profiles)


# In[135]:


# number of active users
user_list = []
for p in profiles[0:20]:
    if p['isActive'] == True:
        user_list.append(p['isActive'])
number_of_active_users = len(user_list)
print(number_of_active_users)


# In[136]:


# number of inactive users
no_user_list = []
for p in profiles[0:20]:
    if p['isActive'] == False:
        no_user_list.append(p['isActive'])
number_of_active_users = len(no_user_list)
print(number_of_active_users)


# In[129]:


# Grand total of balances for all users
b_list = []
for p in profiles[0:20]:
    balance = p['balance'].strip('$,')
    balance = balance.replace(',', '_')
    balance = round(float(balance),2)
    b_list.append(balance)
grand_total = sum(b_list)
print(grand_total)


# In[140]:


# Average balance per user
average_balance = grand_total / len(profiles)
print(round(average_balance, 2))


# In[155]:


# User with the lowest balance
lowest_balance = min(b_list)
lowest_balance = str(lowest_balance)
lowest_balance = '$' + lowest_balance + '0'
lowest_balance = lowest_balance[:2] + ',' + lowest_balance[2:]
print(lowest_balance)

for p in profiles[0:20]:
    if p['balance'] == lowest_balance:
        print(p['name'])


# In[157]:


# User with the highest balance
highest_balance = max(b_list)
highest_balance = str(highest_balance)
highest_balance = '$' + highest_balance
highest_balance = highest_balance[:2] + ',' + highest_balance[2:]
print(highest_balance)

for p in profiles[0:20]:
    if p['balance'] == highest_balance:
        print(p['name'])


# In[169]:


# Most common favorite fruit
most_common_fruit = []
for p in profiles[0:20]:
    fav_fruit = p['favoriteFruit']
    most_common_fruit.append(fav_fruit)
from statistics import mode
mcf = mode(most_common_fruit)
print(mcf)


# In[178]:


# Least most common favorite fruit
most_common_fruit = []
for p in profiles[0:20]:
    fav_fruit = p['favoriteFruit']
    most_common_fruit.append(fav_fruit)
most_common_fruit.sort()
most_common_fruit
from collections import Counter
Counter(most_common_fruit).most_common()[:-2:-1]


# In[219]:


# Total number of unread messages for all users
from re import findall
num_list = []
for p in profiles[0:20]:
    only_numbers = findall('[0-9]+', p['greeting'])
    num_list.append(only_numbers)
print(num_list)


# In[227]:


str_numbers = list(it.chain.from_iterable(num_list))
print(str_numbers)


# In[228]:


numbers = [int(n) for n in str_numbers]
print(numbers)


# In[231]:


total_number_of_unread_messages = sum(numbers)
print(total_of_numbers)


# In[ ]:




