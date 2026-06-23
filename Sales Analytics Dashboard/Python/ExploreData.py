import pandas as pd

df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")

print("Original Shape:")
print(df.shape)

df = df.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

df.to_csv("../data/Cleaned_Superstore.csv", index=False)

print("\nCleaned dataset saved successfully!")