#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[142]:


import csv


# In[143]:


insurance = []


# In[144]:


with open('insurance.csv', newline='') as csvfile:
    holder = csv.DictReader(csvfile)
    for row in holder:
        a = {}
        a['age'] = int(row['age'])
        if row['sex'] == 'female':
            sex = 1
        else:
            sex = 0
        a['sex'] = sex
        a['bmi'] = float(row['bmi'])
        a['children'] = int(row['children'])
        if row['smoker'] == 'yes':
            smoker = 1
        else:
            smoker = 0
        a['smoker'] = smoker
        if row['region'] == 'northeast':
            region = 0
        elif row['region'] == 'northwest':
            region = 1
        elif row['region'] == 'southwest':
            region = 2
        else:
            region = 3
        a['region'] = region
        a['charges'] = float(row['charges'])
        insurance.append(a)


# In[145]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np


# In[146]:


age_bmi = []
for item in insurance:
    temp = []
    temp.append(item['age'])
    temp.append(item['bmi'])
    age_bmi.append(temp)


# In[147]:


for item in age_bmi:
    x = item[0]
    y = item[1]
    plt.plot(x, y, 'o', color='black');


# In[148]:


class Person:
    def __init__(self, age, sex, bmi, children, smoker, region, charges):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.charges = charges
    def __repr__(self):
        rep = str(self.age) + '_' + str(self.sex)
        return rep


# In[149]:


John = Person(5, 0, 22, 3, 0, 3, 14000)


# In[150]:


def smoker_sort(dictionary):
    M_smokers_northeast = 0
    F_smokers_northeast = 0
    M_smokers_northwest = 0
    F_smokers_northwest = 0
    M_smokers_southwest = 0
    F_smokers_southwest = 0
    M_smokers_southeast = 0
    F_smokers_southeast = 0
    for item in dictionary:
        if item['region'] == 0:
            if item['sex'] == 0:
                if item['smoker'] == 1:
                    M_smokers_northeast += 1
            else:
                if item['smoker'] == 1:
                    F_smokers_northeast += 1
        elif item['region'] == 1:
            if item['sex'] == 0:
                if item['smoker'] == 1:
                    M_smokers_northwest += 1
            else:
                if item['smoker'] == 1:
                    F_smokers_northwest += 1
        elif item['region'] == 2:
            if item['sex'] == 0:
                if item['smoker'] == 1:
                    M_smokers_southwest += 1
            else:
                if item['smoker'] == 1:
                    F_smokers_southwest += 1
        else:
            if item['sex'] == 0:
                if item['smoker'] == 1:
                    M_smokers_southeast += 1
            else:
                if item['smoker'] == 1:
                    F_smokers_southeast += 1
    return [M_smokers_northeast, F_smokers_northeast, M_smokers_northwest, F_smokers_northwest, M_smokers_southwest, F_smokers_southwest, M_smokers_southeast, F_smokers_southeast]
    
smoker_data = smoker_sort(insurance)


# In[151]:


def region_population(dictionary):
    M_northeast = 0
    F_northeast = 0
    M_northwest = 0
    F_northwest = 0
    M_southwest = 0
    F_southwest = 0
    M_southeast = 0
    F_southeast = 0
    for item in dictionary:
        if item['region'] == 0:
            if item['sex'] == 0:
                M_northeast += 1
            else:
                F_northeast += 1
        elif item['region'] == 1:
            if item['sex'] == 0:
                M_northwest += 1
            else:
                F_northwest += 1
        elif item['region'] == 2:
            if item['sex'] == 0:
                M_southwest += 1
            else:
                F_southwest += 1
        else:
            if item['sex'] == 0:
                M_southeast += 1
            else:
                F_southeast += 1
    return [M_northeast, F_northeast, M_northwest, F_northwest, M_southwest, F_southwest, M_southeast, F_southeast]
    
population_data = region_population(insurance)


# In[152]:


def smoker_percent(smokers, population):
    return [int(x/y*100) for x,y in zip(smokers,population)]

smoker_percent_data = smoker_percent(smoker_data, population_data)
print(smoker_percent_data)
