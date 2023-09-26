#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the libraries
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None


# In[2]:


# Read in the data
df = pd.read_excel('EMotorsMainData.xlsx')


# In[3]:


df


# In[4]:


# Check for missing data
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[5]:


# Check for the datatypes
print(df.dtypes)


# In[6]:


# Check for outliers
df.boxplot(column=['Quantity'])


# In[7]:


# Check for outliers
df.boxplot(column=['Amount'])


# In[8]:


# Drop duplicates

df.drop_duplicates()


# In[9]:


# Check correlation between Sales_Price and Amount

sns.regplot(x="Sales_Price", y="Amount", data=df)


# In[10]:


# Check correlation matrix between all numeric columns

df.corr(method='pearson')


# In[11]:


df.corr(method='kendall')


# In[12]:


df.corr(method='spearman')


# In[13]:


correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Performance")

plt.ylabel("Performance")

plt.show()


# In[14]:


corr_pairs = correlation_matrix.unstack()

print(corr_pairs)


# In[15]:


sorted_pairs = corr_pairs.sort_values(kind="quicksort")

print(sorted_pairs)


# In[16]:


strong_pairs = sorted_pairs[abs(sorted_pairs) > 0.5]

print(strong_pairs)


# In[17]:


# Looking at the top products by gross amount

ProductTotal = df.groupby('Product_Category')[["Amount"]].sum()

ProductTotalSorted = ProductTotal.sort_values('Amount', ascending = False)[:15]

ProductTotalSorted = ProductTotalSorted['Amount'].astype('int64') 

ProductTotalSorted


# In[18]:


# Top products grouped by year

TopProduct = df.groupby(['Product_Category', 'Year'])[["Amount"]].sum()
TopProductSorted = TopProduct.sort_values('Amount', ascending = False)[:20]
TopProductSorted = TopProductSorted['Amount'].astype('int64') 
TopProductSorted


# In[ ]:




