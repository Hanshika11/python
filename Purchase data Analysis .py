#!/usr/bin/env python
# coding: utf-8

# # Import libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # 1. Data Exploration and Cleaning:
# 
# 

# In[2]:


df = pd.read_csv('purchase_data.csv')
df


# In[4]:


# View the first few rows of the dataset
df.head()


# In[5]:


# Summary information about the dataset, including missing values
df.info()


# In[6]:


# Descriptive statistics of the dataset
df.describe()


# In[7]:


#Shape of the dataset
print(df.shape)


# # 2 User Behavior Analysis
# 
# 

# In[11]:


# Most visited Products
most_visited_products = df['Product_ID'].value_counts().nlargest(10)
print("Top 10 most visited products:")
print(most_visited_products)


# In[20]:


plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
most_visited_pages.plot(kind='bar', color='green')
plt.title('Top 10 Most Visited Products')
plt.ylabel('Number of Visits')


# # 3. Purchase Analysis
# 

# In[34]:


top_selling_products = df.groupby('Product_ID')['Purchase_ID'].count().nlargest(10)
print("Top 10 Selling Products:")
print(top_selling_products)


# In[41]:


# Calculate the overall conversion rate
overall_conversion_rate = df['Purchase_ID'].sum() / df['Transaction_Amount'].sum()
print("Overall Conversion Rate:", overall_conversion_rate)


# In[42]:


top_selling_products = df.groupby('Product_ID')['Purchase_ID'].sum().nlargest(10)
print("Top 10 Selling Products:")
print(top_selling_products)


# In[44]:


top_selling_categories = df.groupby('Product_ID')['Purchase_ID'].sum().nlargest(5)
print("Top 5 Selling Product Categories:")
print(top_selling_categories)


# In[ ]:




