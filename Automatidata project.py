
# ** Automatidata project**
# Go Beyond the Numbers: Translate Data into Insights**

# You are the newest data professional in a fictional data consulting firm: Automatidata. The team is still early into the project, having only just completed an initial plan of action and some early Python coding work. 
# 
# Luana Rodriquez, the senior data analyst at Automatidata, is pleased with the work you have already completed and requests your assistance with some EDA and data visualization work for the New York City Taxi and Limousine Commission project (New York City TLC) to get a general understanding of what taxi ridership looks like. The management team is asking for a Python notebook showing data structuring and cleaning, as well as any matplotlib/seaborn visualizations plotted to help understand the data. At the very least, include a box plot of the ride durations and some time series plots, like a breakdown by quarter or month. 



# Import packages and libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset into dataframe
df = pd.read_csv("E:\Learner-facing C3 Automatidata dataset for Tableau project - 2017_Yellow_Taxi_Trip_Data_0002_sample.csv")

df.head()

df.size

df.describe()

df.info()

# Convert data columns to datetime
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
df.info()

# Create box plot of trip_distance
plt.figure(figsize =(10,2))
sns.boxplot(x=df["trip_distance"])

# Create histogram of trip_distance
plt.figure(figsize = (10,5))
sns.histplot(df['trip_distance'], bins = range(0,26,1))
plt.title('Trip Distance Histogram')

# Create box plot of total_amount
plt.figure(figsize = (10,2))
sns.boxplot(x=df['total_amount'], fliersize = 1)
plt.title('Total Amount')

# Create histogram of total_amount
plt.figure(figsize = (10,5))
sns.histplot(df['total_amount'],bins =range(-20, 120,5))
plt.title('Total Amount Histogram')

# Create box plot of tip_amount
plt.figure(figsize = (7,2))
sns.boxplot(x=df['tip_amount'], fliersize =1)
plt.title('Tip Amount')

# Create histogram of tip_amount
plt.figure(figsize = (10,5))
ax = sns.histplot(df['tip_amount'], bins = range(-5, 20, 1))
ax.set_xticks(range(0,21,2))
ax.set_xticklabels(range(0,21,2))
plt.title('TIp Amount histogram')

# Create histogram of tip_amount by vendor
plt.figure(figsize = (10,5))
ax = sns.histplot(data = df, x = df['tip_amount'], hue = df['VendorID'], bins = range(-5, 20, 1), multiple = 'stack',
            palette = 'pastel')
ax.set_xticks(range(-5, 20, 1))
plt.title('Tip Amount By Vendor')

# Create histogram of tip_amount by vendor for tips > $10 
tips_above_10 = df[df['tip_amount'] > 10]  
plt.figure(figsize = (10,5))
ax = sns.histplot(data = tips_above_10, x = 'tip_amount', hue = 'VendorID', multiple = 'stack',
                 bins = range(5, 60, 2), palette = 'pastel')
ax.set_xticks(range(5, 60, 5))
plt.title('Tip Amount more than $10')


# Examine the unique values in the `passenger_count` column.

df['passenger_count'].value_counts()


# Calculate mean tips by passenger_count
mean_tips_by_passenger_count = df.groupby('passenger_count').mean()[['tip_amount']]
mean_tips_by_passenger_count

# Create bar plot for mean tips by passenger count
data = mean_tips_by_passenger_count.tail(6)
plt.figure(figsize = (12,7))
ax = sns.barplot(data = data, x = data.index, y = 'tip_amount', palette = 'pastel')
ax.axhline(df['tip_amount'].mean(), ls = '--', color = 'green', label = 'Global Mean')
ax.legend()
plt.title('Mean tip amount by passenger count', fontsize=16);


# **Create month and day columns**

# Create a month column
df['month'] = df['tpep_pickup_datetime'].dt.month_name()

# Create a day column
df['day'] = df['tpep_pickup_datetime'].dt.day_name()


# **Plot total ride count by month**
# 
# Begin by calculating total ride count by month.

# Get total number of rides for each month
monthly_rides = df['month'].value_counts()

# Reorder the monthly ride list so months go in order
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
monthly_rides = monthly_rides.reindex(index = month_order)

# Show the index
monthly_rides.index

# Create a bar plot of total rides per month
plt.figure(figsize = (12, 7))
ax = sns.barplot( x= monthly_rides.index, y = monthly_rides)
ax.set_xticklabels(month_order)
plt.title('Ride Count By Month', fontsize = 16);


# **Plot total ride count by day**
# Repeat the above process, but now calculate the total rides by day of the week.

# Repeat the above process, this time for rides by day
day_rides = df['day'].value_counts()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']
day_rides = day_rides.reindex(index = day_order)
day_rides

# Create bar plot for ride count by day
plt.figure(figsize =(12, 7))
ax = sns.barplot(x = day_rides.index, y = day_rides)
ax.set_xticklabels(day_order)
plt.title('Ride Count By Day', fontsize = 16);


# **Plot total revenue by day of the week**
# Repeat the above process, but now calculate the total revenue by day of the week.


# Repeat the process, this time for total revenue by day
revenue_by_day = df.groupby('day').sum()[['total_amount']]
revenue_by_day = revenue_by_day.reindex(index = day_order)
revenue_by_day

# Create bar plot of total revenue by day
plt.figure(figsize =(12, 7))
ax = sns.barplot(x = revenue_by_day.index, y = revenue_by_day['total_amount'])
ax.set_xticklabels(day_order)
ax.set_ylabel('Revenue(USD)')
plt.title('Total Revenue By Day', fontsize = 16);


# Repeat the process, this time for total revenue by month
revenue_by_month = df.groupby('month').sum()[['total_amount']].reindex(index = month_order)
revenue_by_month


# Create a bar plot of total revenue by month
plt.figure(figsize = (12, 7))
ax = sns.barplot(x = revenue_by_month.index, y = revenue_by_month['total_amount'])
ax.set_xticklabels(month_order)
ax.set_ylabel('Revenue (USD)')
plt.title('Total Revenue By Month', fontsize = 16);


# **Plot mean trip distance by drop-off location**

# Get number of unique drop-off location IDs
df['DOLocationID'].nunique()

# Calculate the mean trip distance for each drop-off location
distance_dropoff = df.groupby('DOLocationID').mean()[['trip_distance']]

# Sort the results in descending order by mean trip distance
distance_dropoff = distance_dropoff.sort_values(by = 'trip_distance', ascending = True)
distance_dropoff

# Create a bar plot of mean trip distances by drop-off location in ascending order by distance
plt.figure(figsize = (12, 7))
ax = sns.barplot(x = distance_dropoff.index, y = distance_dropoff['trip_distance'], order=distance_dropoff.index)
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_ylabel('Trip Distance')
plt.title('Mean Trip distance by drop off location', fontsize = 16);


# Check if all drop-off locations are consecutively numbered
df['DOLocationID'].max() - len(set(df['DOLocationID']))


# To eliminate the spaces in the historgram that these missing numbers would create, sort the unique drop-off location values, then convert them to strings. This will make the histplot function display all bars directly next to each other. 

# DOLocationID column is numeric, so sort in ascending order
dropoff_sorted = df['DOLocationID'].sort_values()

# Convert to string
dropoff_sorted = dropoff_sorted.astype('str')

# Plot
plt.figure(figsize = (15, 5))
sns.histplot(data = dropoff_sorted, bins = range(0, 270, 1))
plt.xticks([])
plt.xlabel('Dropoff Locations')
plt.title('Histogram of rides by drop-off location', fontsize=16);
