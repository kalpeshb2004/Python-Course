
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
 
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)
 
# dataset creation
data = {
    "StaffID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Ishaan", "Meera", "Rohan", "Ananya", "Siddharth",
             "Kavya", "Aditya", "Priya", "Yash", "Sanya"],
    "Age": [23, np.nan, 31, 27, 44, np.nan, 36, 48, 28, 33],
    "Gender": ["Male", "female", "M", "Female", "male",
               "F", "Male", "female", np.nan, "Female"],
    "Department": ["marketing", "Marketing", "IT", "it", "HR",
                   "hr", "Finance", "finance", "IT", "Marketing"],
    "Salary": [42000, 57000, np.nan, 51000, 135000,
               39000, 71000, np.nan, 63000, 48000],
    "Experience_Years": [1, 4, 7, 3, 18, 1, 10, 22, 5, 2],
}
 
df = pd.DataFrame(data)
 
print("=" * 70)
print("ORIGINAL (RAW) DATASET")
print("=" * 70)
print(df)
print("\nMissing values per column:\n", df.isnull().sum())
 
#mssing value handling
 
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
 
print("\n" + "=" * 70)
print("STEP 1: AFTER HANDLING MISSING VALUES")
print("=" * 70)
print(df)
print("\nMissing values per column:\n", df.isnull().sum())
 

#handling inconsistent value
 
gender_map = {
    "male": "Male", "m": "Male",
    "female": "Female", "f": "Female",
}
df["Gender"] = df["Gender"].str.strip().str.lower().map(gender_map)
 
dept_map = {
    "marketing": "Marketing",
    "it": "IT",
    "hr": "HR",
    "finance": "Finance",
}
df["Department"] = df["Department"].str.strip().str.lower().map(dept_map)
 
print("\n" + "=" * 70)
print("STEP 2: AFTER FIXING INCONSISTENT VALUES")
print("=" * 70)
print(df)
print("\nUnique Gender values:", df["Gender"].unique())
print("Unique Department values:", df["Department"].unique())
 

# @feature csaling
numeric_cols = ["Age", "Salary", "Experience_Years"]
 
#standerdization
scaler_std = StandardScaler()
df_standardized = df.copy()
df_standardized[numeric_cols] = scaler_std.fit_transform(df[numeric_cols])
 
#normalization
scaler_mm = MinMaxScaler()
df_normalized = df.copy()
df_normalized[numeric_cols] = scaler_mm.fit_transform(df[numeric_cols])
 
print("\n" + "=" * 70)
print("STEP 3a: STANDARDIZED DATA (StandardScaler, mean=0, std=1)")
print("=" * 70)
print(df_standardized)
 
print("\n" + "=" * 70)
print("STEP 3b: NORMALIZED DATA (MinMaxScaler, range 0-1)")
print("=" * 70)
print(df_normalized)
 
