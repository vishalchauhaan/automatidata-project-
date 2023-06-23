#!/usr/bin/env python
# coding: utf-8

# # **Course 3 Automatidata project**
# **Course 3 - Go Beyond the Numbers: Translate Data into Insights**

# You are the newest data professional in a fictional data consulting firm: Automatidata. The team is still early into the project, having only just completed an initial plan of action and some early Python coding work. 
# 
# Luana Rodriquez, the senior data analyst at Automatidata, is pleased with the work you have already completed and requests your assistance with some EDA and data visualization work for the New York City Taxi and Limousine Commission project (New York City TLC) to get a general understanding of what taxi ridership looks like. The management team is asking for a Python notebook showing data structuring and cleaning, as well as any matplotlib/seaborn visualizations plotted to help understand the data. At the very least, include a box plot of the ride durations and some time series plots, like a breakdown by quarter or month. 
# 
# Additionally, the management team has recently asked all EDA to include Tableau visualizations. For this taxi data, create a Tableau dashboard showing a New York City map of taxi/limo trips by month. Make sure it is easy to understand to someone who isn’t data savvy, and remember that the assistant director at the New York City TLC is a person with visual impairments.
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions.

# # Course 3 End-of-course project: Exploratory data analysis
# 
# In this activity, you will examine data provided and prepare it for analysis. You will also design a professional data visualization that tells a story, and will help data-driven decisions for business needs. 
# 
# Please note that the Tableau visualization activity is optional, and will not affect your completion of the course. Completing the Tableau activity will help you practice planning out and plotting a data visualization based on a specific business need. The structure of this activity is designed to emulate the proposals you will likely be assigned in your career as a data professional. Completing this activity will help prepare you for those career moments.
# 
# **The purpose** of this project is to conduct exploratory data analysis on a provided data set. Your mission is to continue the investigation you began in C2 and perform further EDA on this data with the aim of learning more about the variables. 
#   
# **The goal** is to clean data set and create a visualization.
# <br/>  
# *This activity has 4 parts:*
# 
# **Part 1:** Imports, links, and loading
# 
# **Part 2:** Data Exploration
# *   Data cleaning
# 
# 
# **Part 3:** Building visualizations
# 
# **Part 4:** Evaluate and share results
# 
# <br/> 
# Follow the instructions and answer the questions below to complete the activity. Then, you will complete an Executive Summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work. 
# 
# 

# # **Visualize a story in Tableau and Python**

# # **PACE stages** 
# 
# 
# <img src="images/Pace.png" width="100" height="100" align=left>
# 
#    *        [Plan](#scrollTo=psz51YkZVwtN&line=3&uniqifier=1)
#    *        [Analyze](#scrollTo=mA7Mz_SnI8km&line=4&uniqifier=1)
#    *        [Construct](#scrollTo=Lca9c8XON8lc&line=2&uniqifier=1)
#    *        [Execute](#scrollTo=401PgchTPr4E&line=2&uniqifier=1)

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## PACE: Plan 
# 
# In this stage, consider the following questions where applicable to complete your code response:
# 1. Identify any outliers: 
# 
# 
# *   What methods are best for identifying outliers?
# *   How do you make the decision to keep or exclude outliers from any future models?
# 
# 

# ==> ENTER YOUR RESPONSE HERE

# ### Task 1. Imports, links, and loading
# Go to Tableau Public
# The following link will help you complete this activity. Keep Tableau Public open as you proceed to the next steps. 
# 
# Link to supporting materials: 
# Tableau Public: https://public.tableau.com/s/ 
# 
# For EDA of the data, import the data and packages that would be most helpful, such as pandas, numpy and matplotlib. 
# 

# In[1]:


# Import packages and libraries
#==>
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[48]:


# Load dataset into dataframe
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')


# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## PACE: Analyze 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### Task 2a. Data exploration and cleaning
# 
# Decide which columns are applicable
# 
# The first step is to assess your data. Check the Data Source page on Tableau Public to get a sense of the size, shape and makeup of the data set. Then answer these questions to yourself: 
# 
# Given our scenario, which data columns are most applicable? 
# Which data columns can I eliminate, knowing they won’t solve our problem scenario? 
# 
# Consider functions that help you understand and structure the data. 
# 
# *    head()
# *    describe()
# *    info()
# *    groupby()
# *    sortby()
# 
# What do you do about missing data (if any)? 
# 
# Are there data outliers? What are they and how might you handle them? 
# 
# What do the distributions of your variables tell you about the question you're asking or the problem you're trying to solve?
# 
# 
# 

# ==> ENTER YOUR RESPONSE HERE

# Start by discovering, using head and size. 

# In[3]:


df.head()


# In[4]:


df.size


# Use describe... 

# In[5]:


df.describe()


# And info. 

# In[6]:


df.info()


# ### Task 2b. Assess whether dimensions and measures are correct

# On the data source page in Tableau, double check the data types for the applicable columns you selected on the previous step. Pay close attention to the dimensions and measures to assure they are correct. 
# 
# In Python, consider the data types of the columns. *Consider:* Do they make sense? 

# Review the link provided in the previous activity instructions to create the required Tableau visualization. 

# ### Task 2c. Select visualization type(s)

# Select data visualization types that will help you understand and explain the data.
# 
# Now that you know which data columns you’ll use, it is time to decide which data visualization makes the most sense for EDA of the TLC dataset. What type of data visualization(s) would be most helpful? 
# 
# * Line graph
# * Bar chart
# * Box plot
# * Histogram
# * Heat map
# * Scatter plot
# * A geographic map
# 

# ==> ENTER YOUR RESPONSE HERE

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## PACE: Construct 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Construct stage.

# ### Task 3. Data visualization
# 
# You’ve assessed your data, and decided on which data variables are most applicable. It’s time to plot your visualization(s)!
# 

# ### Boxplots

# Perform a check for outliers on relevant columns such as trip distance and trip duration. Remember, some of the best ways to identify the presence of outliers in data are box plots and histograms. 
# 
# **Note:** Remember to convert your date columns to datetime in order to derive total trip duration.  

# In[86]:


# Convert data columns to datetime
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
df.info()


# **trip distance**

# In[8]:


# Create box plot of trip_distance
plt.figure(figsize =(10,2))
sns.boxplot(x=df["trip_distance"])


# In[9]:


# Create histogram of trip_distance
plt.figure(figsize = (10,5))
sns.histplot(df['trip_distance'], bins = range(0,26,1))
plt.title('Trip Distance Histogram')


# **total amount**

# In[10]:


# Create box plot of total_amount
plt.figure(figsize = (10,2))
sns.boxplot(x=df['total_amount'], fliersize = 1)
plt.title('Total Amount')


# In[30]:


# Create histogram of total_amount
plt.figure(figsize = (10,5))
sns.histplot(df['total_amount'],bins =range(-20, 120,5))
plt.title('Total Amount Histogram')


# **tip amount**

# In[11]:


# Create box plot of tip_amount
plt.figure(figsize = (7,2))
sns.boxplot(x=df['tip_amount'], fliersize =1)
plt.title('Tip Amount')


# In[29]:


# Create histogram of tip_amount
plt.figure(figsize = (10,5))
ax = sns.histplot(df['tip_amount'], bins = range(-5, 20, 1))
ax.set_xticks(range(0,21,2))
ax.set_xticklabels(range(0,21,2))
plt.title('TIp Amount histogram')


# **tip_amount by vendor**

# In[19]:


# Create histogram of tip_amount by vendor
plt.figure(figsize = (10,5))
ax = sns.histplot(data = df, x = df['tip_amount'], hue = df['VendorID'], bins = range(-5, 20, 1), multiple = 'stack',
            palette = 'pastel')
ax.set_xticks(range(-5, 20, 1))
plt.title('Tip Amount By Vendor')


# Next, zoom in on the upper end of the range of tips to check whether vendor one gets noticeably more of the most generous tips.

# In[37]:


# Create histogram of tip_amount by vendor for tips > $10 
tips_above_10 = df[df['tip_amount'] > 10]  
plt.figure(figsize = (10,5))
ax = sns.histplot(data = tips_above_10, x = 'tip_amount', hue = 'VendorID', multiple = 'stack',
                 bins = range(5, 60, 2), palette = 'pastel')
ax.set_xticks(range(5, 60, 5))
plt.title('Tip Amount more than $10')


# **Mean tips by passenger count**
# 
# Examine the unique values in the `passenger_count` column.

# In[42]:


#==> ENTER YOUR CODE HERE
df['passenger_count'].value_counts()


# In[58]:


# Calculate mean tips by passenger_count
mean_tips_by_passenger_count = df.groupby('passenger_count').mean()[['tip_amount']]
mean_tips_by_passenger_count


# In[83]:


# Create bar plot for mean tips by passenger count
data = mean_tips_by_passenger_count.tail(6)
plt.figure(figsize = (12,7))
ax = sns.barplot(data = data, x = data.index, y = 'tip_amount', palette = 'pastel')
ax.axhline(df['tip_amount'].mean(), ls = '--', color = 'green', label = 'Global Mean')
ax.legend()
plt.title('Mean tip amount by passenger count', fontsize=16);


# **Create month and day columns**

# In[87]:


# Create a month column
df['month'] = df['tpep_pickup_datetime'].dt.month_name()

# Create a day column
df['day'] = df['tpep_pickup_datetime'].dt.day_name()


# **Plot total ride count by month**
# 
# Begin by calculating total ride count by month.

# In[89]:


# Get total number of rides for each month
monthly_rides = df['month'].value_counts()


# Reorder the results to put the months in calendar order.

# In[91]:


# Reorder the monthly ride list so months go in order
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
monthly_rides = monthly_rides.reindex(index = month_order)


# In[92]:


# Show the index
monthly_rides.index


# In[98]:


# Create a bar plot of total rides per month
plt.figure(figsize = (12, 7))
ax = sns.barplot( x= monthly_rides.index, y = monthly_rides)
ax.set_xticklabels(month_order)
plt.title('Ride Count By Month', fontsize = 16);


# **Plot total ride count by day**
# 
# Repeat the above process, but now calculate the total rides by day of the week.

# In[101]:


# Repeat the above process, this time for rides by day
day_rides = df['day'].value_counts()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']
day_rides = day_rides.reindex(index = day_order)
day_rides


# In[105]:


# Create bar plot for ride count by day
plt.figure(figsize =(12, 7))
ax = sns.barplot(x = day_rides.index, y = day_rides)
ax.set_xticklabels(day_order)
plt.title('Ride Count By Day', fontsize = 16);


# **Plot total revenue by day of the week**
# 
# Repeat the above process, but now calculate the total revenue by day of the week.

# In[113]:


# Repeat the process, this time for total revenue by day
revenue_by_day = df.groupby('day').sum()[['total_amount']]
revenue_by_day = revenue_by_day.reindex(index = day_order)
revenue_by_day


# In[122]:


# Create bar plot of total revenue by day
plt.figure(figsize =(12, 7))
ax = sns.barplot(x = revenue_by_day.index, y = revenue_by_day['total_amount'])
ax.set_xticklabels(day_order)
ax.set_ylabel('Revenue(USD)')
plt.title('Total Revenue By Day', fontsize = 16);


# **Plot total revenue by month**

# In[124]:


# Repeat the process, this time for total revenue by month
revenue_by_month = df.groupby('month').sum()[['total_amount']].reindex(index = month_order)
revenue_by_month


# In[126]:


# Create a bar plot of total revenue by month
plt.figure(figsize = (12, 7))
ax = sns.barplot(x = revenue_by_month.index, y = revenue_by_month['total_amount'])
ax.set_xticklabels(month_order)
ax.set_ylabel('Revenue (USD)')
plt.title('Total Revenue By Month', fontsize = 16);


# #### Scatter plot

# You can create a scatterplot in Tableau Public, which can be easier to manipulate and present. If you'd like step by step instructions, you can review the following link. Those instructions create a scatterplot showing the relationship between total_amount and trip_distance. Consider adding the Tableau visualization to your executive summary, and adding key insights from your findings on those two variables.

# [Tableau visualization guidelines](https://docs.google.com/document/d/1pcfUlttD2Y_a9A4VrKPzikZWCAfFLsBAhuKuomjcUjA/template/preview)

