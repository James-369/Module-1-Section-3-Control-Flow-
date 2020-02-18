#!/usr/bin/env python
# coding: utf-8

# In[2]:


List = list([2,3,4,5])


# In[1]:


import numpy as np
import pandas as pd 


# In[2]:


slices_of_pie = 6
slices_eaten = 0
for slice in range(slices_of_pie):
    print('Another Slice Eaten')
    slices_eaten += 1 
    print('Now Eaten {} slices!'.format(slices_eaten))


# In[4]:


slices_of_pie = 6 
slices_eaten = 0
while slices_eaten < slices_of_pie:
    print('Another Slice Eaten')
    slices_eaten += 1
    print('Now Eaten {} Slices!'.format(slices_eaten))


# In[8]:


time_for_breakfast = 1468 
number_of_cooked_pancakes = 0
while time_for_breakfast > 0 and number_of_cooked_pancakes < 5:
    # make a pancake
    time_for_breakfast -= sum([5,27,5,27,5]) # Add one to pan, slide 1, filp, slide 2, remove 
    number_of_cooked_pancakes += 1
time_for_breakfast


# In[11]:


line_of_hungry_patrons = list(range(0,30))
fed_patrons = []
for patron in line_of_hungry_patrons:
    if patron % 2 == 0:
        line_of_hungry_patrons.remove(patron)
        fed_patrons.append(patron)
print('Those hungry : ', line_of_hungry_patrons)
print('Those fed : ', fed_patrons)
        


# In[12]:


people = [
    {'name': "Daniel", 'age': 29, 'job': "Engineer", 'pet': "Cat", 'pet_name': "Gato"}, 
    {'name': "Katie", 'age': 30, 'job': "Teacher", 'pet': "Dog", 'pet_name': "Frank"},
    {'name': "Owen", 'age': 26, 'job': "Sales person", 'pet': "Cat", 'pet_name': "Cosmo"},
    {'name': "Josh", 'age': 22, 'job': "Student", 'pet': "Cat", 'pet_name': "Chat"},
    {'name': "Estelle", 'age': 35, 'job': "French Diplomat", 'pet': "Dog", 'pet_name': "Gabby"},
    {'name': "Gustav", 'age': 24, 'job': "Brewer", 'pet': "Dog", 'pet_name': "Helen"}
]


# In[14]:


first_dog_person = 0
iteration_count = 0
for person in people:
    iteration_count += 1 
    if person['pet'] == 'Dog':
        print('{} has a dog! Had to check the {} records to find dog owner'.format(person['name'], iteration_count))


# In[ ]:




