import pandas as pd

# Read the dataset
df = pd.read_csv("dataset/intents.csv")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Dataset dimensions
print("\nShape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Dataset information
print("\nInformation:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check unique intents
print("\nUnique Intents:")
print(df["intent"].unique())

# Count examples in each intent
print("\nIntent Counts:")
print(df["intent"].value_counts())