
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

# INTERPOLATION 

# Linear Interpolation
df_interpolate_linear = df.interpolate()
print(df_interpolate_linear)

# using pad method
df_interpolate_pad = df.interpolate(method='pad')
print(df_interpolate_pad)

# using backfill method
df_interpolate_bfill = df.interpolate(method='bfill')
print(df_interpolate_bfill)


# Interpolate Along Rows (Axis=1)
df_interpolate_axis1 = df.interpolate(axis=1)
print(df_interpolate_axis1)

# Using replace() to Handle Null Values

data_with_placeholders = {
    'A': [1, 2, -1, 4, 5],
    'B': [np.nan, 2, 3, 'N/A', 5],
    'C': [1, 'N/A', -1, 4, 5],
    'D': [1, 2, 3, 4, -1]
}

df_placeholders = pd.DataFrame(data_with_placeholders)

df_replace_nan = df_placeholders.replace([-1, 'N/A'], np.nan)
print(df_replace_nan)

# Replace NaN with a Specific Value
df_replace_value = df.replace(np.nan, 0)
print(df_replace_value)

# Replace Different NaN Values in Different Columns
df_replace_colwise = df.replace({'A': np.nan, 'B': np.nan, 'C': np.nan, 'D': np.nan}, {'A': 0, 'B': 1, 'C': 2, 'D': 3})
print(df_replace_colwise)


# End-of-Distribution Imputation

# with Maximum Value Plus a Small Constant
df_end_distribution_max = df.fillna(df.max() + 1)
print(df_end_distribution_max)

# with Minimum Value Minus a Small Constant
df_end_distribution_min = df.fillna(df.min() - 1)
print(df_end_distribution_min)

# with Custom Extreme Value
df_end_distribution_custom = df.fillna(999)
print(df_end_distribution_custom)

# BOXPLOT ANALYSIS

# Creating Box Plot Before and After Imputation
import matplotlib.pyplot as plt
import seaborn as sns

# Original data
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['B'])
plt.title('Before Imputation')

# Imputed data
df_imputed = df.copy()
df_imputed['B'].fillna(df['B'].mean(), inplace=True)
plt.subplot(1, 2, 2)
sns.boxplot(y=df_imputed['B'])
plt.title('After Imputation with Mean')
plt.show()

# Analyzing Skewness and Symmetry with Quartiles

# Calculate quartiles before imputation
q1_before = df['D'].quantile(0.25)
q2_before = df['D'].median()
q3_before = df['D'].quantile(0.75)
print(f'Before Imputation - Q1: {q1_before}, Median: {q2_before}, Q3: {q3_before}')

# Impute and calculate quartiles
df_imputed['D'].fillna(df['D'].median(), inplace=True)
q1_after = df_imputed['D'].quantile(0.25)
q2_after = df_imputed['D'].median()
q3_after = df_imputed['D'].quantile(0.75)
print(f'After Imputation - Q1: {q1_after}, Median: {q2_after}, Q3: {q3_after}')

# Determining Lower and Upper Whiskers for Outlier Detection
q1 = df['C'].quantile(0.25)
q3 = df['C'].quantile(0.75)
iqr = q3 - q1
lower_whisker = q1 - 1.5 * iqr
upper_whisker = q3 + 1.5 * iqr
print(f'Lower Whisker: {lower_whisker}, Upper Whisker: {upper_whisker}')

# Visualizing Data Before and After Imputation with Quartiles
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['C'])
plt.title('Before Imputation')

df_imputed['C'].fillna(df['C'].median(), inplace=True)
plt.subplot(1, 2, 2)
sns.boxplot(y=df_imputed['C'])
plt.title('After Imputation with Median')
plt.show()







