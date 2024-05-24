# STEP-BY-STEP PROCESS
1. EXTRACT the data from Kaggle API
2. TRANSFORM or "clean" the data in python
3. LOAD the data into SQL Server 

EXTRACT
*Extract the data from kaggle.com and setup the transformation process in Jupyter Notebook*
Go to Kaggle.com -- Profile -- Settings -- Create New Token (A kaggle.json file should be downloaded)
Copy the downloaded kaggle.json file and place it in: This PC -- Windows -- Users -- DaSean -- kaggle
Download Anaconda Navigator and then Lauch Juoyter Notebook
Go to Documents -- Create a Folder named "SQL + Python" -- In that folder create a New Python 3 file

TRANSFORM
*Clean the data by changing data types, renaming columns, and adding new columns with different calculations*
Refer to the "CLEANING THE DATA (1-8)" section in the JUPYTER-PYTHON-CODE

LOAD
*load the data from the csv file to MySQL Server*
Refer to the "CONNECT TO THE DATA (1-3)" section from the "JUPYTER-PYTHON-CODE" in order to first connect the MySQL Server
The refer to the "LOAD THE DATA INTO THE DATABASE (1-2)" section in the "JUPYTER-PYTHON-CODE" to load the data in the MySQL Server