# **Plot mean trip distance by drop-off location**

# In[130]:


# Get number of unique drop-off location IDs
df['DOLocationID'].nunique()


# In[138]:


# Calculate the mean trip distance for each drop-off location
distance_dropoff = df.groupby('DOLocationID').mean()[['trip_distance']]

# Sort the results in descending order by mean trip distance
distance_dropoff = distance_dropoff.sort_values(by = 'trip_distance', ascending = True)
distance_dropoff


# In[145]:


# Create a bar plot of mean trip distances by drop-off location in ascending order by distance
plt.figure(figsize = (12, 7))
ax = sns.barplot(x = distance_dropoff.index, y = distance_dropoff['trip_distance'], order=distance_dropoff.index)
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_ylabel('Trip Distance')
plt.title('Mean Trip distance by drop off location', fontsize = 16);


# ## BONUS CONTENT
# 
# To confirm your conclusion, consider the following experiment:
# 1. Create a sample of coordinates from a normal distribution&mdash;in this case 1,500 pairs of points from a normal distribution with a mean of 10 and a standard deviation of 5
# 2. Calculate the distance between each pair of coordinates 
# 3. Group the coordinates by endpoint and calculate the mean distance between that endpoint and all other points it was paired with
# 4. Plot the mean distance for each unique endpoint

# In[ ]:


#BONUS CONTENT

#1. Generate random points on a 2D plane from a normal distribution
#==> ENTER YOUR CODE HERE

# 2. Calculate Euclidean distances between points in first half and second half of array
#==> ENTER YOUR CODE HERE

# 3. Group the coordinates by "drop-off location", compute mean distance
#==> ENTER YOUR CODE HERE

# 4. Plot the mean distance between each endpoint ("drop-off location") and all points it connected to
#==> ENTER YOUR CODE HERE


# **Histogram of rides by drop-off location**

# First, check to whether the drop-off locations IDs are consecutively numbered. For instance, does it go 1, 2, 3, 4..., or are some numbers missing (e.g., 1, 3, 4...). If numbers aren't all consecutive, the histogram will look like some locations have very few or no rides when in reality there's no bar because there's no location. 

# In[152]:


# Check if all drop-off locations are consecutively numbered
df['DOLocationID'].max() - len(set(df['DOLocationID']))


# To eliminate the spaces in the historgram that these missing numbers would create, sort the unique drop-off location values, then convert them to strings. This will make the histplot function display all bars directly next to each other. 

# In[156]:


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


# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## PACE: Execute 
# 
# Consider the questions in your PACE Strategy Document to reflect on the Execute stage.

# ### Task 4a. Results and evaluation
# 
# Having built visualizations in Tableau and in Python, what have you learned about the dataset? What other questions have your visualizations uncovered that you should pursue? 
# 
# ***Pro tip:*** Put yourself in your client's perspective, what would they want to know? 
# 
# Use the following code fields to pursue any additional EDA based on the visualizations you've already plotted. Also use the space to make sure your visualizations are clean, easily understandable, and accessible. 
# 
# ***Ask yourself:*** Did you consider color, contrast, emphasis, and labeling?
# 
# 

# ==> ENTER YOUR RESPONSE HERE
# 
# I have learned .... 
# 
# My other questions are .... 
# 
# My client would likely want to know ... 
# 

# In[ ]:


#==> ENTER YOUR CODE HERE


# In[ ]:


#==> ENTER YOUR CODE HERE


# ### Task 4b. Conclusion
# *Make it professional and presentable*
# 
# You have visualized the data you need to share with the director now. Remember, the goal of a data visualization is for an audience member to glean the information on the chart in mere seconds.
# 
# *Questions to ask yourself for reflection:*
# Why is it important to conduct Exploratory Data Analysis? Why are the data visualizations provided in this notebook useful?
# 

# 
# EDA is important because ... 
# ==> ENTER YOUR RESPONSE HERE
# 
# 
# Visualizations helped me understand ..
# ==> ENTER YOUR RESPONSE HERE
# 

# You’ve now completed professional data visualizations according to a business need. Well done! 
