#PYTHON CODE USING JUPYTER NOTEBOOKS
--
# In[1]:
#CLEANING THE DATA (1-8)
#1. connect to Kaggle to download from it
get_ipython().system('pip install kaggle')
import kaggle

# In[2]:
#1. Download the orders.csv file from https://www.kaggle.com/datasets/ankitbansal06/retail-orders to your local system
# The file will be placed in your "SQL + Python" file
get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')

# In[3]:
#1. "Extract all" from the orders.csv.zip
import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall()
zip_ref.close()

# In[4]:
#1. Read data from the file
import pandas as pd
df = pd.read_csv('orders.csv')
#2. Display the first 20 rows
df.head(20)
#3. Disply the unique/distinct values in the Ship Mode column
df['Ship Mode'].unique()
#4. Turn any value with "Not Available" and "unknown" to null values
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()

# In[5]:
#1. Rename columns names by replacing "ABC" with "abc" AND " " with "_" (convert them to a string object)
#Slower/More precise way of doing it
df.rename(columns={'Order Id':'order_id', 'City':'city'})
#Faster/Easier way of doing it
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(3)

# In[6]:
#1. Create a new column named "discount" that multiples "list_price" by "discount_price" and divide by 100 (or multiple by .01)
df['discount']=df['list_price']*df['discount_percent']*.01
#2. Create a new column named "sale_price" that subtracts "discount" from "List_price"
df['sale_price']= df['list_price']-df['discount']
#3. Create a new column named "Profit" that subtracts "cost_price" from "sale_price"
df['profit']=df['sale_price']-df['cost_price']
#4. Display the entire orders.csv file
df

# In[7]:
#1. Convert order date from the 'object' data type to datetime
#df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
#2. Display the data types of each column in the orders.csv file (df stands for Data Frames)
df.dtypes

# In[8]:
#8. Drop the columns "cost_price," "list price," and "discount percent" permanetly
df.drop(columns=['cost_price','list_price','discount_percent'],inplace=True)

# To drop the columns temporarily, don't have the "inplace=True" at the end
# To only display 3 rows:
df.head(3)

--
# In[1]:
#CONNECT TO THE DATA (1-3)
#1. Import SQL Alchemy because it's better Pythonicaly than SQL
import sqlalchemy as sal

# In[2]:
#1. Create the connection. Use the name "DESKTOP-3MQELCQ" which was found in Microsoft SQL Server Management Studio
#       Use "master" because that is the main database we will be using
#       Use "ODBC+DRIVER+17+FOR+SQL+SERVER" as the "driver" which was found by searching 'ODBC Data Sources (32-bit)''
engine = sal.create_engine('mssql://DESKTOP-3MQELCQ/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')

# In[3]:
#1. Connect to the database
conn=engine.connect()

--
# In[1]:
#LOAD THE DATA INTO THE DATABASE (1-2)
#1. Use to_sql to load this table named "df_orders" to sql
#      Set the "index" equal to "False" so the file isnt indexed starting at 0, but rather the order_id
#      Con (connect) to the connection created in the previous code
#      "Append" to the table rather than "replace" so you are just adding to it
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')

# In[2]:
#1. Replace the data types of the data (in MySQL Server):
#1. DROP TABLE df_orders
#2. CREATE TABLE df_orders
      [order_id] INT PRIMARY KEY,
      [order_date] DATE,
      [ship_mode] VARCHAR(20),
      ...
#3. In Juypter Notebook, run:
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')
#4. In MySQL Server, run: 
# SELECT * FROM df_orders (refresh if needed)

# IGNORE THESE
#!/usr/bin/env python
# coding: utf-8
