# assignment 1
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


iris = load_iris()
X = iris.data
y = iris.target

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

sample = [[6.7, 3.1, 4.7, 1.5]]

prediction = model.predict(sample)


print("Input Sample:", sample)
print("Predicted Class:", prediction)
print("Predicted Flower Name:", iris.target_names[prediction[0]])

# Input Sample: [[6.7, 3.1, 4.7, 1.5]]
# Predicted Class: [1]
# Predicted Flower Name: versicolor



# assignment 2
import pandas as pd
from sklearn.datasets import load_wine

# wine dataset laod
wine = load_wine(as_frame=True)
df = wine.frame
df["wine_class"] = df["target"].map(dict(enumerate(wine.target_names)))
df = df.drop(columns="target")

print("RAW DATA (First 5 Rows)")
print(df.head(), "\n")
print("Shape:", df.shape)

# data cleaning
df = df.drop_duplicates()
df = df.dropna()

print("\nAFTER CLEANSING")
print("Shape:", df.shape)
print("Missing Values:\n", df.isna().sum())


# data filter
filtered_df = df[df["alcohol"] > 13]

print("\nAFTER FILTRATION (Alcohol > 13)")
print("Shape:", filtered_df.shape)
print(filtered_df.head())


# aggregation
wine_summary = filtered_df.groupby("wine_class").agg(
    Avg_Alcohol=("alcohol", "mean"),
    Avg_Malic_Acid=("malic_acid", "mean"),
    Count=("wine_class", "count")
).round(2)

print("\nAGGREGATION: Summary by Wine Class")
print(wine_summary)

# RAW DATA (First 5 Rows)
# Shape: (178, 14)

# AFTER CLEANSING
# Shape: (178, 14)

# AFTER FILTRATION (Alcohol > 13)
# Shape: (71, 14)

# AGGREGATION: 

#Avg_Alcohol        Avg_Malic_Acid    Count
# wine_class
# class_0           13.98            2.01     49
# class_1           13.22            2.58     15
# class_2           13.45            3.11      7