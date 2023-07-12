import pandas as pd
from sodapy import Socrata
import plotly.express as px
import nbformat
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from datetime import *
import statsmodels.api as sm
import seaborn as sns
import plotly.io as pio
import dash_bootstrap_components as dbc
import numpy as np
from sklearn.linear_model import LinearRegression

# https://dev.socrata.com/foundry/data.cityofnewyork.us/k46n-sa2m
client = Socrata("data.cityofnewyork.us", None)
results = client.get("k46n-sa2m",limit=80000)

# Convert to pandas DataFrame
dhs_daily_df = pd.DataFrame.from_records(results)

#converting to type numeric
cols = dhs_daily_df.columns.drop('date_of_census')
dhs_daily_df[cols] = dhs_daily_df[cols].apply(pd.to_numeric)

dhs_daily_df['date_of_census'] = pd.to_datetime(dhs_daily_df['date_of_census'])

# Create a list to store the new column names
new_columns = []

# Iterate over each column
for column in dhs_daily_df.columns:
    if column != 'total_individuals_in_shelter' and column != 'date_of_census':
        # Generate the new column name with the prefix "perc_" followed by the original column name
        new_column = 'perc_' + column
        
        # Divide the values in the current column by the values in the 'total_individuals_in_shelter' column
        new_values = ((dhs_daily_df[column].astype(float) / dhs_daily_df['total_individuals_in_shelter'].astype(float))*100).round(2)
        
        # Append the new column to the DataFrame
        dhs_daily_df[new_column] = new_values
        
        # Append the new column name to the list
        new_columns.append(new_column)

# convert to monthly & quarterly
# Set the 'date' column as the index
dhs_daily_df.set_index('date_of_census', inplace=True)

# Resample to monthly average data
monthly_avg_df = dhs_daily_df.resample('M').mean()

# Resample to quarterly average data
quarterly_avg_df = dhs_daily_df.resample('Q').mean()

# Resample to quarterly average data
yearly_avg_df = dhs_daily_df.resample('Y').mean()

#dhs_daily_df.reset_index(inplace=True)
#monthly_avg_df.reset_index(inplace=True)
#quarterly_avg_df.reset_index(inplace=True)
#yearly_avg_df.reset_index(inplace=True)




