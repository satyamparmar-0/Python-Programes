import pandas as pd

data = {
    "Name" : ["Tom","Jerry","Michael","Sucre"],
    "Age" : [20,22,26, None],
    "City" : ["New York","Los Angeles", "Indore",None]
}

# create the datframe
df = pd.DataFrame(data)

print("DataFrame\n",df)

# find the null value from the data
print("Null values in DataFrame:\n", df.isnull().sum())

# replace the null value with the mean 
df['Age'].fillna(df['Age'].mean(), inplace=True)

print("DataFrame after filling null values:\n", df)

# describe the dataset
print("describe function: \n",df.describe())

# info function 
print("info function: \n", df.info())

# Find the number of rows and columns in the 'dataframe' Pandas series using the 'shape' keyword.
print("Number of rows and columns in DataFrame:\n", df.shape)

# print the first five and last rows of the DataFrame
print("First five rows of DataFrame:\n", df.head())
print("Last five rows of DataFrame:\n", df.tail())

#  Retrieve items from a Pandas series using the indexing method.
print("Retrieve items from a Pandas series using the indexing method:\n", df['Name'][0])

# Arrange the weights in the increasing order using the 'sort_values()' function.
print("DataFrame sorted by Age:\n", df.sort_values(by='Age'))

# Count the number of times each item in the 'dataframe' Pandas series occurs.
print("Count of each Name in DataFrame:\n", df['Name'].value_counts())

print("City column in DataFrame:\n", df["City"])