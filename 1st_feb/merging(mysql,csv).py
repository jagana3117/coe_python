import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# Step 1: Create a SQLAlchemy engine to connect to the MySQL database
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/cvr')

# Step 2: Use the engine to read the SQL query into a DataFrame
sql_query = "SELECT * FROM energy_usage;"

# Load data from SQL into a DataFrame using the SQLAlchemy engine
energy_df = pd.read_sql(sql_query, engine)

# Step 3: Read data from a CSV file into a DataFrame
appliance_df = pd.read_csv('energy_con.csv')

# Step 4: Merge the two DataFrames on 'household_id'
merged_df = pd.merge(energy_df, appliance_df, on='household_id', how='outer')

# Step 5: Print the merged DataFrame
print("\nMerged DataFrame:")
pd.set_option('display.max_columns', None)#display all columns
pd.set_option('display.width', None)  # Prevent line wrapping
pd.set_option('display.max_colwidth', None)#prevent  column width
print(merged_df)
print(merged_df['household_id'].dtypes)

import pandas as pd
from sqlalchemy import create_engine

# Step 1: Create a SQLAlchemy engine to connect to the MySQL database
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/cvr')

# Step 2: Use the engine to read the SQL query into a DataFrame
sql_query = "SELECT * FROM energy_usage;"

# Load data from SQL into a DataFrame using the SQLAlchemy engine
energy_df = pd.read_sql(sql_query, engine)

# Step 3: Read data from a CSV file into a DataFrame
appliance_df = pd.read_csv('energy_con.csv')

# Step 4: Merge the two DataFrames on 'household_id'
merged_df = pd.merge(energy_df, appliance_df, on='household_id', how='outer')

# Step 5: Print the merged DataFrame
print("\nMerged DataFrame:")
pd.set_option('display.max_columns', None)#display all columns
pd.set_option('display.width', None)  # Prevent line wrapping
pd.set_option('display.max_colwidth', None)#prevent  column width
print(merged_df)

print(merged_df['household_id'].dtypes)
print('before convertion')
print(merged_df['household_id'].memory_usage(deep=True))
print('after converstion')
merged_df['household_id']=merged_df['household_id'].astype(np.int16)
print(merged_df['household_id'].memory_usage(deep=True))
print(merged_df['household_id'].dtypes)
print(merged_df.dtypes)
merged_df['date']=merged_df['date'].astype('category')
print('object to category')
print(merged_df['date'].dtypes)
