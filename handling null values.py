
# Check for Null Values in a DataFrame

import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, np.nan, np.nan, 4, 5],
    'D': [1, 2, 3, 4, np.nan]
}
df = pd.DataFrame(data)
print(df)

null_values = df.isnull()
print(null_values)

#counting null values
total_null = df.isnull().sum()
print(total_null)

# info() for checking the null values
df.info()


#Handling missing data 

# simple imputation using fillna()

df_filled = df.fillna(0)
print(df_filled)

# filling null values using pad method
df_ffill = df.fillna(method='pad')
print(df_ffill)

# filling null values using bfill method
df_bfill = df.fillna(method='bfill')
print(df_bfill)

# filling null values column wise 
df_column_fill = df.fillna({'A': 0, 'B': 1, 'C': 2, 'D': 3})
print(df_column_fill)

# filling Null Values Along the Rows (axis=1)
df_ffill_axis1 = df.fillna(method='pad', axis=1)
print(df_ffill_axis1)

# filling null values using mean()
df_mean_filled = df.fillna(df.mean())
print(df_mean_filled)

# filling null values using median
df_median_filled = df.fillna(df.median())
print(df_median_filled)

# filling null values using mode
df_mode_filled = df.fillna(df.mode().iloc[0])
print(df_mode_filled)

# filling null values using min()
df_min_filled = df.fillna(df.min())
print(df_min_filled)

# filling null values using max()
df_max_filled = df.fillna(df.max())
print(df_max_filled)


# dropping the null values using dropna()

df_dropped_rows = df.dropna()
print(df_dropped_rows)

# Drop Columns with Any Null Values
df_dropped_columns = df.dropna(axis=1)
print(df_dropped_columns)

# Drop Rows Based on a Subset of Columns
df_dropped_subset = df.dropna(subset=['A', 'B'])
print(df_dropped_subset)

# Drop Rows with a Threshold of Non-Null Values
df_dropped_thresh = df.dropna(thresh=3)
print(df_dropped_thresh)

# Remove Columns with Less than a Certain Number of Non-Null Values
df_dropna_cols_thresh = df.dropna(axis=1, thresh=4)
print(df_dropna_cols_thresh)

# Remove Rows Based on the Condition of Null Values (How)
df_dropna_all = df.dropna(how='all') # default is how='any'
print(df_dropna_all)


