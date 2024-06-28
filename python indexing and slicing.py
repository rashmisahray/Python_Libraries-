import pandas as pd
import numpy as np

data = {
    'Name': ['Rashmi', 'Armaan', 'Yash', 'Priya', 'Priyanka', 'Priyanshu', 'Isha', 'Arpita'],
    'Age': [24, 27, 22, 32, 29, 25, np.nan, 30],
    'City': ['New Delhi', 'Rohtak', 'Faridabad', 'Hyderabad', 'Mumbai', 'Jaipur', 'Manali', 'Rohtak'],
    'Score': [85.6, 90.4, 78.9, 88.2, 92.1, 75.0, 89.5, 91.2]
}

df = pd.DataFrame(data)
print(df)

#indexing
#loc for lable based indexing
df_loc = df.loc[df['Name'].isin(['Rashmi', 'Isha']), ['Name', 'Score']]
print(df_loc)


#iloc for position based indexing
df_iloc = df.iloc[:3, :2]
print(df_iloc)

#boolean indexing
df_age_filtered = df[df['Age'] > 25]
print(df_age_filtered)

#Combined Boolean Indexing
df_age_range_filtered = df[(df['Age'] >= 25) & (df['Age'] <= 30)]
print(df_age_range_filtered)


#slicing

#slicing wiht loc
df_loc_slice = df.loc[:, ['Name', 'City']]
print(df_loc_slice)

#slicing wiht iloc
df_iloc_slice = df.iloc[1:4, 2:4]
print(df_iloc_slice)



