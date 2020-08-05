#!/usr/bin/env python
# coding: utf-8

# ## 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise

# In[8]:


def is_two(x):
    if x == 2 or x == '2':
        return True
    else: 
        return False


# In[9]:


is_two(2)


# In[10]:


is_two(4)


# In[18]:


is_two('2')


# ## 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[40]:


def is_vowel(string):
    if string.lower() in 'aeiou':
        return True
    else:
        return False


# In[50]:


is_vowel('A')


# In[51]:


is_vowel('dsgasf')


# In[33]:


is_vowel('o')


# ## 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[68]:


def is_consonant(string):
    if is_vowel(string) == False and len(string) == 1:
        return True
    else: 
        return False


# In[69]:


is_consonant('ez')


# In[57]:


is_consonant('z')


# In[58]:


is_consonant('a')


# ## 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[135]:


def capitalize_first_letter_of_consonant(string):
    if is_consonant(string[0]):
        return string.capitalize()
    else:
        print('This word does not start with a consonant')


# In[137]:


capitalize_first_letter_of_consonant('doh')


# In[77]:


'string'[0]


# In[95]:


is_consonant('string'[0])


# In[131]:


type('string'.capitalize())


# ## 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip

# In[144]:


def calculate_tip(gratuity, amount):
    return round(amount * gratuity, 2)


# In[145]:


calculate_tip(.18, 30)


# ## 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[146]:


def apply_discount(price, percentage):
    discount = price * percentage
    return price - discount


# In[148]:


apply_discount(39, .15)


# ## 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[120]:


def handle_commas(string):
    return int(string.replace(',', '_'))


# In[124]:


handle_commas('3,533,432')


# ## 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F)

# In[164]:


def get_letter_grade(number):
    if number <= 100 and number >= 88:
        return 'A'
    elif number <= 87 and number >= 80:
        return 'B'
    elif number <= 79 and number >= 67:
        return 'C'
    elif number <= 66 and number >= 60:
        return 'D'
    elif number <= 59 and number >= 0:
        return 'F'


# In[168]:


get_letter_grade(87)


# ## 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed

# In[171]:


def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    for s in string:
        if s in vowels:
            string = string.replace(s, "")
    return string


# In[175]:


remove_vowels('the string does not exist')


# ## 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#     - Name will become name
#     - First Name will become first_name
#     - % Completed will become completed

# In[201]:


string = '   brand marz '
print(string)
if string[0] == ' ':
    string = string.replace(string[0], '')
    
for s in string[1:-1]:
        if s == ' ':
            string = string[1:-1].replace(' ', '_')

if string[-1] == ' ':
    string = string[-1].replace(string[-1], '')
    
print(string)


# In[177]:


def normalize_name(string):
    for s in string[1:-1]:
        if s == ' ':
            string = string[1:-1].replace(' ', '_')
    
    if string[0] == ' ':
        string = string.replace(string[0], '')
    
    if string[-1] == ' ':
        string = string.replace(string[-1], '')
    
    string = string.lower()
    
    return string


# In[181]:


# leading and trailing whitespace should be removed
if string[0] == ' ':
    string = string.replace(' ', '')
    
if string[-1] == ' ':
    string = string.replace(' ', '')


# In[ ]:


# spaces should be replaced with underscores
for s in string[1:-1]:
        if s == ' ':
            string = string.replace(' ', '_')


# In[ ]:


# anything that is not a valid python identifier should be removed

# - cannot start with a number
while string[0].isdigit():
        string = string.replace(string[0], '')
        continue
    
# - cannot use keywords
import keyword
if string in keyword.kwlist:
    return print('Cannot use keyword')


# - cannot contain special symbols like (!, @, #, $, %, etc.)
special_char = '[@!#$%^&*()<>?/\|}{~:]'
for s in string:
    if s in special_char:
        string = string.replace(s, '')


# In[ ]:


# everything should be lowercase
string = string.lower()


# ## 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[117]:


# define a function that will accept a single parameter (list of numbers), 
# and return an updated list, the cumulative sum
# cumulative meaning the current total at each stage
def cumulative_sum(num_list):
    # create an empty list called csum: place holder for new values to be returned
    csum = []
    # set a variable called count to 0 to be updated at each iteration of the 
    # upcoming for loop
    count = 0
    # use a for loop to iterate through each number in original list
    for number in num_list:
        #the count will be updated to sum the count plus the current number in the list
        count = number + count
        # the final stage is using .append() to add the new count(cumulative sum) 
        # to the new list
        csum.append(count)
        # with a for loop this repeats until each number in the list has been processed
        # the new list is then returned with the updated numbers, the cumulative sum
    return csum


# In[118]:


cumulative_sum([1, 1, 1])


# In[300]:


cumulative_sum([1, 2, 3, 4])


# In[203]:


cumulative_sum([])


# In[ ]:


# use asserts in the begining to eliminate garbage user input

