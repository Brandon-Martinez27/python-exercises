#!/usr/bin/env python
# coding: utf-8

# ### 1. Conditional Basics

# #### a. prompt the user for a day of the week, print out whether the day is Monday or not

# In[1]:


valu = input("Enter day of the week: ") 
print(valu)


# In[2]:


if valu.lower() == 'monday':
    print("Today is Monday")
else:
    print("Today is not Monday")


# #### b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# In[3]:


valu2 = input("Enter day of the week: ") 
print(valu2)


# In[4]:


if valu2.lower() == 'saturday' or valu2.lower() == 'sunday':
    print("It's the freakin weekend!")
else:
    print("Back to work...")


# #### c. create variables and make up values for
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be
# #### write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[11]:


hours_per_week = 55
hourly_rate = 44

time_and_a_half = (hours_per_week - 40) * (hourly_rate * 1.5)

if hours_per_week > 40:
    paycheck = (hourly_rate * 40) + time_and_a_half
else:
    paycheck = hourly_rate * hours_per_week
print(paycheck)


# ### 2. Loop Basics

# a. While
# 
# - Create an integer variable i with a value of 5.
# - Create a while loop that runs so long as i is less than or equal to 15
# - Each loop iteration, output the current value of i, then increment i by one. 

# In[13]:


i = 5

while i <= 15:
    print(i)
    i += 1


# - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# - Alter your loop to count backwards by 5's from 100 to -10.
# - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

# In[14]:


i = 0
while i <= 100:
    print(i)
    i += 2
print("________________________")
i = 100
while i >= -5:
    print(i)
    i -= 5
print("________________________")    
i = 2
while i < 1_000_000:
    print(i)
    i = i**2


# - Write a loop that uses print to create the output shown below.

# In[15]:


i = 100
while i >= 5:
    print(i)
    i -= 5


# b. For Loops
# 
#     i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number

# In[18]:


inp = int(input("Enter a number: "))
for number in range(1,11):
    print(inp, "x", number, "=", inp * number)


#     ii. Create a for loop that uses print to create the output shown below.

# In[19]:


one_to_nine = list(range(1,10))
for n in one_to_nine:
    print(str(n)*n)
# I spent way too long on this problem! 
# I didn't know you could multiply a string by an integer.


# c. break and continue
# 
#     i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered

# ###### ALL conditions must be True (and)
# - i <= 50 # input is less than/ equal to 50
# - i >= 1 # input is greater than/equal to 1
# - i.isdigit() # input is has digits
# - i % 2 != 0 # input must be odd
# 
# ##### process
# - if all true then 'break' the loop
# - loop(while) the input command if one of conditons returns false
# - a while loop will stop when until condition is false
# - all true conditions must be reversed to keep running 

# ###### step 1(failed): first try (didn't account for invalid info)
inp = int(input("Enter an odd number between 1 and 50: "))
while inp > 50 or inp < 1 or inp % 2 == 0:
    inp = int(input("Enter an odd number between 1 and 50: "))
    continue
# ###### step 2: Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered
for n in range (1,51):
    if n == inp:
        print('Skipped', inp)
        continue
    if n % 2 != 0:
        print(n)
# In[82]:


# final code
while True:
    try:
        inp = int(input("Enter an odd number between 1 and 50: "))
        if inp <= 50 and inp >= 1 and inp % 2 != 0:
            break
        print('Read the prompt')
    except ValueError:
        print('Number please')
for n in range (1,51):
    if n == inp:
        print('Skipped', inp)
        continue
    if n % 2 != 0:
        print(n)


# d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[85]:


while True:
    try:
        inp = int(input("Enter a positive integer: "))
        if inp > 0 :
            break
        print('Read the prompt')
    except ValueError:
        print('Integer please')


# In[86]:


for n in range (inp+1):
    print(n)


# e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[92]:


while True:
    try:
        inp = int(input("Enter a positive integer: "))
        if inp > 0 :
            break
        print('Read the prompt')
    except ValueError:
        print('Integer please')


# In[93]:


while inp > 0:
    print(inp)
    inp -= 1


# ### 3. Fizzbuzz
# 
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# - Write a program that prints the numbers from 1 to 100.

# In[94]:


for n in range(1,101):
    print(n)


# - For multiples of three print "Fizz" instead of the number

# In[97]:


for n in range(1,101):
    if n % 3 ==0:
        print('Fizz')
        continue
    print(n) 


# - For the multiples of five print "Buzz".

# In[98]:


for n in range(1,101):
    if n % 5 == 0:
        print('Buzz')
        continue
    print(n)


# - For numbers which are multiples of both three and five print "FizzBuzz".

# In[100]:


for n in range(1,101):
    if n % 5 == 0 and n % 3 == 0:
        print('FizzBuzz')
        continue
    print(n)


# ### 4. Display a table of powers.

# - Prompt the user to enter an integer.
# - Display a table of squares and cubes from 1 to the value entered
# - Ask if the user wants to continue.
# - Assume that the user will enter valid data.
# - Only continue if the user agrees to.

