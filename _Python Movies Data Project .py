#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.pyplot import figure
get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)
df = pd.read_csv('movies.csv')
df.head()


# In[1]:


for col in df.columns:
    pct_miising= np.mean(df[col].isnull())
    print('{}-{}%'.format(col, pct_miising))


# In[13]:


df.dtypes


# In[24]:


df['yearcorrect']=df['released'].astype(str).str[:4]
df


# In[25]:


df=df.sort_values(by=['gross'],inplace=False,ascending=False)


# In[27]:


pd.set_option('display_max_rows',None)


# In[35]:


df['company'].drop_duplicates().sort_values(ascending=False)


# In[33]:


df.drop_duplicates()


# In[ ]:





# In[32]:


df.drop_duplicates()


# In[36]:


df


# In[40]:


df.dtypes


# In[45]:


#Scatterplot with budget vs gross
plt.scatter(x=df['budget'],y=df['gross'])

plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross of Earnings')
plt.ylabel('Budget of Films')

plt.show()


# In[43]:


df.head()


# In[52]:


#plot budget vs gross using seaborn 
sns.regplot(x='budget',y='gross',data=df,scatter_kws={"color":"black"},line_kws={"color":"purple"})


# In[56]:


df.corr(method='kendall')


# In[57]:


#high correlations between Budget and Gross


# In[60]:


correlation_matrix=df.corr(method='pearson')
sns.heatmap(correlation_matrix,annot=True)
plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movies Features')
plt.ylabel('Movies Features')
plt.show()


# In[61]:


#looking at company
df.head()


# In[64]:


df_numerized=df
for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype=='object'):
        df_numerized[col_name]=df_numerized[col_name].astype('category')
        df_numerized[col_name]=df_numerized[col_name].cat.codes
        
df_numerized


# In[65]:


df


# In[66]:


correlation_matrix=df_numerized.corr(method='pearson')
sns.heatmap(correlation_matrix,annot=True)
plt.title('Correlation Matrix for Numeric Features')
plt.xlabel('Movies Features')
plt.ylabel('Movies Features')
plt.show()


# In[67]:


df_numerized.corr()


# In[68]:


correlation_mat=df_numerized.corr()
corr_pairs=correlation_mat.unstack()
corr_pairs


# In[69]:


sorted_pairs=corr_pairs.sort_values()
sorted_pairs


# In[70]:


high_corr=sorted_pairs[(sorted_pairs)>0.5]
high_corr


# In[ ]:




