# Complete Example of SimpleImputer Methods

from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

# Sample dataset with missing values
data = {
    "Age": [25, 30, np.nan, 40, 35],
    "Salary": [30000, np.nan, 35000, 40000, np.nan],
    "Gender": ["Male", "Female", np.nan, "Male", "Male"]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)


# 1️⃣ Mean Imputation
print("\n--- Mean Imputation (for numeric data) ---")

mean_imputer = SimpleImputer(strategy='mean')
df_mean = df.copy()
df_mean[["Age", "Salary"]] = mean_imputer.fit_transform(df_mean[["Age", "Salary"]])

print(df_mean)


# 2️⃣ Median Imputation
print("\n--- Median Imputation ---")

median_imputer = SimpleImputer(strategy='median')
df_median = df.copy()
df_median[["Age", "Salary"]] = median_imputer.fit_transform(df_median[["Age", "Salary"]])

print(df_median)


# 3️⃣ Most Frequent Imputation
print("\n--- Most Frequent Imputation ---")

freq_imputer = SimpleImputer(strategy='most_frequent')
df_freq = df.copy()
df_freq[["Gender"]] = freq_imputer.fit_transform(df_freq[["Gender"]])

print(df_freq)


# 4️⃣ Constant Imputation
print("\n--- Constant Imputation ---")

constant_imputer = SimpleImputer(strategy='constant', fill_value=0)
df_const = df.copy()
df_const[["Age", "Salary"]] = constant_imputer.fit_transform(df_const[["Age", "Salary"]])

print(df_const)