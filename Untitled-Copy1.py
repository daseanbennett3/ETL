#!/usr/bin/env python
# coding: utf-8

# In[1]:
#CLEANING THE DATA (1-7)
#1 connect to kaggle to download from it
get_ipython().system('pip install kaggle')
import kaggle

# In[2]:
#2 Download the orders.csv file from https://www.kaggle.com/datasets/ankitbansal06/retail-orders
get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')

# In[3]:
#3 "Extract all" from the orders.csv.zip
import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall()
zip_ref.close()

# In[11]:
#Read data from the file
import pandas as pd
df = pd.read_csv('orders.csv')
#Display the first 20 rows
df.head(20)
#Disply the unique/distinct values in the Ship Mode column
df['Ship Mode'].unique()
#3 Turn any value with "Not Available" and "unknown" to null values
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# In[12]:


#4 Rename columns names by replacing "ABC" with "abc" AND " " with "_" (convert them to a string object)
#Slower/More precise way of doing it
df.rename(columns={'Order Id':'order_id', 'City':'city'})
#Faster/Easier way of doing it
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(3)


# In[14]:


#5 Create a new column named "discount" that multiples "list_price" by "discount_price" and divide by 100 (or multiple by .01)
df['discount']=df['list_price']*df['discount_percent']*.01
# Create a new column named "sale_price" that subtracts "discount" from "List_price"
df['sale_price']= df['list_price']-df['discount']
# Create a new column named "Profit" that subtracts "cost_price" from "sale_price"
df['profit']=df['sale_price']-df['cost_price']
# Display the entire orders.csv file
df


# In[18]:


#6 convert order date from object data type to datetime
#df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")

# Display the data types of each column in the orders.csv file (df stands for Data Frames)
df.dtypes


# In[22]:


#7 Drop the columns "cost_price," "list price," and "discount percent" permanetly
df.drop(columns=['cost_price','list_price','discount_percent'],inplace=True)

#To drop the columns temporarily, don't have the "inplace=True" at the end


# In[27]:


df.head(3)


# In[24]:


#CONNECT TO THE DATA
#import SQL Alchemy because its better Pythonicaly than SQL
import sqlalchemy as sal
#Create the connection. Use the name "DESKTOP-3MQELCQ" which was found in Microsoft SQL Server Management Studio
#Use "master" because that is the main database
#Use "ODBC+DRIVER+17+FOR+SQL+SERVER" as the driver which was found by searching 'ODBC Data Sources (32-bit)''
engine = sal.create_engine('mssql://DESKTOP-3MQELCQ/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
#Connect to the 
conn=engine.connect()


# In[25]:


#LOAD THE DATA INTO THE DATABASE
#Use to_sql to load this table named "df_orders" to sql
#Set the "index" equal to "False" so the file isnt indexed starting at 0, but rather the order_id
#Con (connect) to the connection created in the previous code
#"Append" to the table rather than "replace" so you are just adding to it
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')


# In[ ]:
#Replace the data types of the data (in SQL):
#1. DROP TABLE df_orders
#2. CREATE TABLE df_orders
      [order_id] INT PRIMARY KEY,
      [order_date] DATE,
      [ship_mode] VARCHAR(20),
      ...
#3In python, run:
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')
#4 SELECT * FROM df_orders (refresh if needed)