# ###### step 1: prompt user to enter integer
while True:
    try:
        inp = int(input("Enter an integer: "))
        break
    except ValueError:
        print('Integer please')
# ###### step 2: display a table of squares & cubes from 1 to entered number
for x in range(1,inp+1):   
    print(x, x*2, x*3)  
# ###### step 3: ask if user wants to continue (assume valid data)
inp = input("Would you like to continue: ")
if inp.lower() == 'yes':
    continue
elif inp.lower() == 'no':
    break
# In[32]:


# final code
while True:
    try:
        inp = int(input("Enter an integer: "))
    except ValueError:
        print('Integer please')
    for x in range(1,inp+1):   
        print(x, x*2, x*3)
    inp = input("Would you like to continue: ")
    if inp.lower() == 'yes':
        continue
    elif inp.lower() == 'no':
        break


# ### 5. Convert given number grades into letter grades.
# 
# - Prompt the user for a numerical grade from 0 to 100.
# - Display the corresponding letter grade.
# - Prompt the user to continue.
# - Assume that the user will enter valid integers for the grades.
# - The application should only continue if the user agrees to.

# ###### step 1: prompt user for grade from 1 to 100
while True:
    try:
        inp = int(input("Enter your grade: "))
        if inp >= 100 and inp <= 0: #swap for step 2
                                    #insert step 3
            break
        print('Read the prompt')
    except ValueError:
        print('Number please')
# ###### step 2: Displays letter grade (based on response)
if inp <= 100 and inp >= 88:
    print('A')
elif inp <= 87 and inp >= 80:
    print('B')
elif inp <= 79 and inp >= 67:
    print('C')
elif inp <= 66 and inp >= 60:
    print('D')
elif inp <= 59 and inp >= 0:
    print('F')
# ###### step 3: prompts user to continue
inp = input("Would you like to continue: ")
if inp.lower() == 'yes':
    continue
elif inp.lower() == 'no':
    break
# In[ ]:


# final code
while True:
    try:
        inp = int(input("Enter your grade: "))
        if inp <= 100 and inp >= 88:
            print('A')
        elif inp <= 87 and inp >= 80:
            print('B')
        elif inp <= 79 and inp >= 67:
            print('C')
        elif inp <= 66 and inp >= 60:
            print('D')
        elif inp <= 59 and inp >= 0:
            print('F')
        inp = input("Would you like to continue: ")
        if inp.lower() == 'yes':
            continue
        elif inp.lower() == 'no':
            break
        print('What was that?')
    except ValueError:
        print('Number please')


# #### Bonus
# 
# - Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# In[ ]:


while True:
    try:
        inp = int(input("Enter your grade: "))
        if inp <= 100 and inp >= 97:
            print('A+')
        elif inp <= 96 and inp >= 92:
            print('A')
        elif inp <= 91 and inp >= 88:
            print('A-')
        elif inp <= 87 and inp >= 85:
            print('B+')
        elif inp <= 84 and inp >= 83:
            print('B')
        elif inp <= 82 and inp >= 80:
            print('B-')
        elif inp <= 79 and inp >= 76:
            print('C+')
        elif inp <= 75 and inp >= 71:
            print('C')
        elif inp <= 70 and inp >= 67:
            print('C-')
        elif inp <= 66 and inp >= 65:
            print('D+')
        elif inp <= 64 and inp >= 62:
            print('D')
        elif inp <= 61 and inp >= 60:
            print('D-')
        elif inp <= 59 and inp >= 0:
            print('F')
        inp = input("Would you like to continue: ")
        if inp.lower() == 'yes':
            continue
        elif inp.lower() == 'no':
            break
        print('What was that?')
    except ValueError:
        print('Number please')


# ### 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# 
#     a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[71]:


# list of dictionaries, books I've read
books = [
    {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "genre": "Spiritual"
    },
    {
       "title": "Waking Up",
        "author": "Sam Harris",
        "genre": "Spiritual" 
        
    },
    {
       "title": "Total Money Makeover",
        "author": "Dave Ramsey",
        "genre": "Finance" 
        
    },
    {
       "title": "I Will Teach You to be Rich",
        "author": "Ramit Sethi",
        "genre": "Finance" ,
        
    },
    {
       "title": "The House of the Scorpion",
        "author": "Nancy Farmer",
        "genre": "Fiction" 
        
    },
    {
       "title": "Ender's Game",
        "author": "Orson Scott Card",
        "genre": "Fiction" 
        
    },
    {
       "title": "Essentialism",
        "author": "Greg Mckeown",
        "genre": "Self-help" 
        
    },
    {
       "title": "The Four Agreements",
        "author": "Eckhart Tolle",
        "genre": "Self-Help" 
        
    }
]


# In[79]:


inp = input("Enter a genre: ")
for book in books:
    if inp.lower() == book["genre"].lower():
        print(book["title"])


# In[ ]:




