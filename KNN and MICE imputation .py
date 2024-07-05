from sklearn.impute import KNNImputer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, np.nan, np.nan, 4, 5],
    'D': [1, 2, 3, 4, np.nan]
})
print(df)


# KNN Imputation

imputer = KNNImputer(n_neighbors=2)
df_knn_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Visualize 'B' column before Imputation
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['B'], bins=10, kde=True)
plt.title('Before KNN Imputation - Column B')

# Visualize 'B' column after KNN Imputation
plt.subplot(1, 2, 2)
sns.histplot(df_knn_imputed['B'], bins=10, kde=True)
plt.title('After KNN Imputation - Column B')
plt.show()

# MICE Imputation

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import matplotlib.pyplot as plt
import seaborn as sns

# MICE Imputation
imputer = IterativeImputer(max_iter=10, random_state=0)
df_mice_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Visualize 'C' column before and after MICE Imputation
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(df['C'], bins=10, kde=True)
plt.title('Before MICE Imputation - Column C')

plt.subplot(1, 2, 2)
sns.histplot(df_mice_imputed['C'], bins=10, kde=True)
plt.title('After MICE Imputation - Column C')
plt.show()









