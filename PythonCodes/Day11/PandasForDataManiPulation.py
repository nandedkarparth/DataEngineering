import pandas as pd

# Creating a DataFrame from a Dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Displaying the DataFrame
print("Original DataFrame:")
print(df.head())
print()

# Getting Information
print("DataFrame Information:")
print(df.info())
print()

# Descriptive Statistics
print("Descriptive Statistics:")
print(df.describe())
print()

# Selecting Columns
names = df['Name']
print("Names Column:")
print(names)
print()

# Filtering Rows Based on a Condition
young_people = df[df['Age'] < 30]
print("Young People:")
print(young_people)
print()

# Handling Missing Data
df_clean = df.dropna()
print("DataFrame without Missing Values:")
print(df_clean)
print()

df_filled = df.fillna(value=0)
print("DataFrame with Missing Values Filled:")
print(df_filled)
print()

# Grouping and Aggregating Data
grouped_by_city = df.groupby('City')
average_age_by_city = grouped_by_city['Age'].mean()
print("Average Age by City:")
print(average_age_by_city)
print()

# Adding and Removing Columns
df['IsAdult'] = df['Age'] >= 18
print("DataFrame with IsAdult Column:")
print(df)
print()

df = df.drop(columns=['IsAdult'])
print("DataFrame without IsAdult Column:")
print(df)
print()

# Sorting Data
df_sorted = df.sort_values(by='Age', ascending=False)
print("DataFrame Sorted by Age:")
print(df_sorted)
print()

# Merging and Concatenating DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
result_concat = pd.concat([df1, df2], ignore_index=True)
print("Concatenated DataFrame:")
print(result_concat)
print()

df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Age': [25, 30]})
result_merge = pd.merge(df1, df2, on='ID')
print("Merged DataFrame:")
print(result_merge)
print()

# Exporting Data
df.to_csv('output.csv', index=False)
print("DataFrame exported to 'output.csv'")
print()

df.to_excel('output.xlsx', index=False)
print("DataFrame exported to 'output.xlsx'")
